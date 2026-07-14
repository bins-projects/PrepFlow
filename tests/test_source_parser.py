from compiler.source_parser import parse_source_questions


def test_parse_single_multiple_choice_question() -> None:
    text = """Chapter 1: Nursing Theory

MULTIPLE CHOICE

1. Which theory should the nurse use to prioritize patient care?
a. Erikson's Psychosocial Theory
b. Paul's Critical-Thinking Theory
c. Maslow's Hierarchy of Needs
d. Rosenstock's Health Belief Model
ANS: C
Maslow's hierarchy helps prioritize physiological and psychological needs.
DIF: Remembering OBJ: 1.5 TOP: Planning
MSC: Management of Care
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1

    question = questions[0]

    assert question["chapter"] == "Chapter 1: Nursing Theory"
    assert question["section"] == "MULTIPLE CHOICE"
    assert question["source_question_number"] == 1
    assert question["question_type"] == "multiple_choice"
    assert question["stem"] == (
        "Which theory should the nurse use to prioritize patient care?"
    )
    assert question["choices"] == [
        {"label": "A", "text": "Erikson's Psychosocial Theory"},
        {"label": "B", "text": "Paul's Critical-Thinking Theory"},
        {"label": "C", "text": "Maslow's Hierarchy of Needs"},
        {"label": "D", "text": "Rosenstock's Health Belief Model"},
    ]
    assert question["correct_answers"] == ["C"]
    assert question["rationale"] == (
        "Maslow's hierarchy helps prioritize physiological and psychological needs."
    )


def test_parse_wrapped_question_stem() -> None:
    text = """Chapter 1: Nursing Theory

MULTIPLE CHOICE

4. The nursing instructor is researching the five proficiencies regarded as essential for students and
professionals. Which organization added safety as a sixth competency?
a. Quality and Safety Education for Nurses
b. Institute of Medicine
c. American Association of Colleges of Nursing
d. National League for Nursing
ANS: A
QSEN added safety as a sixth competency.
DIF: Remembering
"""

    questions = parse_source_questions(text)

    assert questions[0]["stem"] == (
        "The nursing instructor is researching the five proficiencies regarded as "
        "essential for students and professionals. Which organization added safety "
        "as a sixth competency?"
    )


def test_parse_wrapped_answer_choice() -> None:
    text = """Chapter 1: Nursing Theory

MULTIPLE CHOICE

2. Which definition of nursing is attributed to Florence Nightingale?
a. The imbalance between the patient and the environment decreases the capacity for
health.
b. The nurse focuses on interpersonal processes.
c. The nurse assists the patient toward independence.
d. Human beings interact as energy fields.
ANS: A
Nightingale emphasized the relationship between health and environment.
DIF: Remembering
"""

    questions = parse_source_questions(text)

    assert questions[0]["choices"][0] == {
        "label": "A",
        "text": (
            "The imbalance between the patient and the environment decreases "
            "the capacity for health."
        ),
    }

from pathlib import Path


def test_parse_real_fundamentals_sample() -> None:
    sample_path = Path(
        "output/imports/fundamentals/02_clean.txt"
    )

    if not sample_path.exists():
        import pytest

        pytest.skip(
            "Private generated Fundamentals fixture is not available."
        )

    sample = sample_path.read_text(encoding="utf-8")
    questions = parse_source_questions(sample)

    assert len(questions) > 1000


def test_source_metadata_does_not_append_to_last_choice() -> None:
    text = """Chapter 1: Nursing Theory

MULTIPLE CHOICE

1. Which theory should guide priority care?
a. Erikson
b. Paul
c. Maslow
d. Rosenstock
ANS: C
Maslow helps prioritize patient needs.
DIF: Remembering OBJ: 1.5 TOP: Planning
MSC: NCLEX Client Needs Category: Safe and Effective Care Environment
Concepts: Care Coordination
"""

    questions = parse_source_questions(text)

    assert questions[0]["choices"][-1] == {
        "label": "D",
        "text": "Rosenstock",
    }


def test_parse_rationale_that_appears_after_metadata() -> None:
    text = """Chapter 15: Nursing Informatics

