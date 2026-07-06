import re


def split_choice_text(choices):
    if isinstance(choices, list):
        return choices

    if isinstance(choices, dict):
        combined = " ".join(f"{k}. {v}" for k, v in choices.items())

        matches = re.findall(
            r"([a-zA-Z])\s*[.)]\s*(.*?)(?=\s+[a-zA-Z]\s*[.)]\s*|$)",
            combined,
        )

        return [
            {"label": label.upper(), "text": text.strip()}
            for label, text in matches
        ]

    return []


def format_choices(choices):
    normalized_choices = split_choice_text(choices)
    lines = []

    for choice in normalized_choices:
        label = choice["label"]
        text = choice["text"]
        lines.append(f"{label}. {text}")

    return "\n".join(lines)


def normalize_answer(answer):
    return answer.strip().upper().replace(",", "").replace(" ", "")


def get_prompt(question):
    return question.get("prompt") or question.get("stem")


def get_correct_answers(question):
    answer = question.get("correct_answer") or question.get("correct_answers")

    if isinstance(answer, list):
        return [str(a).upper() for a in answer]

    return list(str(answer).upper())


def check_answer(user_answer, correct_answers):
    user_answer = normalize_answer(user_answer)
    correct_set = set(correct_answers)
    user_set = set(user_answer)

    return user_set == correct_set


def ask_question(question, header=None):
    print()

    if header:
        print(header)
    else:
        print(f"Question {question['question_number']}")

    print()
    print(get_prompt(question))
    print()
    print(format_choices(question["choices"]))
    print()

    answer = input("Your answer: ")
    correct_answers = get_correct_answers(question)
    is_correct = check_answer(answer, correct_answers)

    print()
    if is_correct:
        print("Correct!")
    else:
        correct = ", ".join(correct_answers)
        print("Incorrect.")
        print(f"Correct answer: {correct}")

    print()
    print("Rationale:")
    print(question["rationale"])

    return is_correct
