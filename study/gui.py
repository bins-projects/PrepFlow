"""PrepFlow desktop application shell."""

from __future__ import annotations

from collections import OrderedDict
import random
import threading
import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser

from study.loader import list_packs, load_pack
from study.question import check_answer, get_correct_answers, get_prompt
from study.review import ReviewQueue
from study.save_state import (
    delete_saved_session,
    has_saved_session,
    load_session,
    save_session,
)
from study.scoring import ScoreTracker
from study.selection import (
    ChapterSelection,
    aggregate_questions,
    build_loaded_question_lookup,
)
from study.session import SessionManager
from study.update_checker import fetch_latest_version, is_newer_version
from study.version import APP_VERSION, RELEASES_URL


DISPLAY_NAMES = {
    "Fundamentals of Nursing": "Fundamentals",
    "Pharmacy": "Pharm",
    "Medical-Surgical": "Medical-Surgical",
}

DISPLAY_ORDER = {
    "Fundamentals": 0,
    "Pharm": 1,
    "Medical-Surgical": 2,
}


class PrepFlowApp(tk.Tk):
    """Main PrepFlow desktop window."""

    def __init__(self) -> None:
        super().__init__()

        self.title("PrepFlow")
        self.geometry("1000x700")
        self.minsize(820, 580)

        self.current_frame: ttk.Frame | None = None
        self.chapter_variables: dict[tuple[object, str], tk.BooleanVar] = {}
        self.builder_selections: list[ChapterSelection] = []
        self.builder_subjects: list[dict] = []
        self.builder_active_pack_id: str | None = None
        self.builder_check_variables: dict[str, dict[tuple[object, str], tk.BooleanVar]] = {}
        self.builder_card_count_labels: dict[str, ttk.Label] = {}
        self.block_size_variable = tk.StringVar(value="15")

        self._configure_styles()
        self.show_home_screen()

    def _configure_styles(self) -> None:
        style = ttk.Style(self)

        if "clam" in style.theme_names():
            style.theme_use("clam")

        style.configure(
            "Title.TLabel",
            font=("TkDefaultFont", 34, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            font=("TkDefaultFont", 14),
        )
        style.configure(
            "Subject.TButton",
            font=("TkDefaultFont", 15, "bold"),
            padding=(16, 22),
        )
        style.configure(
            "Count.TLabel",
            font=("TkDefaultFont", 11),
        )
        style.configure(
            "Chapter.TCheckbutton",
            font=("TkDefaultFont", 12),
            padding=(8, 8),
        )
        style.configure(
            "Primary.TButton",
            font=("TkDefaultFont", 12, "bold"),
            padding=(18, 10),
        )

    def _replace_screen(self) -> ttk.Frame:
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = ttk.Frame(self, padding=32)
        self.current_frame.pack(fill="both", expand=True)
        return self.current_frame

    def show_home_screen(self) -> None:
        container = self._replace_screen()

        header = ttk.Frame(container)
        header.pack(fill="x", pady=(10, 38))

        ttk.Label(
            header,
            text="PrepFlow",
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x")

        ttk.Label(
            header,
            text="Choose a study category",
            style="Subtitle.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(10, 0))

        if has_saved_session():
            saved_controls = ttk.Frame(container)
            saved_controls.pack(pady=(0, 20))

            ttk.Button(
                saved_controls,
                text="Resume Saved Session",
                style="Primary.TButton",
                command=self._resume_saved_session,
            ).pack(side="left", padx=(0, 8))

            ttk.Button(
                saved_controls,
                text="Start Over",
                command=self._discard_saved_session,
            ).pack(side="left")

        subjects = []
        for pack_info in list_packs():
            pack = load_pack(pack_info["path"])
            pack_id = self._pack_identifier(pack)
            display_name = DISPLAY_NAMES.get(
                pack.get("title", pack_info["title"]),
                pack_info["title"],
            )
            subjects.append(
                {
                    "pack_id": pack_id,
                    "display_name": display_name,
                    "question_count": pack_info["question_count"],
                    "pack_info": pack_info,
                }
            )

        subjects.sort(
            key=lambda subject: DISPLAY_ORDER.get(
                subject["display_name"],
                99,
            )
        )

        cards = ttk.Frame(container)
        cards.pack(fill="both", expand=True)

        for column in range(3):
            cards.columnconfigure(column, weight=1, uniform="subjects")
        cards.rowconfigure(0, weight=1)

        for column, subject in enumerate(subjects):
            card = ttk.Frame(cards, padding=10)
            card.grid(
                row=0,
                column=column,
                padx=10,
                pady=10,
                sticky="nsew",
            )

            ttk.Button(
                card,
                text=subject["display_name"],
                style="Subject.TButton",
                command=lambda selected=subject: self.show_chapter_screen(
                    selected
                ),
            ).pack(fill="both", expand=True)

            ttk.Label(
                card,
                text=f'{subject["question_count"]:,} questions',
                style="Count.TLabel",
                anchor="center",
            ).pack(fill="x", pady=(12, 0))

        ttk.Label(
            container,
            text="Select a category to choose chapters and begin studying.",
            anchor="center",
        ).pack(fill="x", pady=(25, 5))

        update_bar = ttk.Frame(container)
        update_bar.pack(fill="x", pady=(8, 0))

        ttk.Label(
            update_bar,
            text=f"Version {APP_VERSION}",
        ).pack(side="left")

        self.update_button = ttk.Button(
            update_bar,
            text="Check for Updates",
            command=self._check_for_updates,
        )
        self.update_button.pack(side="right")

    def _discard_saved_session(self) -> None:
        confirmed = messagebox.askyesno(
            "Start Over",
            "Start over and permanently delete your saved quiz progress?",
            parent=self,
        )

        if not confirmed:
            return

        delete_saved_session()
        self.show_home_screen()

    def _check_for_updates(self) -> None:
        self.update_button.configure(
            text="Checking...",
            state="disabled",
        )

        def check() -> None:
            try:
                latest_version = fetch_latest_version()
            except RuntimeError as error:
                try:
                    self.after(
                        0,
                        lambda: self._finish_update_check(error=error),
                    )
                except tk.TclError:
                    pass
                return

            try:
                self.after(
                    0,
                    lambda: self._finish_update_check(
                        latest_version=latest_version,
                    ),
                )
            except tk.TclError:
                pass

        threading.Thread(target=check, daemon=True).start()

    def _finish_update_check(
        self,
        latest_version: str | None = None,
        error: RuntimeError | None = None,
    ) -> None:
        self.update_button.configure(
            text="Check for Updates",
            state="normal",
        )

        if error is not None:
            messagebox.showerror(
                "Update Check Failed",
                str(error),
                parent=self,
            )
            return

        if latest_version and is_newer_version(latest_version):
            open_release = messagebox.askyesno(
                "Update Available",
                (
                    f"PrepFlow {latest_version.removeprefix('v')} is "
                    f"available.\n\n"
                    f"You currently have version {APP_VERSION}.\n\n"
                    "Open the download page?"
                ),
                parent=self,
            )

            if open_release:
                webbrowser.open(RELEASES_URL)
            return

        messagebox.showinfo(
            "PrepFlow Is Up to Date",
            f"You are using the latest version: {APP_VERSION}.",
            parent=self,
        )

    def _pack_identifier(self, pack: dict) -> str:
        pack_id = pack.get("pack_id") or pack.get("id")

        if not isinstance(pack_id, str) or not pack_id.strip():
            raise ValueError("Pack is missing a non-empty pack_id")

        return pack_id.strip()

    def _builder_subjects_data(self) -> list[dict]:
        subjects = []

        for pack_info in list_packs():
            pack = load_pack(pack_info["path"])
            pack_id = self._pack_identifier(pack)
            display_name = DISPLAY_NAMES.get(
                pack.get("title", pack_info["title"]),
                pack_info["title"],
            )
            subjects.append(
                {
                    "pack_id": pack_id,
                    "display_name": display_name,
                    "question_count": pack_info["question_count"],
                    "pack_info": pack_info,
                }
            )

        subjects.sort(
            key=lambda subject: DISPLAY_ORDER.get(
                subject["display_name"],
                99,
            )
        )
        return subjects

    def _display_name_for_pack_id(self, pack_id: str) -> str:
        if pack_id in {"fundamentals", "fundamentals-of-nursing"}:
            return "Fundamentals"
        if pack_id == "pharmacy":
            return "Pharm"
        if pack_id in {"medical_surgical", "medical-surgical", "medsurg"}:
            return "Medical-Surgical"

        return pack_id.replace("_", "-").title()

    def _resolve_subject_pack_id(self, subject: dict | None) -> str | None:
        if not isinstance(subject, dict):
            return None

        pack_id = subject.get("pack_id")
        if isinstance(pack_id, str) and pack_id.strip():
            return pack_id.strip()

        pack_info = subject.get("pack_info")
        if isinstance(pack_info, dict):
            pack_id = pack_info.get("pack_id")
            if isinstance(pack_id, str) and pack_id.strip():
                return pack_id.strip()

            path = pack_info.get("path")
            if isinstance(path, str) and path.strip():
                try:
                    pack = load_pack(path)
                except (FileNotFoundError, OSError, TypeError, ValueError):
                    pass
                else:
                    try:
                        return self._pack_identifier(pack)
                    except ValueError:
                        pass

        for builder_subject in self.builder_subjects:
            if not isinstance(builder_subject, dict):
                continue

            subject_pack_id = builder_subject.get("pack_id")
            if isinstance(subject_pack_id, str) and subject_pack_id.strip():
                if builder_subject.get("display_name") == subject.get("display_name"):
                    return subject_pack_id.strip()

            builder_pack_info = builder_subject.get("pack_info")
            if isinstance(builder_pack_info, dict):
                builder_path = builder_pack_info.get("path")
                subject_path = pack_info.get("path") if isinstance(pack_info, dict) else None
                if isinstance(builder_path, str) and builder_path == subject_path:
                    if isinstance(subject_pack_id, str) and subject_pack_id.strip():
                        return subject_pack_id.strip()

        return None

    def _ensure_block_size_variable(self) -> tk.StringVar:
        if not hasattr(self, "block_size_variable") or self.block_size_variable is None:
            self.block_size_variable = tk.StringVar(value="15")
        return self.block_size_variable

    def _selected_count_for_category(self, pack_id: str) -> int:
        return sum(
            1
            for selection in self.builder_selections
            if selection.pack_id == pack_id
        )

    def _validate_block_size(self, selected_question_count: int) -> int | None:
        block_size_var = self._ensure_block_size_variable()
        raw_value = block_size_var.get()
        if not isinstance(raw_value, str):
            raw_value = str(raw_value)
        raw_value = raw_value.strip()

        if not raw_value:
            messagebox.showerror(
                "Block Size",
                "Please enter a block size.",
                parent=self,
            )
            return None

        try:
            block_size = int(raw_value)
        except ValueError:
            messagebox.showerror(
                "Block Size",
                "Block size must be a whole number.",
                parent=self,
            )
            return None

        if block_size < 1:
            messagebox.showerror(
                "Block Size",
                "Block size must be at least 1.",
                parent=self,
            )
            return None

        if selected_question_count and block_size > selected_question_count:
            messagebox.showerror(
                "Block Size",
                (
                    "Block size cannot exceed the number of selected "
                    f"questions ({selected_question_count})."
                ),
                parent=self,
            )
            return None

        return block_size

    def _toggle_builder_selection(
        self,
        pack_id: str,
        chapter_number: object,
        chapter_title: str,
        selected: bool,
    ) -> None:
        selection = ChapterSelection(
            pack_id=pack_id,
            chapter=chapter_number,
            chapter_title=chapter_title,
        )

        existing_index = None
        for index, existing in enumerate(self.builder_selections):
            if (
                existing.pack_id == selection.pack_id
                and existing.chapter == selection.chapter
                and existing.chapter_title == selection.chapter_title
            ):
                existing_index = index
                break

        if selected and existing_index is None:
            self.builder_selections.append(selection)
        elif not selected and existing_index is not None:
            self.builder_selections.pop(existing_index)

        self._refresh_builder_status()

    def _clear_builder(self) -> None:
        for variables in getattr(self, "builder_check_variables", {}).values():
            for variable in variables.values():
                variable.set(False)

        self.builder_selections.clear()
        self._refresh_builder_status()

    def _refresh_builder_status(self) -> None:
        selected_count = len(self.builder_selections)
        word = "chapter" if selected_count == 1 else "chapters"

        selection_label = self.__dict__.get("selection_label")
        if selection_label is not None:
            selection_label.configure(
                text=f"{selected_count} {word} selected"
            )

        start_button = self.__dict__.get("start_button")
        if start_button is not None:
            start_button.configure(
                state="normal" if selected_count else "disabled"
            )

        builder_summary_label = self.__dict__.get("builder_summary_label")
        if builder_summary_label is not None:
            builder_summary_label.configure(
                text=self._builder_summary_text()
            )

        for pack_id, label in self.__dict__.get("builder_card_count_labels", {}).items():
            if hasattr(label, "configure"):
                label.configure(text=f"{self._selected_count_for_category(pack_id)} selected")

    def _builder_summary_text(self) -> str:
        if not self.builder_selections:
            return "Your Quiz is empty."

        grouped: OrderedDict[str, list[ChapterSelection]] = OrderedDict()
        for selection in self.builder_selections:
            display_name = self._display_name_for_pack_id(selection.pack_id)
            grouped.setdefault(display_name, []).append(selection)

        lines = ["Your Quiz"]
        for display_name, selections in grouped.items():
            lines.append(f"• {display_name}")
            for selection in selections:
                if selection.chapter is None:
                    chapter_label = selection.chapter_title
                else:
                    chapter_label = f"Chapter {selection.chapter}: {selection.chapter_title}"
                lines.append(f"  - {chapter_label}")

        return "\n".join(lines)

    def _build_selected_questions(self, packs: list[dict]) -> list[dict]:
        refs = aggregate_questions(packs, self.builder_selections)
        lookup = build_loaded_question_lookup(packs)
        supported_types = {
            "mc",
            "multiple_choice",
            "multiple_response",
            "completion",
            "ordering",
            "ordered_response",
        }

        questions = []
        for ref in refs:
            question = lookup.get((ref.pack_id, ref.question_id))
            if question is None:
                continue

            if question.get("type") not in supported_types:
                continue

            question_copy = dict(question)
            question_copy["_pack_id"] = ref.pack_id
            questions.append(question_copy)

        return questions

    def _build_resume_state(
        self,
        subject_display_name: str,
        selected_packs: list[dict],
        ordered_questions: list[dict],
        current_question: dict | None,
        review_questions: list[dict],
        missed_questions: list[dict],
        score_summary: dict,
        current_index: int,
        block_size: int,
        review_mode: bool,
        block_correct: int,
        block_missed: int,
    ) -> dict:
        def question_ref(question: dict | None) -> dict | None:
            if question is None:
                return None
            return {
                "pack_id": question.get("_pack_id") or "",
                "question_id": question.get("id"),
            }

        return {
            "subject_display_name": subject_display_name,
            "subject_question_count": len(ordered_questions),
            "selected_packs": selected_packs,
            "question_order": [
                question_ref(question)
                for question in ordered_questions
            ],
            "current_index": current_index,
            "current_question": question_ref(current_question),
            "block_size": block_size,
            "review_mode": review_mode,
            "review_question_refs": [
                question_ref(question)
                for question in review_questions
            ],
            "score": score_summary,
            "missed_question_refs": [
                question_ref(question)
                for question in missed_questions
            ],
            "block_correct": block_correct,
            "block_missed": block_missed,
        }

    def _restore_session_state(self, session_state: dict, packs: list[dict]) -> dict:
        if not isinstance(session_state, dict):
            raise ValueError("Session state must be a mapping")

        selected_packs = session_state.get("selected_packs")
        if not isinstance(selected_packs, list):
            raise ValueError("selected_packs must be a list")

        pack_lookup = {}
        for pack in packs:
            pack_id = self._pack_identifier(pack)
            pack_lookup[pack_id] = pack

        resolved_packs = []
        for pack_info in selected_packs:
            if not isinstance(pack_info, dict):
                raise ValueError("selected_packs entries must be mappings")
            pack_id = pack_info.get("pack_id")
            if not isinstance(pack_id, str) or not pack_id.strip():
                raise ValueError("selected pack is missing a valid pack_id")
            pack = pack_lookup.get(pack_id)
            if pack is None:
                raise ValueError(f"Pack {pack_id!r} was not found")
            resolved_packs.append({"pack_id": pack_id, "pack": pack})

        lookup = build_loaded_question_lookup([entry["pack"] for entry in resolved_packs])

        ordered_questions = []
        for ref in session_state.get("question_order", []):
            if not isinstance(ref, dict):
                raise ValueError("question_order entries must be mappings")
            pack_id = ref.get("pack_id")
            question_id = ref.get("question_id")
            if not isinstance(pack_id, str) or not pack_id.strip():
                raise ValueError("question ref is missing a pack_id")
            if not isinstance(question_id, str) or not question_id.strip():
                raise ValueError("question ref is missing a question_id")

            question = lookup.get((pack_id, question_id))
            if question is None:
                raise ValueError(f"Question {question_id!r} was not found in pack {pack_id!r}")

            question_copy = dict(question)
            question_copy["_pack_id"] = pack_id
            ordered_questions.append(question_copy)

        current_question = None
        current_question_ref = session_state.get("current_question")
        if current_question_ref is not None:
            if not isinstance(current_question_ref, dict):
                raise ValueError("current_question must be a mapping")
            pack_id = current_question_ref.get("pack_id")
            question_id = current_question_ref.get("question_id")
            if not isinstance(pack_id, str) or not pack_id.strip():
                raise ValueError("current_question is missing a pack_id")
            if not isinstance(question_id, str) or not question_id.strip():
                raise ValueError("current_question is missing a question_id")
            question = lookup.get((pack_id, question_id))
            if question is None:
                raise ValueError(f"Question {question_id!r} was not found in pack {pack_id!r}")
            current_question = dict(question)
            current_question["_pack_id"] = pack_id

        review_questions = []
        for ref in session_state.get("review_question_refs", []):
            if not isinstance(ref, dict):
                raise ValueError("review_question_refs entries must be mappings")
            pack_id = ref.get("pack_id")
            question_id = ref.get("question_id")
            question = lookup.get((pack_id, question_id))
            if question is None:
                raise ValueError(f"Question {question_id!r} was not found in pack {pack_id!r}")
            question_copy = dict(question)
            question_copy["_pack_id"] = pack_id
            review_questions.append(question_copy)

        missed_questions = []
        for ref in session_state.get("missed_question_refs", []):
            if not isinstance(ref, dict):
                raise ValueError("missed_question_refs entries must be mappings")
            pack_id = ref.get("pack_id")
            question_id = ref.get("question_id")
            question = lookup.get((pack_id, question_id))
            if question is None:
                raise ValueError(f"Question {question_id!r} was not found in pack {pack_id!r}")
            question_copy = dict(question)
            question_copy["_pack_id"] = pack_id
            missed_questions.append(question_copy)

        return {
            "ordered_questions": ordered_questions,
            "current_question": current_question,
            "review_questions": review_questions,
            "missed_questions": missed_questions,
            "current_index": session_state.get("current_index", 0),
            "block_size": session_state.get("block_size", 15),
            "review_mode": session_state.get("review_mode", False),
            "score": session_state.get("score", {}),
            "block_correct": session_state.get("block_correct", 0),
            "block_missed": session_state.get("block_missed", 0),
        }

    def _restore_questions_from_state(self, state: dict, packs: list[dict]) -> list[dict]:
        session_state = state.get("session", state)
        restored = self._restore_session_state(session_state, packs)
        return restored["ordered_questions"]

    def show_chapter_screen(self, subject: dict) -> None:
        container = self._replace_screen()
        self.builder_subjects = self._builder_subjects_data()
        self.builder_active_pack_id = self._resolve_subject_pack_id(subject)

        top_bar = ttk.Frame(container)
        top_bar.pack(fill="x")

        ttk.Button(
            top_bar,
            text="← Back",
            command=self.show_home_screen,
        ).pack(side="left")

        ttk.Label(
            top_bar,
            text="Build Your Quiz",
            style="Title.TLabel",
            anchor="center",
        ).pack(side="left", expand=True)

        category_frame = ttk.Frame(container)
        category_frame.pack(fill="x", pady=(18, 12))

        self.builder_card_count_labels = {}
        for builder_subject in self.builder_subjects:
            pack_id = builder_subject["pack_id"]
            card = ttk.Frame(category_frame, padding=(10, 8))
            card.pack(side="left", padx=(0, 8), pady=(0, 4))
            is_active = pack_id == self.builder_active_pack_id
            button = ttk.Button(
                card,
                text=builder_subject["display_name"],
                style="Subject.TButton" if is_active else "Primary.TButton",
                command=lambda selected=builder_subject: self.show_chapter_screen(selected),
            )
            button.pack()
            count_label = ttk.Label(card, text="0 selected", style="Count.TLabel")
            count_label.pack(pady=(6, 0))
            self.builder_card_count_labels[pack_id] = count_label

        ttk.Label(
            container,
            text="Choose chapters from the active category.",
            style="Subtitle.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(0, 12))

        controls = ttk.Frame(container)
        controls.pack(fill="x", pady=(0, 10))
        self.selection_label = ttk.Label(controls, text="0 chapters selected")
        self.selection_label.pack(side="left")

        block_size_frame = ttk.Frame(controls)
        block_size_frame.pack(side="left", padx=(16, 0))
        ttk.Label(block_size_frame, text="Block size").pack(side="left")
        self.block_size_variable = self._ensure_block_size_variable()
        ttk.Entry(
            block_size_frame,
            textvariable=self.block_size_variable,
            width=6,
        ).pack(side="left", padx=(6, 0))

        clear_button = ttk.Button(
            controls,
            text="Clear Quiz",
            command=self._clear_builder,
        )
        clear_button.pack(side="right")

        self.start_button = ttk.Button(
            controls,
            text="Start Studying",
            style="Primary.TButton",
            state="disabled",
            command=lambda: self._start_studying(subject),
        )
        self.start_button.pack(side="right", padx=(0, 8))

        self.builder_summary_label = ttk.Label(
            container,
            text=self._builder_summary_text(),
            justify="left",
            wraplength=900,
        )
        self.builder_summary_label.pack(fill="x", pady=(0, 12))

        chapter_section = ttk.Frame(container)
        chapter_section.pack(fill="both", expand=True)

        if self.builder_active_pack_id is None:
            self.builder_active_pack_id = self._resolve_subject_pack_id(subject)

        active_subject = next(
            (
                builder_subject
                for builder_subject in self.builder_subjects
                if builder_subject["pack_id"] == self.builder_active_pack_id
            ),
            subject,
        )
        pack_info = active_subject["pack_info"]
        pack = load_pack(pack_info["path"])
        pack_id = self._pack_identifier(pack)

        chapter_counts: OrderedDict[tuple[object, str], int] = OrderedDict()
        for question in pack["questions"]:
            chapter_number = question.get("chapter")
            chapter_title = question.get("chapter_title") or "Untitled Chapter"
            key = (chapter_number, chapter_title)
            chapter_counts[key] = chapter_counts.get(key, 0) + 1

        if pack_id not in self.builder_check_variables:
            self.builder_check_variables[pack_id] = {}

        for key in chapter_counts:
            chapter_number, chapter_title = key
            if (chapter_number, chapter_title) not in self.builder_check_variables[pack_id]:
                existing_selection = next(
                    (
                        selection
                        for selection in self.builder_selections
                        if (
                            selection.pack_id == pack_id
                            and selection.chapter == chapter_number
                            and selection.chapter_title == chapter_title
                        )
                    ),
                    None,
                )
                self.builder_check_variables[pack_id][(chapter_number, chapter_title)] = tk.BooleanVar(
                    value=existing_selection is not None
                )

        chapter_canvas = tk.Canvas(chapter_section, highlightthickness=0)
        self.chapter_canvas = chapter_canvas
        chapter_scrollbar = ttk.Scrollbar(
            chapter_section,
            orient="vertical",
            command=chapter_canvas.yview,
        )
        chapter_canvas.configure(yscrollcommand=chapter_scrollbar.set)
        chapter_canvas.pack(side="left", fill="both", expand=True)
        chapter_scrollbar.pack(side="right", fill="y")

        chapter_frame = ttk.Frame(chapter_canvas)
        chapter_canvas.create_window((0, 0), window=chapter_frame, anchor="nw")

        def _update_scroll_region(event=None) -> None:
            chapter_canvas.configure(scrollregion=chapter_canvas.bbox("all"))

        chapter_frame.bind("<Configure>", _update_scroll_region)
        chapter_canvas.bind("<Configure>", _update_scroll_region)
        chapter_canvas.bind("<MouseWheel>", self._scroll_chapter_canvas)
        chapter_canvas.bind("<Button-4>", self._scroll_chapter_canvas)
        chapter_canvas.bind("<Button-5>", self._scroll_chapter_canvas)

        for row, ((chapter_number, chapter_title), count) in enumerate(chapter_counts.items()):
            if chapter_number is None:
                label = chapter_title
            else:
                label = f"Chapter {chapter_number}: {chapter_title}"

            label = f"{label}  —  {count:,} questions"

            variable = self.builder_check_variables[pack_id][(chapter_number, chapter_title)]
            ttk.Checkbutton(
                chapter_frame,
                text=label,
                variable=variable,
                style="Chapter.TCheckbutton",
                command=lambda chapter_number=chapter_number, chapter_title=chapter_title, pack_id=pack_id: self._toggle_builder_selection(
                    pack_id,
                    chapter_number,
                    chapter_title,
                    self.builder_check_variables[pack_id][(chapter_number, chapter_title)].get(),
                ),
            ).grid(row=row, column=0, sticky="w", padx=10, pady=2)

        self._refresh_builder_status()

    def _scroll_chapter_canvas(self, event) -> None:
        if not hasattr(self, "chapter_canvas"):
            return

        if event.num == 4:
            delta = -1
        elif event.num == 5:
            delta = 1
        else:
            delta = -1 if getattr(event, "delta", 0) > 0 else 1

        self.chapter_canvas.yview_scroll(delta, "units")

    def _start_studying(self, subject: dict) -> None:
        selected_pack_ids = {
            selection.pack_id for selection in self.builder_selections
        }

        selected_pack_entries = []
        for pack_info in list_packs():
            pack = load_pack(pack_info["path"])
            pack_id = self._pack_identifier(pack)
            if pack_id in selected_pack_ids:
                selected_pack_entries.append(
                    {
                        "pack_id": pack_id,
                        "path": str(pack_info["path"]),
                        "pack": pack,
                    }
                )

        selected_questions = self._build_selected_questions(
            [entry["pack"] for entry in selected_pack_entries]
        )

        if not selected_questions:
            self._show_message_screen(
                title="No Questions Available",
                message=(
                    "No supported study questions were found in the "
                    "selected chapters."
                ),
                button_text="Back to Chapters",
                command=lambda: self.show_chapter_screen(subject),
            )
            return

        block_size = self._validate_block_size(len(selected_questions))
        if block_size is None:
            return

        self.session_subject = {
            "display_name": "Your Quiz",
            "question_count": len(selected_questions),
            "pack_info": {
                "selected_packs": [
                    {"pack_id": entry["pack_id"], "path": entry["path"]}
                    for entry in selected_pack_entries
                ],
            },
        }
        self.session_pack_path = [
            entry["path"] for entry in selected_pack_entries
        ]
        self.session = SessionManager(
            selected_questions,
            block_size=block_size,
            shuffle=True,
        )
        self.score = ScoreTracker()
        self.review = ReviewQueue()

        self.review_mode = False
        self.current_question = None
        self.answer_submitted = False

        self.block_correct = 0
        self.block_missed = 0

        self._load_next_first_attempt_question()

    def _current_block_size(self) -> int:
        total_questions = self.session.total_questions()
        block_size = self.session.block_size
        block_number = self.session.current_block_number()

        block_start = (block_number - 1) * block_size
        remaining = total_questions - block_start

        return min(block_size, remaining)

    def _total_block_count(self) -> int:
        total_questions = self.session.total_questions()
        block_size = self.session.block_size

        return max(1, (total_questions + block_size - 1) // block_size)

    def _load_next_first_attempt_question(self) -> None:
        if not self.session.has_next_question():
            self._show_session_complete()
            return

        self.review_mode = False
        self.current_question = self.session.get_next_question()
        self.answer_submitted = False
        self._show_question_screen()

    def _show_question_screen(self) -> None:
        question = self.current_question
        self._save_current_session()
        container = self._replace_screen()

        top_bar = ttk.Frame(container)
        top_bar.pack(fill="x")

        ttk.Button(
            top_bar,
            text="Save & Quit",
            command=self.show_home_screen,
        ).pack(side="left")

        ttk.Label(
            top_bar,
            text=self.session_subject["display_name"],
            style="Subtitle.TLabel",
        ).pack(side="left", expand=True)

        block_number = self.session.current_block_number()
        total_blocks = self._total_block_count()

        if self.review_mode:
            position_text = (
                f"Block {block_number} of {total_blocks} • "
                f"Review • {self.review.count() + 1} remaining"
            )
        else:
            position_text = (
                f"Block {block_number} of {total_blocks} • "
                f"Question {self.session.question_in_block()} "
                f"of {self._current_block_size()}"
            )

        ttk.Label(
            top_bar,
            text=position_text,
        ).pack(side="right")

        progress = ttk.Progressbar(
            container,
            maximum=self.session.total_questions(),
            value=self.session.completed_questions(),
        )
        progress.pack(fill="x", pady=(18, 12))

        # Keep navigation controls visible regardless of question length.
        bottom_bar = ttk.Frame(container)
        bottom_bar.pack(side="bottom", fill="x", pady=(12, 0))

        summary = self.score.summary()

        ttk.Label(
            bottom_bar,
            text=(
                f'First pass: {summary["first_attempt_correct"]} correct, '
                f'{summary["first_attempt_missed"]} missed'
            ),
        ).pack(side="left")

        self.submit_button = ttk.Button(
            bottom_bar,
            text="Submit Answer",
            style="Primary.TButton",
            state="disabled",
            command=self._submit_current_answer,
        )
        self.submit_button.pack(side="right")

        self.next_button = ttk.Button(
            bottom_bar,
            text="Continue",
            style="Primary.TButton",
            command=self._advance_after_answer,
        )

        # The question, choices, feedback, and rationale scroll together.
        content_container = ttk.Frame(container)
        content_container.pack(fill="both", expand=True)

        canvas = tk.Canvas(
            content_container,
            highlightthickness=0,
            borderwidth=0,
        )
        scrollbar = ttk.Scrollbar(
            content_container,
            orient="vertical",
            command=canvas.yview,
        )
        content = ttk.Frame(canvas, padding=(2, 10, 12, 18))

        content.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            ),
        )

        canvas_window = canvas.create_window(
            (0, 0),
            window=content,
            anchor="nw",
        )

        canvas.bind(
            "<Configure>",
            lambda event: canvas.itemconfigure(
                canvas_window,
                width=event.width,
            ),
        )

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        ttk.Label(
            content,
            text=get_prompt(question),
            font=("TkDefaultFont", 15),
            wraplength=820,
            justify="left",
        ).pack(fill="x", anchor="w", pady=(0, 20))

        question_type = self._normalized_question_type(question)

        self.choices_frame = ttk.Frame(content)
        self.choices_frame.pack(fill="x")
        choices_frame = self.choices_frame

        if question_type == "multiple_choice":
            self.selected_answer = tk.StringVar(value="")

            for choice in question.get("choices", []):
                ttk.Radiobutton(
                    choices_frame,
                    text=f'{choice["label"]}. {choice["text"]}',
                    variable=self.selected_answer,
                    value=choice["label"],
                    command=self._update_submit_state,
                ).pack(
                    fill="x",
                    anchor="w",
                    padx=10,
                    pady=8,
                )

        elif question_type == "multiple_response":
            self.response_variables = {}

            ttk.Label(
                choices_frame,
                text="Select all that apply.",
                font=("TkDefaultFont", 11, "italic"),
            ).pack(fill="x", anchor="w", padx=10, pady=(0, 6))

            for choice in question.get("choices", []):
                variable = tk.BooleanVar(value=False)
                self.response_variables[choice["label"]] = variable

                ttk.Checkbutton(
                    choices_frame,
                    text=f'{choice["label"]}. {choice["text"]}',
                    variable=variable,
                    command=self._update_submit_state,
                ).pack(
                    fill="x",
                    anchor="w",
                    padx=10,
                    pady=8,
                )

        elif question_type == "completion":
            self.completion_answer = tk.StringVar(value="")

            ttk.Label(
                choices_frame,
                text="Enter your answer:",
                font=("TkDefaultFont", 11, "bold"),
            ).pack(fill="x", anchor="w", padx=10, pady=(0, 6))

            completion_entry = ttk.Entry(
                choices_frame,
                textvariable=self.completion_answer,
                font=("TkDefaultFont", 13),
            )
            completion_entry.pack(fill="x", padx=10, pady=8)
            completion_entry.bind(
                "<KeyRelease>",
                lambda event: self._update_submit_state(),
            )
            completion_entry.focus_set()

        elif question_type == "ordered_response":
            self.ordered_choices = list(question.get("choices", []))

            ttk.Label(
                choices_frame,
                text=(
                    "Click and hold an item, then drag it into the "
                    "correct position."
                ),
                font=("TkDefaultFont", 11, "italic"),
                wraplength=800,
                justify="left",
            ).pack(fill="x", anchor="w", padx=10, pady=(0, 8))

            ordering_area = ttk.Frame(choices_frame)
            ordering_area.pack(fill="x", padx=10)

            self.ordering_listbox = tk.Listbox(
                ordering_area,
                height=max(4, len(self.ordered_choices)),
                font=("TkDefaultFont", 12),
                selectmode="browse",
                exportselection=False,
            )
            self.ordering_listbox.pack(
                fill="both",
                expand=True,
            )

            self._dragged_order_index = None

            self.ordering_listbox.bind(
                "<Button-1>",
                self._start_order_drag,
            )
            self.ordering_listbox.bind(
                "<B1-Motion>",
                self._drag_ordered_choice,
            )
            self.ordering_listbox.bind(
                "<ButtonRelease-1>",
                self._finish_order_drag,
            )

            self._refresh_ordering_listbox()

        self.feedback_frame = ttk.Frame(content)
        self.feedback_frame.pack(fill="x", pady=(20, 0))

    @staticmethod
    def _normalized_question_type(question: dict) -> str:
        question_type = question.get("type")

        if question_type in {"mc", "multiple_choice"}:
            return "multiple_choice"

        if question_type in {"ordering", "ordered_response"}:
            return "ordered_response"

        return question_type

    def _current_user_answer(self) -> str:
        question_type = self._normalized_question_type(
            self.current_question
        )

        if question_type == "multiple_choice":
            return self.selected_answer.get()

        if question_type == "multiple_response":
            return "".join(
                label
                for label, variable in self.response_variables.items()
                if variable.get()
            )

        if question_type == "completion":
            return self.completion_answer.get().strip()

        if question_type == "ordered_response":
            return "".join(
                choice["label"]
                for choice in self.ordered_choices
            )

        return ""

    def _update_submit_state(self) -> None:
        if self.answer_submitted:
            return

        question_type = self._normalized_question_type(
            self.current_question
        )

        if question_type == "ordered_response":
            has_answer = bool(self.ordered_choices)
        else:
            has_answer = bool(self._current_user_answer())

        self.submit_button.configure(
            state="normal" if has_answer else "disabled"
        )

    def _start_order_drag(self, event) -> None:
        index = self.ordering_listbox.nearest(event.y)

        if 0 <= index < len(self.ordered_choices):
            self._dragged_order_index = index
            self.ordering_listbox.selection_clear(0, tk.END)
            self.ordering_listbox.selection_set(index)
            self.ordering_listbox.activate(index)

    def _drag_ordered_choice(self, event) -> None:
        if self._dragged_order_index is None:
            return

        target_index = self.ordering_listbox.nearest(event.y)
        target_index = max(
            0,
            min(target_index, len(self.ordered_choices) - 1),
        )

        if target_index == self._dragged_order_index:
            return

        choice = self.ordered_choices.pop(self._dragged_order_index)
        self.ordered_choices.insert(target_index, choice)
        self._dragged_order_index = target_index

        self._refresh_ordering_listbox()
        self.ordering_listbox.selection_set(target_index)
        self.ordering_listbox.activate(target_index)
        self.ordering_listbox.see(target_index)

    def _finish_order_drag(self, event) -> None:
        if self._dragged_order_index is not None:
            self.ordering_listbox.selection_clear(0, tk.END)
            self.ordering_listbox.selection_set(
                self._dragged_order_index
            )

        self._dragged_order_index = None

    def _refresh_ordering_listbox(self) -> None:
        self.ordering_listbox.delete(0, tk.END)

        for choice in self.ordered_choices:
            self.ordering_listbox.insert(
                tk.END,
                f'{choice["label"]}. {choice["text"]}',
            )

        self._update_submit_state()

    def _move_ordered_choice(self, direction: int) -> None:
        selection = self.ordering_listbox.curselection()

        if not selection:
            return

        current_index = selection[0]
        new_index = current_index + direction

        if new_index < 0 or new_index >= len(self.ordered_choices):
            return

        self.ordered_choices[current_index], self.ordered_choices[new_index] = (
            self.ordered_choices[new_index],
            self.ordered_choices[current_index],
        )

        self._refresh_ordering_listbox()
        self.ordering_listbox.selection_set(new_index)
        self.ordering_listbox.activate(new_index)
        self.ordering_listbox.see(new_index)

    def _submit_current_answer(self) -> None:
        if self.answer_submitted:
            return

        question = self.current_question
        correct_answers = get_correct_answers(question)

        question_type = self._normalized_question_type(question)

        is_correct = check_answer(
            self._current_user_answer(),
            correct_answers,
            question_type,
        )

        self.answer_submitted = True
        self.submit_button.configure(state="disabled")
        self.choices_frame.destroy()

        if self.review_mode:
            self.score.record_review_answer(is_correct)

            if not is_correct:
                self.review.add(question)
        else:
            self.score.record_answer(question, is_correct)

            if is_correct:
                self.block_correct += 1
            else:
                self.block_missed += 1
                self.review.add(question)

        if is_correct:
            feedback_text = "Correct!"
        else:
            correct_text = ", ".join(correct_answers)
            feedback_text = f"Incorrect. Correct answer: {correct_text}"

        ttk.Label(
            self.feedback_frame,
            text=feedback_text,
            font=("TkDefaultFont", 13, "bold"),
            wraplength=850,
            justify="left",
        ).pack(fill="x", anchor="w", pady=(0, 12))

        ttk.Label(
            self.feedback_frame,
            text="Rationale",
            font=("TkDefaultFont", 12, "bold"),
        ).pack(fill="x", anchor="w")

        ttk.Label(
            self.feedback_frame,
            text=question.get("rationale", ""),
            wraplength=850,
            justify="left",
        ).pack(fill="x", anchor="w", pady=(6, 0))

        self.next_button.pack(side="right")
        self.submit_button.pack_forget()

    def _advance_after_answer(self) -> None:
        if self.review_mode:
            if self.review.has_questions():
                self.current_question = self.review.next_question()
                self.answer_submitted = False
                self._show_question_screen()
            else:
                self._show_review_complete()
            return

        block_finished = self.session.is_block_complete()
        session_finished = not self.session.has_next_question()

        if block_finished or session_finished:
            self._show_block_complete()
        else:
            self._load_next_first_attempt_question()

    def _show_block_complete(self) -> None:
        container = self._replace_screen()
        block_number = self.session.current_block_number()

        ttk.Label(
            container,
            text=f"Block {block_number} Complete",
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(70, 18))

        total = self.block_correct + self.block_missed

        ttk.Label(
            container,
            text=(
                f"First-pass score: {self.block_correct} of {total}\n"
                f"Missed questions to review: {self.review.count()}"
            ),
            style="Subtitle.TLabel",
            anchor="center",
            justify="center",
        ).pack(fill="x", pady=(0, 30))

        if self.review.has_questions():
            ttk.Button(
                container,
                text="Review Missed Questions",
                style="Primary.TButton",
                command=self._begin_review,
            ).pack()
        elif self.session.has_next_question():
            ttk.Button(
                container,
                text="Begin Next Block",
                style="Primary.TButton",
                command=self._begin_next_block,
            ).pack()
        else:
            ttk.Button(
                container,
                text="View Session Results",
                style="Primary.TButton",
                command=self._show_session_complete,
            ).pack()

    def _begin_review(self) -> None:
        self.review_mode = True
        self.current_question = self.review.next_question()
        self.answer_submitted = False
        self._show_question_screen()

    def _show_review_complete(self) -> None:
        container = self._replace_screen()

        ttk.Label(
            container,
            text="Review Complete",
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(80, 18))

        ttk.Label(
            container,
            text="All missed questions from this block are now mastered.",
            style="Subtitle.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(0, 30))

        if self.session.has_next_question():
            ttk.Button(
                container,
                text="Begin Next Block",
                style="Primary.TButton",
                command=self._begin_next_block,
            ).pack()
        else:
            ttk.Button(
                container,
                text="View Session Results",
                style="Primary.TButton",
                command=self._show_session_complete,
            ).pack()

    def _begin_next_block(self) -> None:
        self.block_correct = 0
        self.block_missed = 0
        self.review_mode = False
        self._load_next_first_attempt_question()

    def _save_current_session(self) -> None:
        if self.current_question is None:
            return

        summary = self.score.summary()
        selected_packs = []
        if self.session_subject.get("pack_info", {}).get("selected_packs"):
            selected_packs = self.session_subject["pack_info"][
                "selected_packs"
            ]

        save_session(
            self._build_resume_state(
                subject_display_name=self.session_subject["display_name"],
                selected_packs=selected_packs,
                ordered_questions=self.session.questions,
                current_question=self.current_question,
                review_questions=list(self.review.questions),
                missed_questions=list(self.score.missed_questions),
                score_summary=summary,
                current_index=self.session.current_index,
                block_size=self.session.block_size,
                review_mode=self.review_mode,
                block_correct=self.block_correct,
                block_missed=self.block_missed,
            )
        )

    def _resolve_saved_pack_entries(self, selected_packs: list[dict]) -> list[dict]:
        current_pack_entries = []
        for pack_info in list_packs():
            try:
                pack = load_pack(pack_info["path"])
            except (FileNotFoundError, OSError, TypeError, ValueError):
                continue

            pack_id = self._pack_identifier(pack)
            current_pack_entries.append(
                {
                    "pack_id": pack_id,
                    "path": str(pack_info["path"]),
                    "pack": pack,
                }
            )

        available_packs_by_id = {
            entry["pack_id"]: entry for entry in current_pack_entries
        }

        resolved_entries = []
        for pack_info in selected_packs:
            if not isinstance(pack_info, dict):
                raise ValueError("selected_packs entries must be mappings")

            pack_id = pack_info.get("pack_id")
            if not isinstance(pack_id, str) or not pack_id.strip():
                raise ValueError("selected pack is missing a valid pack_id")

            entry = available_packs_by_id.get(pack_id)
            if entry is not None:
                resolved_entries.append(entry)
                continue

            stored_path = pack_info.get("path")
            if not isinstance(stored_path, str) or not stored_path.strip():
                raise ValueError(f"Pack {pack_id!r} could not be resolved")

            try:
                pack = load_pack(stored_path)
            except (FileNotFoundError, OSError, TypeError, ValueError) as error:
                raise ValueError(f"Pack {pack_id!r} could not be resolved") from error

            resolved_entries.append(
                {
                    "pack_id": pack_id,
                    "path": stored_path,
                    "pack": pack,
                }
            )

        return resolved_entries

    def _resume_saved_session(self) -> None:
        state = load_session()

        if state is None:
            self.show_home_screen()
            return

        try:
            session_state = state.get("session", state)
            selected_packs = session_state.get("selected_packs", [])
            resolved_pack_entries = self._resolve_saved_pack_entries(selected_packs)
            restored_state = self._restore_session_state(
                session_state,
                [entry["pack"] for entry in resolved_pack_entries],
            )
            ordered_questions = restored_state["ordered_questions"]
            current_question = restored_state["current_question"]
            review_questions = restored_state["review_questions"]
            missed_questions = restored_state["missed_questions"]
        except (KeyError, TypeError, ValueError, FileNotFoundError, OSError):
            delete_saved_session()
            self.show_home_screen()
            return

        selected_pack_payload = [
            {"pack_id": entry["pack_id"], "path": entry["path"]}
            for entry in resolved_pack_entries
        ]

        self.session_subject = {
            "display_name": session_state.get("subject_display_name", "Your Quiz"),
            "question_count": session_state.get("subject_question_count", 0),
            "pack_info": {
                "selected_packs": selected_pack_payload,
            },
        }
        self.session_pack_path = [entry["path"] for entry in selected_pack_payload]

        self.session = SessionManager(
            ordered_questions,
            block_size=restored_state.get("block_size", 15),
            shuffle=False,
        )
        self.session.current_index = restored_state.get("current_index", 0)

        self.review = ReviewQueue()
        self.review.questions = review_questions

        self.score = ScoreTracker()
        score_state = restored_state.get("score", {})
        self.score.first_attempt_correct = score_state.get(
            "first_attempt_correct",
            0,
        )
        self.score.first_attempt_missed = score_state.get(
            "first_attempt_missed",
            0,
        )
        self.score.review_corrected = score_state.get(
            "review_corrected",
            0,
        )
        self.score.completed = score_state.get("completed", 0)
        self.score.missed_questions = missed_questions

        self.review_mode = restored_state.get("review_mode", False)
        self.current_question = current_question
        self.answer_submitted = False
        self.block_correct = restored_state.get("block_correct", 0)
        self.block_missed = restored_state.get("block_missed", 0)

        self._show_question_screen()

    def _show_session_complete(self) -> None:
        delete_saved_session()
        container = self._replace_screen()
        summary = self.score.summary()

        total = summary["completed"]
        correct = summary["first_attempt_correct"]
        missed = summary["first_attempt_missed"]

        percentage = round((correct / total) * 100) if total else 0

        ttk.Label(
            container,
            text="Quiz Complete",
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(70, 18))

        ttk.Label(
            container,
            text=(
                f"First-pass score: {percentage}%\n"
                f"{correct} of {total} correct on the first attempt."
            ),
            style="Subtitle.TLabel",
            anchor="center",
            justify="center",
        ).pack(fill="x", pady=(0, 30))

        ttk.Button(
            container,
            text="Return Home",
            style="Primary.TButton",
            command=self.show_home_screen,
        ).pack()

    def _show_message_screen(
        self,
        title: str,
        message: str,
        button_text: str,
        command,
    ) -> None:
        container = self._replace_screen()

        ttk.Label(
            container,
            text=title,
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(80, 18))

        ttk.Label(
            container,
            text=message,
            style="Subtitle.TLabel",
            anchor="center",
            wraplength=700,
        ).pack(fill="x", pady=(0, 30))

        ttk.Button(
            container,
            text=button_text,
            style="Primary.TButton",
            command=command,
        ).pack()


def main() -> None:
    app = PrepFlowApp()
    app.mainloop()


if __name__ == "__main__":
    main()