MULTIPLE CHOICE

11. Which informatics competency level describes this nurse?
a. Beginner
b. Experienced
c. Specialist
d. Innovator
ANS: B
NOT: Concepts: Technology and Informatics
U S N T O
Experienced nurses understand data relationships and identify trends.
DIF: Analyzing OBJ: 15.4 TOP: Evaluation
"""

    questions = parse_source_questions(text)

    assert questions[0]["rationale"] == (
        "Experienced nurses understand data relationships and identify trends."
    )


def test_inline_metadata_does_not_append_to_stem() -> None:
    text = """Chapter 26: Infection Prevention

MULTIPLE CHOICE

1. Which isolation precaution should the nurse implement for hepatitis A? DIF: Applying
a. Airborne
b. Droplet
c. Contact
d. Protective
ANS: C
Contact precautions are appropriate.
"""

    questions = parse_source_questions(text)

    assert questions[0]["stem"] == (
        "Which isolation precaution should the nurse implement for hepatitis A?"
    )


def test_inline_metadata_does_not_append_to_rationale() -> None:
    text = """Chapter 6: Nursing Process

MULTIPLE CHOICE

1. Which patient should receive priority care?
a. A patient with cold symptoms
b. A patient with a twisted ankle
c. A patient with an obstructed airway
d. A patient requesting discharge teaching
ANS: C
An obstructed airway is an immediate threat. Analyzing OBJ: 6.3 TOP: Assessment
"""

    questions = parse_source_questions(text)

    assert questions[0]["rationale"] == (
        "An obstructed airway is an immediate threat."
    )


def test_parse_completion_with_answer_on_following_line() -> None:
    text = """Chapter 1: Dosage Calculations

COMPLETION

1. What is the weight in pounds for an individual who weighs 70 kg? lb
ANS:
154
One kilogram equals 2.2 pounds.
DIF: Understanding
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["question_type"] == "completion"
    assert questions[0]["choices"] == []
    assert questions[0]["correct_answers"] == ["154"]
    assert questions[0]["rationale"] == (
        "One kilogram equals 2.2 pounds."
    )


def test_parse_split_choice_marker() -> None:
    text = """Chapter 1: Test

MULTIPLE CHOICE

1. What is another term for seizure disorder?
a
.
Epilepsy
b
.
Enkephalin
c
.
Narcolepsy
d
.
Neuropathy
ANS: A
A seizure disorder is also called epilepsy.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert len(questions[0]["choices"]) == 4
    assert questions[0]["choices"][0]["label"] == "A"
    assert questions[0]["choices"][0]["text"] == "Epilepsy"


def test_recovers_missing_a_choice_when_answer_key_confirms_it() -> None:
    text = """Chapter 25: Drug Therapy for Seizures

MULTIPLE CHOICE

2. What is another term for seizure disorder?
Epilepsy
b. Enkephalin
c. Narcolepsy
d. Neuropathy
ANS: A
A seizure disorder is sometimes called epilepsy.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["stem"] == "What is another term for seizure disorder?"
    assert questions[0]["choices"][0]["label"] == "A"
    assert questions[0]["choices"][0]["text"] == "Epilepsy"


def test_wrapped_stem_line_beginning_with_time_is_not_new_question():
    text = """
Chapter 50: Diabetes and Hypoglycemia
MULTIPLE CHOICE
16. A patient with type 1 diabetes has an insulin order for NPH insulin, 35 U, to be given at
0700. The patient has also been instructed not to take anything by mouth.
a. Give the insulin as ordered.
b. Give the insulin with a small snack.
c. Inform the charge nurse.
d. Hold the insulin until after the blood draw.
ANS: D
Holding the insulin is appropriate.
DIF: Cognitive Level: Application
17. What should the nurse assess next?
a. Temperature
b. Blood pressure
c. Blood glucose
d. Respiratory rate
ANS: C
The blood glucose should be assessed.
DIF: Cognitive Level: Application
"""

    questions = parse_source_questions(text)

    assert len(questions) == 2
    assert questions[0]["source_question_number"] == 16
    assert "0700. The patient" in questions[0]["stem"]
    assert len(questions[0]["choices"]) == 4
    assert questions[0]["correct_answers"] == ["D"]


