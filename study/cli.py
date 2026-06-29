from study.loader import load_questions
from study.question import ask_question
from study.session import SessionManager
from study.scoring import ScoreTracker


def main():
    questions = load_questions()
    session = SessionManager(questions)
    score = ScoreTracker()

    print(f"Loaded {len(questions)} questions.\n")

    while session.has_next_question():
        question = session.get_next_question()
        is_correct = ask_question(question)
        score.record_answer(question, is_correct)

        input("\nPress Enter for next question...")


if __name__ == "__main__":
    main()