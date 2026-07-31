from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def completed_first_pass_step(missed_count: int, has_more: bool) -> str:
    if max(0, missed_count) > 0:
        return "review"
    return "next-block" if has_more else "final-summary"


def completed_review_step(has_more: bool) -> str:
    return "next-block" if has_more else "final-summary"


@dataclass
class QuizLifecycle:
    total_questions: int
    block_size: int
    block_start: int = 0
    question_index: int = 0
    first_pass_correct: int = 0
    first_pass_missed: int = 0
    block_correct: int = 0
    block_missed: list[int] = field(default_factory=list)
    review_queue: list[int] = field(default_factory=list)
    current_review: int | None = None
    review_mode: bool = False
    screen: str = "question"
    mobile_portrait: bool = True
    advanced_boundary: int | None = None

    @property
    def block_end(self) -> int:
        return min(self.block_start + self.block_size, self.total_questions)

    def answer(self, correct: bool) -> None:
        if self.review_mode:
            if not correct and self.current_review is not None:
                self.review_queue.append(self.current_review)
            return

        if correct:
            self.first_pass_correct += 1
            self.block_correct += 1
        else:
            self.first_pass_missed += 1
            self.block_missed.append(self.question_index)

    def continue_from_feedback(self) -> None:
        if self.review_mode:
            if self.review_queue:
                self.current_review = self.review_queue.pop(0)
                self.screen = "question"
                return
            self.review_mode = False
            self.current_review = None
            self.screen = completed_review_step(self.block_end < self.total_questions)
            if self.screen == "next-block" and self.mobile_portrait:
                self.screen = "block-progress"
            return

        self.question_index += 1
        if self.question_index < self.block_end:
            self.screen = "question"
            return

        step = completed_first_pass_step(
            len(self.block_missed), self.block_end < self.total_questions
        )
        if step == "review":
            self.review_mode = True
            self.review_queue = list(self.block_missed)
            self.current_review = self.review_queue.pop(0)
            self.screen = "question"
            return
        self.screen = step
        if self.screen == "next-block" and self.mobile_portrait:
            self.screen = "block-progress"

    def start_next_block(self, completed_block_end: int | None = None) -> None:
        boundary = self.block_end if completed_block_end is None else completed_block_end
        if boundary != self.block_end or self.block_start >= boundary:
            return
        self.advanced_boundary = boundary
        self.block_start = boundary
        self.question_index = self.block_start
        self.block_correct = 0
        self.block_missed = []
        self.screen = "question"

    def normalize_mobile_boundary(self, saved_screen: str, saved_block_end: int) -> None:
        if saved_screen == "block-progress":
            self.screen = "block-progress"
            return
        if saved_screen == "block-summary" and self.block_missed:
            self.review_mode = True
            self.review_queue = list(self.block_missed)
            self.current_review = self.review_queue.pop(0)
            self.screen = "question"
            return
        self.start_next_block(saved_block_end)

    def block_progress_statistics(self) -> dict[str, int]:
        block_length = self.block_end - self.block_start
        return {
            "block_correct": self.block_correct,
            "block_total": block_length,
            "cumulative_correct": self.first_pass_correct,
            "cumulative_total": self.block_end,
            "missed_mastered": len(self.block_missed),
            "overall_completed": self.block_end,
            "overall_total": self.total_questions,
            "next_block_total": min(
                self.block_end + self.block_size, self.total_questions
            ) - self.block_end,
        }


def test_one_question_incorrect_enters_review() -> None:
    quiz = QuizLifecycle(1, 1)
    quiz.answer(False)
    quiz.continue_from_feedback()
    assert (quiz.review_mode, quiz.current_review, quiz.screen) == (True, 0, "question")


def test_review_miss_remains_queued() -> None:
    quiz = QuizLifecycle(1, 1, review_mode=True, current_review=0)
    quiz.answer(False)
    assert quiz.review_queue == [0]


def test_review_mastery_leaves_queue() -> None:
    quiz = QuizLifecycle(1, 1, review_mode=True, current_review=0)
    quiz.answer(True)
    quiz.continue_from_feedback()
    assert (quiz.review_queue, quiz.review_mode, quiz.screen) == ([], False, "final-summary")


def test_one_question_correct_reaches_final_summary() -> None:
    quiz = QuizLifecycle(1, 1)
    quiz.answer(True)
    quiz.continue_from_feedback()
    assert quiz.screen == "final-summary"


def test_block_size_one_opens_progress_then_next_first_pass_question() -> None:
    quiz = QuizLifecycle(4, 1)
    quiz.answer(True)
    quiz.continue_from_feedback()
    assert (quiz.question_index, quiz.screen) == (1, "block-progress")
    quiz.start_next_block(1)
    assert (quiz.question_index, quiz.screen) == (1, "question")


def test_block_size_two_advances_without_skipping() -> None:
    quiz = QuizLifecycle(4, 2)
    quiz.answer(True)
    quiz.continue_from_feedback()
    assert quiz.question_index == 1
    quiz.answer(True)
    quiz.continue_from_feedback()
    assert quiz.screen == "block-progress"
    quiz.start_next_block(2)
    assert quiz.question_index == 2