def test_rationale_beginning_with_choice_like_prefix_stays_rationale():
    text = """
Chapter 57: Skin Disorders
MULTIPLE CHOICE
7. Where should the nurse assess for Candida albicans?
a. Scalp
b. Abdominal skinfolds
c. Shaft of the penis
d. Sacrum
ANS: B
C. albicans infection appears most often in skinfolds.
DIF: Cognitive Level: Comprehension
8. What should the nurse assess next?
a. Temperature
b. Blood pressure
c. Skin color
d. Respirations
ANS: C
Skin color should be assessed.
DIF: Cognitive Level: Comprehension
"""

    questions = parse_source_questions(text)

    assert len(questions) == 2
    assert len(questions[0]["choices"]) == 4
    assert questions[0]["rationale"] == (
        "C. albicans infection appears most often in skinfolds."
    )


def test_completion_sequence_question_is_classified_as_ordered_response():
    text = """
Chapter 1: Nursing Practice
COMPLETION
9. Place the corresponding letter to each stage in the correct order. _________
(Place the events in the appropriate sequence. Do not separate answers with punctuation.)
a. Outcomes
b. Conceptualization
c. Frustration
d. Action
ANS:
CBDA
The correct sequence is frustration, conceptualization, action, and outcomes.
DIF: Cognitive Level: Application
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["question_type"] == "ordered_response"
    assert questions[0]["correct_answers"] == ["C", "B", "D", "A"]
    assert len(questions[0]["choices"]) == 4


def test_source_parser_accepts_choice_g():
    text = """
Chapter 1: Nursing Practice
COMPLETION
10. Place the steps in the appropriate sequence. _________
a. Negotiate a plan.
b. Clarify values.
c. Ask if it is an ethical dilemma.
d. Verbalize the problem.
e. Gather information.
f. Identify possible courses of action.
g. Evaluate the plan over time.
ANS: CEBDFAG
The steps should be completed in the listed sequence.
DIF: Cognitive Level: Application
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert len(questions[0]["choices"]) == 7
    assert questions[0]["choices"][-1] == {
        "label": "G",
        "text": "Evaluate the plan over time.",
    }


def test_parser_joins_wrapped_chapter_heading():
    text = """
Chapter 03: Medical-Surgical Patients: Individuals, Families, and
Communities Linton: Medical-Surgical Nursing, 8th Edition
MULTIPLE CHOICE
1. What should the nurse include in the care plan?
a. The patient’s preferences
b. The nurse’s preferences
c. Only hospital policy
d. Only the family’s preferences
ANS: A
The patient’s preferences should be included.
DIF: Cognitive Level: Application
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["chapter"] == (
        "Chapter 03: Medical-Surgical Patients: Individuals, Families, "
        "and Communities Linton: Medical-Surgical Nursing, 8th Edition"
    )


def test_multiline_source_header_does_not_attach_to_previous_question():
    text = """
Chapter 31: Hematologic Disorders
COMPLETION
2. Cells capable of developing into RBCs are called ______ cells.
ANS:
stem
Adult stem cells can develop into several blood cell types.
DIF: Cognitive Level: Comprehension
Chapter 32: Immunologic Disorders
Linton: Medical-Surgical Nursing, 8th
Edition
MULTIPLE CHOICE
1. Which population has the greatest incidence?
a. Group A
b. Group B
c. Group C
d. Group D
ANS: B
Group B has the greatest incidence.
DIF: Cognitive Level: Knowledge
"""

    questions = parse_source_questions(text)

    assert len(questions) == 2
    assert questions[0]["rationale"] == (
        "Adult stem cells can develop into several blood cell types."
    )
    assert questions[1]["chapter"] == "Chapter 32: Immunologic Disorders"


def test_parser_preserves_real_wrapped_chapter_title_but_removes_source_header():
    text = """
Chapter 33: Cardiovascular System
Introduction Linton: Medical-Surgical Nursing,
8th Edition
MULTIPLE CHOICE
1. What should the nurse assess?
a. Pulse
b. Temperature
c. Weight
d. Height
ANS: A
The pulse should be assessed.
DIF: Cognitive Level: Knowledge
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["chapter"] == (
        "Chapter 33: Cardiovascular System Introduction"
    )

def test_parser_normalizes_ans_greater_than_marker() -> None:
    text = """
Chapter 3: Mathematics Review
MULTIPLE CHOICE
1. What is the safest calculation practice?
A.
Estimate the dose.
B.
Ensure the numbers are entered correctly. Ans> B
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["choices"] == [
        {"label": "A", "text": "Estimate the dose."},
        {
            "label": "B",
            "text": "Ensure the numbers are entered correctly.",
        },
    ]
    assert questions[0]["correct_answers"] == ["B"]


def test_parser_normalizes_inline_dash_answer_marker() -> None:
    text = """
Chapter 28: Drug Therapy For Male Reproductive Problems
MULTIPLE CHOICE
1. Which finding is most important?
A. Mild fatigue
B. Occasional thirst
C. Dry skin
D. Strength of the urinary stream. - ANS: D
The urinary stream helps assess obstruction severity.
DIF: Cognitive Level: Applying
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["choices"][-1] == {
        "label": "D",
        "text": "Strength of the urinary stream.",
    }
    assert questions[0]["correct_answers"] == ["D"]
    assert questions[0]["rationale"] == (
        "The urinary stream helps assess obstruction severity."
    )

def test_parser_handles_unnumbered_ans_greater_than_question() -> None:
    text = """
Chapter 3: Mathematics Review and Introduction to Dosage Calculations
What Is The Most Important Consideration When Using A Calculator?
A.
Always estimate the answer.
B.
Ensure the numbers are entered in the correct order. Ans> B
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["stem"] == (
        "What Is The Most Important Consideration When Using A Calculator?"
    )
    assert questions[0]["correct_answers"] == ["B"]


def test_parser_handles_unnumbered_inline_dash_answer_question() -> None:
    text = """
Chapter 28: Drug Therapy For Male Reproductive Problems
To Determine The Severity Of Symptoms For A Patient With BPH, What Should The Nurse Ask?
A. Blood in the urine.
B. Lower back pain.
C. Erectile dysfunction.
D. Strength of the urinary stream. - ANS: D
The urinary stream helps determine obstruction severity.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["correct_answers"] == ["D"]
    assert questions[0]["choices"][-1] == {
        "label": "D",
        "text": "Strength of the urinary stream.",
    }

def test_parser_handles_multiple_wrapped_unnumbered_questions() -> None:
    text = """
Chapter 28: Drug Therapy For Male Reproductive Problems
What finding helps determine the severity of benign prostatic
hyperplasia in an older adult?
A. Blood in the urine
B. Lower back pain
C. Erectile dysfunction
D. Strength of the urinary stream Ans> D
The urinary stream helps determine obstruction severity.
A patient taking finasteride asks about expected adverse
effects. Which response is correct?
A. Severe hypertension
B. Decreased libido
C. Immediate symptom relief
D. Increased fertility Ans> B
Decreased libido can occur with androgen suppression.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 2
    assert questions[0]["correct_answers"] == ["D"]
    assert questions[1]["correct_answers"] == ["B"]
    assert questions[1]["stem"] == (
        "A patient taking finasteride asks about expected adverse "
        "effects. Which response is correct?"
    )

def test_parser_classifies_unheaded_blank_as_completion() -> None:
    text = """
Chapter 3: Mathematics Review and Introduction to Dosage Calculations
A patient is prescribed aspirin 650 mg. Tablets contain 325 mg.
How many tablets should be administered?
_____ tablet(s) Ans> 2
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["question_type"] == "completion"
    assert questions[0]["choices"] == []
    assert questions[0]["correct_answers"] == ["2"]