def test_review_attempts_preserve_first_pass_score() -> None:
    quiz = QuizLifecycle(1, 1)
    quiz.answer(False)
    quiz.continue_from_feedback()
    quiz.answer(False)
    quiz.continue_from_feedback()
    quiz.answer(True)
    assert (quiz.first_pass_correct, quiz.first_pass_missed) == (0, 1)


def test_resume_pending_block_completion_has_forward_route() -> None:
    quiz = QuizLifecycle(4, 1, block_start=0, question_index=1, screen="block-progress")
    quiz.normalize_mobile_boundary("block-progress", 1)
    assert (quiz.block_start, quiz.question_index, quiz.screen) == (0, 1, "block-progress")


def test_resume_post_grade_feedback_consumes_transition_once() -> None:
    quiz = QuizLifecycle(1, 1, first_pass_correct=1, question_index=0, screen="feedback")
    quiz.continue_from_feedback()
    assert (quiz.question_index, quiz.screen) == (1, "final-summary")


def test_legacy_question_snapshot_at_block_boundary_resolves_forward() -> None:
    quiz = QuizLifecycle(4, 1, block_start=0, question_index=1, screen="question")
    quiz.normalize_mobile_boundary("mastered-summary", 1)
    assert (quiz.block_start, quiz.question_index, quiz.screen) == (1, 1, "question")


def test_drug_library_round_trip_does_not_change_pending_state() -> None:
    quiz = QuizLifecycle(4, 1, question_index=1, screen="block-progress")
    quiz.normalize_mobile_boundary("block-progress", 1)
    assert (quiz.block_start, quiz.question_index, quiz.screen) == (0, 1, "block-progress")


def test_review_mastery_opens_progress_before_next_block() -> None:
    quiz = QuizLifecycle(4, 1)
    quiz.answer(False)
    quiz.continue_from_feedback()
    quiz.answer(True)
    quiz.continue_from_feedback()
    assert (quiz.block_start, quiz.question_index, quiz.screen) == (0, 1, "block-progress")
    quiz.start_next_block(1)
    assert (quiz.block_start, quiz.question_index, quiz.screen) == (1, 1, "question")


def test_repeated_boundary_normalization_is_idempotent() -> None:
    quiz = QuizLifecycle(4, 1, question_index=1, screen="next-block")
    quiz.normalize_mobile_boundary("mastered-summary", 1)
    score = (quiz.first_pass_correct, quiz.first_pass_missed)
    quiz.normalize_mobile_boundary("mastered-summary", 1)
    assert (quiz.block_start, quiz.question_index) == (1, 1)
    assert (quiz.first_pass_correct, quiz.first_pass_missed) == score


def test_repeated_progress_continue_does_not_skip_question() -> None:
    quiz = QuizLifecycle(4, 1, question_index=1, screen="block-progress")
    quiz.start_next_block(1)
    quiz.start_next_block(1)
    assert (quiz.block_start, quiz.question_index) == (1, 1)


def test_block_size_one_progress_statistics() -> None:
    quiz = QuizLifecycle(4, 1, question_index=1, first_pass_correct=1, block_correct=1)
    assert quiz.block_progress_statistics() == {
        "block_correct": 1,
        "block_total": 1,
        "cumulative_correct": 1,
        "cumulative_total": 1,
        "missed_mastered": 0,
        "overall_completed": 1,
        "overall_total": 4,
        "next_block_total": 1,
    }


def test_block_size_two_progress_statistics_preserve_first_pass_score() -> None:
    quiz = QuizLifecycle(
        4, 2, question_index=2, first_pass_correct=1, first_pass_missed=1,
        block_correct=1, block_missed=[1]
    )
    stats = quiz.block_progress_statistics()
    assert (stats["block_correct"], stats["block_total"]) == (1, 2)
    assert (stats["cumulative_correct"], stats["cumulative_total"]) == (1, 2)
    assert stats["missed_mastered"] == 1


def test_short_final_block_uses_actual_question_count() -> None:
    quiz = QuizLifecycle(3, 2, block_start=2, question_index=3, block_correct=1)
    assert quiz.block_progress_statistics()["block_total"] == 1


def test_final_summary_waits_for_first_pass_and_review_completion() -> None:
    quiz = QuizLifecycle(1, 1)
    quiz.answer(False)
    quiz.continue_from_feedback()
    assert quiz.screen != "final-summary"
    quiz.answer(True)
    quiz.continue_from_feedback()
    assert quiz.screen == "final-summary"


def test_browser_uses_the_tested_lifecycle_contract() -> None:
    navigation = (ROOT / "web/navigation-rules.js").read_text()
    app = (ROOT / "web/app.js").read_text()
    assert 'return "review";' in navigation
    assert 'return hasMoreQuestions ? "next-block" : "final-summary";' in navigation
    assert "completeFirstPassBlock();" in app
    assert "completeMasteredBlock();" in app
    assert 'saveSession("feedback");' in app
    assert 'saved.screen === "feedback"' in app
    assert "questionIndex >= blockEnd" in app
    assert "usesMobilePortraitPresentation()" in app
    assert "advanceToNextBlock(saved.blockEnd);" in app
    assert 'saveSession("block-progress");' in app
    assert 'saved.screen === "block-progress"' in app