def test_parser_normalizes_choices_answer_and_rationale_labels() -> None:
    text = """
Chapter 11: Immunizations
MULTIPLE CHOICE
1. What type of immunity is learned?
Choices:
A) Innate immunity
B) Acquired immunity
C) Passive immunity
D) Artificial immunity
Answer: B) Acquired immunity
Rationale: Acquired immunity develops after exposure.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["question_type"] == "multiple_choice"
    assert questions[0]["choices"] == [
        {"label": "A", "text": "Innate immunity"},
        {"label": "B", "text": "Acquired immunity"},
        {"label": "C", "text": "Passive immunity"},
        {"label": "D", "text": "Artificial immunity"},
    ]
    assert questions[0]["correct_answers"] == ["B"]
    assert (
        questions[0]["rationale"]
        == "Acquired immunity develops after exposure."
    )


def test_parser_classifies_numeric_no_choice_answer_as_completion() -> None:
    text = """
Chapter 29: Reproductive Problems
1. The prescribed dose is 2.5 mg and tablets contain 0.625 mg.
How many tablets should be administered? - ANS: 4
Want 2.5 mg and have 0.625 mg per tablet.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["question_type"] == "completion"
    assert questions[0]["choices"] == []
    assert questions[0]["correct_answers"] == ["4"]
    assert "0.625 mg per tablet" in questions[0]["rationale"]

def test_labeled_format_preserves_multiple_question_boundaries() -> None:
    text = """
Chapter 11: Immunizations
MULTIPLE CHOICE
1. First question?
Choices:
A) First choice
B) Second choice
Answer: B) Second choice
Rationale: First rationale.
2. Second question?
Choices:
A) Third choice
B) Fourth choice
Answer: A) Third choice
Rationale: Second rationale.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 2
    assert questions[0]["source_question_number"] == 1
    assert questions[0]["correct_answers"] == ["B"]
    assert questions[0]["rationale"] == "First rationale."
    assert questions[1]["source_question_number"] == 2
    assert questions[1]["correct_answers"] == ["A"]
    assert questions[1]["rationale"] == "Second rationale."


def test_parser_normalizes_correct_answer_and_explanation() -> None:
    text = """
Chapter 26: Insomnia
1. Which drug can cause amnesia?
A. Drug one
B. Drug two
C. Temazepam
D. Drug four
Correct Answer: C. Temazepam
Explanation: Temazepam can impair memory.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["correct_answers"] == ["C"]
    assert questions[0]["rationale"] == "Temazepam can impair memory."


def test_parser_normalizes_answer_and_feedback() -> None:
    text = """
Chapter 27: Eye Problems
1. Which statement is correct?
A. First statement
B. Second statement
C. Both eyes are usually affected
D. Fourth statement
Answer: C. Both eyes are usually affected
Feedback: This disorder commonly affects both eyes.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["correct_answers"] == ["C"]
    assert (
        questions[0]["rationale"]
        == "This disorder commonly affects both eyes."
    )

def test_parser_normalizes_plain_inline_ans_marker() -> None:
    text = """
Chapter 10: Antiinflammatory Drugs
MULTIPLE CHOICE
1. Which substance is inhibited?
A. Tumor necrosis factor
B. White blood cells
C. Cyclo-oxygenase
D. Interferon
Instructor note about this topic ANS: A
The drug inhibits tumor necrosis factor.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["correct_answers"] == ["A"]
    assert (
        questions[0]["rationale"]
        == "The drug inhibits tumor necrosis factor."
    )


def test_parser_normalizes_multiline_ordered_answer_key() -> None:
    text = """
Chapter 21: Diabetes
ORDERING
1. Place the steps in the correct order.
A. First option
B. Second option
C. Third option
D. Fourth option
ANS:
1. D
2. C
3. A
4. B
The steps must be completed in the listed sequence.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["question_type"] == "ordered_response"
    assert questions[0]["correct_answers"] == ["D", "C", "A", "B"]
    assert (
        questions[0]["rationale"]
        == "The steps must be completed in the listed sequence."
    )

def test_unnumbered_question_does_not_absorb_previous_rationale() -> None:
    text = """
Chapter 28: Male Reproductive Problems
A previous question?
A. First
B. Second
C. Third
D. Fourth - ANS: C
Previous rationale ends here.
A couple is seen because they have not conceived.
When performing an examination, what should the nurse assess?
A. Hydrocele
B. Varicocele
C. Epididymitis
D. Paraphimosis - ANS: B
Persistent varicoceles are associated with infertility.
Which information should the nurse include in teaching?
A. Perform the examination in a warm area
B. Only the testis is normally palpable
C. Perform it weekly
D. Both testes must be equal in size - ANS: A
The testes hang lower when warm.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 3

    assert questions[1]["stem"] == (
        "A couple is seen because they have not conceived. "
        "When performing an examination, what should the nurse assess?"
    )
    assert questions[1]["correct_answers"] == ["B"]
    assert questions[1]["rationale"] == (
        "Persistent varicoceles are associated with infertility."
    )

    assert questions[2]["stem"] == (
        "Which information should the nurse include in teaching?"
    )
    assert questions[2]["correct_answers"] == ["A"]

def test_parser_repairs_split_choice_marker_with_text_after_period() -> None:
    text = """Chapter 9: Antiviral Drugs
MULTIPLE CHOICE
2. Why does immunity develop?
A. First answer.
B
. Second answer.
C. Third answer.
D
. Fourth answer.
ANS: D
The immune system develops protection.
"""

    questions = parse_source_questions(text)

    assert questions[0]["choices"] == [
        {"label": "A", "text": "First answer."},
        {"label": "B", "text": "Second answer."},
        {"label": "C", "text": "Third answer."},
        {"label": "D", "text": "Fourth answer."},
    ]

def test_parser_repairs_sequential_choice_labels_without_periods() -> None:
    text = """Chapter 1: Drug Basics
MULTIPLE CHOICE
2. Which term describes the intended effect?
A. Side effect
B Intended action
C. Adverse reaction
D Idiosyncratic response
ANS: B
The intended action is the desired therapeutic effect.
"""

    questions = parse_source_questions(text)

    assert questions[0]["choices"] == [
        {"label": "A", "text": "Side effect"},
        {"label": "B", "text": "Intended action"},
        {"label": "C", "text": "Adverse reaction"},
        {"label": "D", "text": "Idiosyncratic response"},
    ]

def test_parser_repairs_missing_period_choice_after_wrapped_choice() -> None:
    text = """Chapter 1: Drug Basics
MULTIPLE CHOICE
20. What is the best response?
A. Ask the patient to describe the reaction she had
to this drug.
B Ask whether the drug was taken by mouth or injection.
C. Contact the health care provider to request
another prescription.
D Tell the patient an antidote will prevent the reaction.
ANS: A
Clarifying the previous reaction is the priority.
"""

    questions = parse_source_questions(text)

    assert questions[0]["choices"] == [
        {
            "label": "A",
            "text": "Ask the patient to describe the reaction she had to this drug.",
        },
        {
            "label": "B",
            "text": "Ask whether the drug was taken by mouth or injection.",
        },
        {
            "label": "C",
            "text": "Contact the health care provider to request another prescription.",
        },
        {
            "label": "D",
            "text": "Tell the patient an antidote will prevent the reaction.",
        },
    ]

def test_parser_starts_new_question_after_rationale_with_inline_metadata() -> None:
    text = """Chapter 23: Drug Therapy for Seizures
MULTIPLE CHOICE
2. What is another term for seizure disorder?
B. Enkephalin
C. Narcolepsy
D. Neuropathy
ANS: A
An individual with repeated seizures has a seizure disorder, sometimes called epilepsy. DIF: Cognitive Level: Remembering REF: P. 401
3. Which health problem is the most serious possible side effect for status epilepticus?
A. Ruptured spinal disks
B. Brain tumor
C. Broken bones
D. Brain damage
ANS: D
Status epilepticus can cause brain damage.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 2

    assert questions[0]["source_question_number"] == 2
    assert questions[0]["correct_answers"] == ["A"]
    assert questions[0]["rationale"] == (
        "An individual with repeated seizures has a seizure disorder, "
        "sometimes called epilepsy."
    )

    assert questions[1]["source_question_number"] == 3
    assert questions[1]["correct_answers"] == ["D"]
    assert questions[1]["rationale"] == (
        "Status epilepticus can cause brain damage."
    )
