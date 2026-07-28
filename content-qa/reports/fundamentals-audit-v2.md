# Fundamentals Pack QA Audit

> Read-only scan. The original Pack was not modified.

## Summary

- Pack: `packs/fundamentals.prepflow.json`
- Questions scanned: **1040**
- Text fields scanned: **15577**
- Questions with findings: **219**
- Total findings: **268**

### Findings by severity

- high: 105
- medium: 163

### Findings by category

- Contamination: 43
- Structure: 9
- Text: 216

### Findings by rule

- multiple spaces: 70
- possible broken web text: 53
- space before punctuation: 51
- edition metadata: 41
- possible split suffix: 25
- detached taxonomy word: 10
- duplicate correct answers: 8
- space inside parentheses: 6
- NURSINGTB contamination: 2
- correct answer not found in choices: 1
- repeated word: 1

## Detailed findings

### 1. PFQ-fundamentals-000000001 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 1
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[0].rationale`
- Detail: Pattern requires human review against the original source.

```text
Maslow‘s hierarchy of needs specifies the psychological and physiologic factors that affect each person‘s physical and mental health. The nurse‘s understanding of these factors helps with formulating Nursing diagnoses that address the patient‘s needs and values to prioritize car…
```

### 2. PFQ-fundamentals-000000004 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 4
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[3].rationale`
- Detail: Pattern requires human review against the original source.

```text
The Institute of Medicine r e pNo r t ,RH eIa l thGP r oBf e.s sCi o nMs Education: A Bridge to Quality (2003),outlines five core competencies. These include patient-centered care, interdisciplinary teamwork, use of evidence-based medicine, quality improvement, and use of inform…
```

### 3. PFQ-fundamentals-000000011 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 11
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[10].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Expect that the patient may return to the hospital if the discharge process is poorly done. NUR ISG BN.CTM O
```

### 4. PFQ-fundamentals-000000024 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 24
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[23].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["A", "B", "C", "D", "B", "C"]
```

### 5. PFQ-fundamentals-000000025 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 25
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[24].rationale`
- Detail: Known source or extraction contamination detected.

```text
The process of using evidence-based practice (EBP) starts with the identification of a problem. The nurse then conducts a literature search to find the best evidence pertaining to the problem. Facility resources may impact the ability to implement the chosen decision. Patient pr…
```

### 6. PFQ-fundamentals-000000038 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 38
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[37].rationale`
- Detail: Pattern requires human review against the original source.

```text
Values clarification is a process used to help people reflect on, clarify, and prioritize personal values to increase self-awareness or to make decisions. Nurses can use values clari fication to help patients identify the nature of a conflict and reach a decision based on their …
```

### 7. PFQ-fundamentals-000000044 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 44
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[43].rationale`
- Detail: Pattern requires human review against the original source.

```text
Swanson‘s Theory of Caring is composed of five interrelated caring processes: having faith in the ability of others to have meaningful lives; striving to understand the meaning of events in other‘s lives; being emotionally present to the other person; doing for others what the y…
```

### 8. PFQ-fundamentals-000000046 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 46
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[45].rationale`
- Detail: Pattern requires human review against the original source.

```text
First-order beliefs serve as the foundation or the basis of an individual‘s belief system. People begin developing first-order beliefs about what is correct, real, and true in early childhood directly through experiences NandRUindIiSrecGtNl y fBr o.mCi n fMo rm a t i o n shared …
```

### 9. PFQ-fundamentals-000000048 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 48
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[47].stem`
- Detail: Pattern requires human review against the original source.

```text
Caring, according to the American Nurses Association (ANA) Code of Ethics (2 015), is having concern or regard for that which affects the welfare of another. The nurse recognizes that as a profession, nursing can trace its earliest beginnings to what types of nurturing activitie…
```

### 10. PFQ-fundamentals-000000050 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 50
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[49].rationale`
- Detail: Known source or extraction contamination detected.

```text
Compassion fatigue is an extreme state of distress experienced as the progressive and cumulative result of exposure to stress in the therapeutic use of self in caring for others. Compassion fatigue involves the nurse experiencing a feeling of being unable to meet the needs of pa…
```

### 11. PFQ-fundamentals-000000061 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 61
- Chapter: Communication
- JSON path: `$.questions[60].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Therapeutic touch, such as holding the patient‘s hand or touching the patient‘s shoulder, can provide comfort and may alleviate pain. This is especially true when a patient is undergoing a painful or stressful procedure. Making inappropriate facial expressions may be o…
```

### 12. PFQ-fundamentals-000000064 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 64
- Chapter: Communication
- JSON path: `$.questions[63].rationale`
- Detail: Pattern requires human review against the original source.

```text
The ―B‖ in SBAR stands for ―Background,‖ or what led up to the current situation. The ―S‖ stands for Situation or what is happening right now. The ―A‖ stands for ―Assessment,‖ or what is the identified problem, concern, or need. The ―R‖ stands for ―Recommendation,‖ or what actio…
```

### 13. PFQ-fundamentals-000000068 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 68
- Chapter: Communication
- JSON path: `$.questions[67].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who is unable to take oral medication s because of persistent nausea and vomiting. When the nurse decides to call the primary care physician and as k for a different medication administration route, this is a demonstration of what act?
```

### 14. PFQ-fundamentals-000000070 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 70
- Chapter: Communication
- JSON path: `$.questions[69].rationale`
- Detail: Pattern requires human review against the original source.

```text
The primary source from which data are collected is the patient. A secondary source would include a significant other, family members, caregivers, other members of the health team, and medical records.
```

### 15. PFQ-fundamentals-000000073 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 73
- Chapter: Communication
- JSON path: `$.questions[72].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Tearing down boundariesNR I G B.C M
```

### 16. PFQ-fundamentals-000000074 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 74
- Chapter: Communication
- JSON path: `$.questions[73].rationale`
- Detail: Pattern requires human review against the original source.

```text
N R I G B When communicating with a hearing-impaired patient, the nurse should make sure that the area is well lit with as little background noise as possible. Hearing aids amplify all sounds, making noisy environments confusing and frustrating. Raising the voice level slightly,…
```

### 17. PFQ-fundamentals-000000075 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 75
- Chapter: Communication
- JSON path: `$.questions[74].rationale`
- Detail: Known source or extraction contamination detected.

```text
Providing a backrub is considered therapeutic touch; additional examples include holding a patient‘s hand and gently touching a patient‘s arm. Silence refers to being present with a patient without verbal communication. Facing the patient and refraining from unusual body movemen…
```

### 18. PFQ-fundamentals-000000077 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 77
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[76].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the last 3 days of a patient‘s pain history and notes that the pain level has remained constant. The nurse validates the pain level with the patient and decides to contact the provider for furthNerUoRrdSerIs.NInGtThBis .s cCe nOa r i o , which process is t…
```

### 19. PFQ-fundamentals-000000079 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 79
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[78].rationale`
- Detail: Pattern requires human review against the original source.

```text
A role-play strategy involves assigning learners to different roles based on expected outcomes in a particular setting. Other learners and facilitators observe the role playing, and then all are involved in the debriefing or discussion of the scenario. As with simulation, this a…
```

### 20. PFQ-fundamentals-000000081 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 81
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[80].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is preparing to restart a patient‘s intravenous line and discovers that the patient has no usable veins in either arm. When working to solve this problem, the nurse should carry out which action?
```

### 21. PFQ-fundamentals-000000091 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 91
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[90].rationale`
- Detail: Pattern requires human review against the original source.

```text
Decisions may be unduly influenced by bias, which is an inclination or tendency to favoritism or partiality. Bias may be related to a preconceived notion or prejudice such as believing that ―these people seek their medication.‖ It is important for nurses to examine personal bias…
```

### 22. PFQ-fundamentals-000000093 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 93
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[92].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "B", "C"]
```

### 23. PFQ-fundamentals-000000095 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 95
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[94].rationale`
- Detail: Pattern requires human review against the original source.

```text
Intuition is the feeling that you know something without specific evidence. Inferences are intellectual acts that involve a conclusion being made on the basis of something. The accuracy of an inference is directly related to the accuracy of what the inference is based on. Deduct…
```

### 24. PFQ-fundamentals-000000099 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 99
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[98].rationale`
- Detail: Known source or extraction contamination detected.

```text
Because nursing requires the application of knowledge to make clinical decisions and guide care, it involves active participation by the nurse. The application of knowledge requires development of a questioning attitude. This process is sometimes referred to as thinking like a n…
```

### 25. PFQ-fundamentals-000000100 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 100
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[99].rationale`
- Detail: Pattern requires human review against the original source.

```text
The nursing process is the foundation of professional nursing practice. It is the framework within which nurses provide care to patients in an organized and effective manner. Paul describes critical thinking as a complex process during which individuals think about their thinkin…
```

### 26. PFQ-fundamentals-000000110 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 110
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[109].rationale`
- Detail: Pattern requires human review against the original source.

```text
A two-part risk, Nursing diagnostic statement contains only: (1) the patient‘s identified need or problem (i.e., NANDA-I Nursing diagnostic label) and (2) factors indicating vulnerability (i.e., risk factors). The risk factor is the history of stroke. The chest discomfort and sh…
```

### 27. PFQ-fundamentals-000000123 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 123
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[122].rationale`
- Detail: Pattern requires human review against the original source.

```text
The Nursing diagnosis identifies an actual or potential problem or response to a problem. Accurate identification of Nursing diagnoses for patients results from carefully analyzing, validating, and N R I G B. clustering relateUd pSatieNnt suTbje ctivOe (symptoms) and objective (…
```

### 28. PFQ-fundamentals-000000123 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 123
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[122].rationale`
- Detail: Pattern requires human review against the original source.

```text
The Nursing diagnosis identifies an actual or potential problem or response to a problem. Accurate identification of Nursing diagnoses for patients results from carefully analyzing, validating, and N R I G B. clustering relateUd pSatieNnt suTbje ctivOe (symptoms) and objective (…
```

### 29. PFQ-fundamentals-000000124 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 124
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[123].rationale`
- Detail: Known source or extraction contamination detected.

```text
Establishing short- and long-term goals to address Nursing diagnoses involves discussion with the patient and often requires collaboration with family members and other members of the health care team. Coordinated, team-based patient care is called collaborative care. The patien…
```

### 30. PFQ-fundamentals-000000126 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 126
- Chapter: Assessment
- JSON path: `$.questions[125].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient interview consists of three phases: orientation (introductory), working, and termination. Each phase contributes to the development of trust and engagement between the nurse and the patient. During the orientation phase of the interview, the nurse should establish th…
```

### 31. PFQ-fundamentals-000000129 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 129
- Chapter: Assessment
- JSON path: `$.questions[128].rationale`
- Detail: Pattern requires human review against the original source.

```text
Auscultation is a technique of listening with the assistance of a stethoscope to sounds made by organs or systems such as the heart, blood vessels, lungs, and abdominal cavity. Inspection involves the use of vision, hearing, and smell to closely scrutinize physical characteristi…
```

### 32. PFQ-fundamentals-000000132 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 132
- Chapter: Assessment
- JSON path: `$.questions[131].rationale`
- Detail: Pattern requires human review against the original source.

```text
Triage, a form of emergency assessment, is the classification of patients according to treatment priority. Patients are categorized by the urgency of their condition. Most emergency departments use a five-tier triage system. The five-tier system classifies patients by levels num…
```

### 33. PFQ-fundamentals-000000135 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 135
- Chapter: Assessment
- JSON path: `$.questions[134].rationale`
- Detail: Pattern requires human review against the original source.

```text
Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Objective data, also referred to as signs, can be measured or observed. The …
```

### 34. PFQ-fundamentals-000000137 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 137
- Chapter: Assessment
- JSON path: `$.questions[136].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is monitoring the blood sugar results of a patient receiving an intravenou s nutritional supplement. The patient tells the nurse, ―I have never had sugar problems before. My doctor says it is because I am getting this IV.‖ These types of data are considered to be which…
```

### 35. PFQ-fundamentals-000000137 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 137
- Chapter: Assessment
- JSON path: `$.questions[136].rationale`
- Detail: Pattern requires human review against the original source.

```text
Primary data come directly from the patient. Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Family members, friends, and ot…
```

### 36. PFQ-fundamentals-000000137 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 137
- Chapter: Assessment
- JSON path: `$.questions[136].rationale`
- Detail: Pattern requires human review against the original source.

```text
Primary data come directly from the patient. Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Family members, friends, and ot…
```

### 37. PFQ-fundamentals-000000139 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 139
- Chapter: Assessment
- JSON path: `$.questions[138].rationale`
- Detail: Pattern requires human review against the original source.

```text
As patient information is collected, consistency between subjective and objective data must be confirmed. Sometimes, the nurse can use laboratory and diagnostic test results to validate the subjective data. In this case, checking the urinalysis for congruency with the patient‘s …
```

### 38. PFQ-fundamentals-000000139 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 139
- Chapter: Assessment
- JSON path: `$.questions[138].rationale`
- Detail: Pattern requires human review against the original source.

```text
As patient information is collected, consistency between subjective and objective data must be confirmed. Sometimes, the nurse can use laboratory and diagnostic test results to validate the subjective data. In this case, checking the urinalysis for congruency with the patient‘s …
```

### 39. PFQ-fundamentals-000000140 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 140
- Chapter: Assessment
- JSON path: `$.questions[139].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is attempting to get the patient to sign the operative consent. When asked if the health care provider explained the procedure to the patient, the patient replies ―Not much.‖ What action will the nurse take next?
```

### 40. PFQ-fundamentals-000000149 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 149
- Chapter: Assessment
- JSON path: `$.questions[148].rationale`
- Detail: Known source or extraction contamination detected.

```text
Patient-centered care requires the nurse to understand patient and family preferences and values. Nurses must recognize patients‘ expectations for care and provide care with respect for the diversity of human experience. While interpreting data, the nurse must be careful to avoi…
```

### 41. PFQ-fundamentals-000000155 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 155
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[154].rationale`
- Detail: Pattern requires human review against the original source.

```text
The second part of the Nursing diagnosis consists of related factors (for actual Nu rsing diagnoses) and risk factors (for risk Nursing diagnoses). Related factors are the underlying cause or etiology of a patient‘s problem. Risk factors are environmental, physical, psychologica…
```

### 42. PFQ-fundamentals-000000158 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 158
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[157].rationale`
- Detail: Pattern requires human review against the original source.

```text
All patient information should be considered as potentially contributing to the identification of diagnostic labels. This information includes subjective and objective data collected through physical assessment of the patient, interview of the patient and family members, and lab…
```

### 43. PFQ-fundamentals-000000158 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 158
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[157].rationale`
- Detail: Pattern requires human review against the original source.

```text
All patient information should be considered as potentially contributing to the identification of diagnostic labels. This information includes subjective and objective data collected through physical assessment of the patient, interview of the patient and family members, and lab…
```

### 44. PFQ-fundamentals-000000162 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 162
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[161].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Impaired self feeding rel aNt edRt o uIppeGr exBt r.e mCi t yMw e a knes s as manifested by inability to get food onto s pUo o nS. N T O
```

### 45. PFQ-fundamentals-000000162 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 162
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[161].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Impaired self feeding rel aNt edRt o uIppeGr exBt r.e mCi t yMw e a knes s as manifested by inability to get food onto s pUo o nS. N T O
```

### 46. PFQ-fundamentals-000000168 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 168
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[167].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is creating a care plan for a patient admitted with severe bone pain related t o an infected leg wound. Which diagnosis written on the plan indicates an understanding of the components of a Nursing diagnosis? (Select all that apply.)
```

### 47. PFQ-fundamentals-000000169 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 169
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[168].rationale`
- Detail: Pattern requires human review against the original source.

```text
Each type of Nursing diagnostic statement contains sections or parts. Actual Nursing diagnostic statements are written with three parts: a diagnosis label, related factors, and defining characteristics. Risk Nursing diagnoses have two segments: a diagnosis label and risk factors…
```

### 48. PFQ-fundamentals-000000172 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 172
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[171].rationale`
- Detail: Known source or extraction contamination detected.

```text
Risk factors may be environmental, physical, psychological, or situational concerns. The nurse is concerned that the patient may be at risk for suicide. Verbal statements by the patient, physical illness such as chronic pain, prior attempts to commit suicide, and a lack of socia…
```

### 49. PFQ-fundamentals-000000178 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 178
- Chapter: Planning
- JSON path: `$.questions[177].rationale`
- Detail: Pattern requires human review against the original source.

```text
Goals are broad statements of purpose that describe the aim of nursing care. Goals represent short- or long-term objectives that are determined during the planning step. Some sources establish time parameters for short- and long-term goals, whereas others do not. According to Ca…
```

### 50. PFQ-fundamentals-000000191 — correct answer not found in choices

- Severity: **high**
- Category: Structure
- Question index: 191
- Chapter: Planning
- JSON path: `$.questions[190].correct_answers`
- Detail: Available choice labels: ['B', 'C', 'D']

```text
A
```

### 51. PFQ-fundamentals-000000196 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 196
- Chapter: Planning
- JSON path: `$.questions[195].rationale`
- Detail: Pattern requires human review against the original source.

```text
Patients should be included in the planning process. Involving patients in planning their care helps them to: (1) be aware oNf i d Re n t i If i e dGn e eBd s., C( 2 ) Maccept realistic and measurable goals, and (3) embrace interventions to best achieve the mutually agreed-on go…
```

### 52. PFQ-fundamentals-000000197 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 197
- Chapter: Planning
- JSON path: `$.questions[196].rationale`
- Detail: Known source or extraction contamination detected.

```text
Measurable goals are specific, with numeric parameters or other concrete methods of judging whether the goal was met. When writing a goal statement with a patient, the nurse needs to clearly identify how achievement of the goal will be evaluated. When terms such as acceptable or…
```

### 53. PFQ-fundamentals-000000205 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 205
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[204].rationale`
- Detail: Pattern requires human review against the original source.

```text
N R I G B. C M Independent nursing interventions are tasks within the nursing scope of practice that the nurse may undertake without a physician or PCP order. Repositioning a patient in bed, performing oral hygiene, and providing emotional support through active listening are ex…
```

### 54. PFQ-fundamentals-000000205 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 205
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[204].rationale`
- Detail: Pattern requires human review against the original source.

```text
N R I G B. C M Independent nursing interventions are tasks within the nursing scope of practice that the nurse may undertake without a physician or PCP order. Repositioning a patient in bed, performing oral hygiene, and providing emotional support through active listening are ex…
```

### 55. PFQ-fundamentals-000000208 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 208
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[207].rationale`
- Detail: Pattern requires human review against the original source.

```text
With the patient‘s permission, the nurse should share instructions with the people who may assist with care. Nurses empower patients and their support systems through effective teaching. When nurses provide patients and their families with opportunities to ask questions and comp…
```

### 56. PFQ-fundamentals-000000217 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 217
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[216].rationale`
- Detail: Pattern requires human review against the original source.

```text
Evaluation is the final step in the nursing process. Evaluation focuses on the patient and the patient‘s response to n ur singNi nUt eRrv eInt ioGn s aBnd.oCutcMome attainment. Evaluation is not a record of care that was implemented. Patient outcomes serve as the criteria agains…
```

### 57. PFQ-fundamentals-000000217 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 217
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[216].rationale`
- Detail: Pattern requires human review against the original source.

```text
Evaluation is the final step in the nursing process. Evaluation focuses on the patient and the patient‘s response to n ur singNi nUt eRrv eInt ioGn s aBnd.oCutcMome attainment. Evaluation is not a record of care that was implemented. Patient outcomes serve as the criteria agains…
```

### 58. PFQ-fundamentals-000000222 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 222
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[221].rationale`
- Detail: Known source or extraction contamination detected.

```text
Delegation principles focus on the appropriate intervention (task) being performed under the correct circumstances, by the correct personnel, and with the correct direction and supervision. The right patienNt a n dRt hIe ri gGhUt tBimS.eCreNfeMr Tto components of the ―6 Rights‖ …
```

### 59. PFQ-fundamentals-000000236 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 236
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[235].rationale`
- Detail: Pattern requires human review against the original source.

```text
An admission summary includes the patient‘s history, a medication reconciliation, and an initial assessment that a dd res Ns eUs tRhSe pIaNtieGnTt‘Bs .p r obOle m s , including identification of needs pertinent to discharge planning and formulation of a plan of care based on tho…
```

### 60. PFQ-fundamentals-000000241 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 241
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[240].rationale`
- Detail: Pattern requires human review against the original source.

```text
An ineffective handoff may lead to wrong treatments, wrong medications, or other life-threatening events, increasing the length of stay and causing patient injury or death. Improvement in the hand-off process can increase patient safety and promote positive patient outcomes. The…
```

### 61. PFQ-fundamentals-000000248 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 248
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[247].rationale`
- Detail: Known source or extraction contamination detected.

```text
SBAR stands for situation (what is happening the current time), background (circumstances leading up to this situation), assessment (what the nurse thinks the problem is), and recommendation (what needs to be done to correct the situation). A history of hypertension would be bac…
```

### 62. PFQ-fundamentals-000000250 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 250
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[249].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Deontology is an ethical theory that stresses the rightness or wrongness of individual behaviors, duties, and obligations without concern for the consequences of specific actions. Meeting the needs of patients while maintaining their right to privacy, confidentiality, …
```

### 63. PFQ-fundamentals-000000268 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 268
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[267].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who has had many admissions and readmissions. T he nurse believes that the patient keeps coming to the hospital because the patient ―wants his drugs,‖ and is ―non-compliant‖ at home with diabetic therapy. To reduce the risk of slander against t …
```

### 64. PFQ-fundamentals-000000268 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 268
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[267].rationale`
- Detail: Pattern requires human review against the original source.

```text
Defamation of character occurs when a public statement is made that is false and injurious to another person. Oral defamation of character is slander. Slander is spoken information that is untrue, causing prejudice against someone or jeopardizing that person‘s reputation. The nu…
```

### 65. PFQ-fundamentals-000000274 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 274
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[273].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse knows which law protects health care professionals from charges of negligence when providing emergency care at the scene of an accident? U S N
```

### 66. PFQ-fundamentals-000000277 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 277
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[276].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The Uniform Anatomical Gift Act GB.CM U S N T O
```

### 67. PFQ-fundamentals-000000277 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 277
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[276].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The Uniform Anatomical Gift Act GB.CM U S N T O
```

### 68. PFQ-fundamentals-000000277 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 277
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[276].rationale`
- Detail: Known source or extraction contamination detected.

```text
Advance directives consist of three documents: (1) living will, (2) durable power of attorney, and (3) health care proxy, commonly referred to as a durable power of attorney for health care. The Patient‘s Bill of Rights informs consumers of health care about specific privileges …
```

### 69. PFQ-fundamentals-000000280 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 280
- Chapter: Leadership and Management
- JSON path: `$.questions[279].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is acting as a leader in the role of charge nurse and notes that the unlicen sed assistive personnel (UAP) on the floor are stressed related to their increased workload. The nurse changes the original planned approach based on the presenting situation. Which theory of …
```

### 70. PFQ-fundamentals-000000280 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 280
- Chapter: Leadership and Management
- JSON path: `$.questions[279].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Transformational U S N
```

### 71. PFQ-fundamentals-000000281 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 281
- Chapter: Leadership and Management
- JSON path: `$.questions[280].rationale`
- Detail: Pattern requires human review against the original source.

```text
Transactional leaders use reward and punishment to gain the cooperation of follow ers. Transformational leaders use methods that inspire people to follow their lead. Transformational leaders work toward transforming an organization with the help of others. The authoritarian or a…
```

### 72. PFQ-fundamentals-000000281 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 281
- Chapter: Leadership and Management
- JSON path: `$.questions[280].rationale`
- Detail: Pattern requires human review against the original source.

```text
Transactional leaders use reward and punishment to gain the cooperation of follow ers. Transformational leaders use methods that inspire people to follow their lead. Transformational leaders work toward transforming an organization with the help of others. The authoritarian or a…
```

### 73. PFQ-fundamentals-000000285 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 285
- Chapter: Leadership and Management
- JSON path: `$.questions[284].rationale`
- Detail: Pattern requires human review against the original source.

```text
Although autocratic leadership is a strict form of leadership, it is useful in crisis situations. A nurse may act as an autocratic leader when taking charge after a patient is found unresponsive. In this situation, it is helpful to have a leader who takes control and directs oth…
```

### 74. PFQ-fundamentals-000000286 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 286
- Chapter: Leadership and Management
- JSON path: `$.questions[285].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse has made patient care assignments and expects all team members to set their own goals for the day and manage their time to meet their goals. The nurse is implementing w hat style of leadership?
```

### 75. PFQ-fundamentals-000000294 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 294
- Chapter: Leadership and Management
- JSON path: `$.questions[293].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Assistance with eating breakfast U S N
```

### 76. PFQ-fundamentals-000000295 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 295
- Chapter: Leadership and Management
- JSON path: `$.questions[294].rationale`
- Detail: Pattern requires human review against the original source.

```text
The person to whom the assignment was delegated cannot delegate that assignment to someone else. If the person cannot carry out the assignment, the individual needs to notify the delegating RN so that the task may be reassigned or completed by the RN. The RN must remember to del…
```

### 77. PFQ-fundamentals-000000301 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 301
- Chapter: Leadership and Management
- JSON path: `$.questions[300].rationale`
- Detail: Known source or extraction contamination detected.

```text
Mintzberg described management in terms of behaviors. Underlying his descriptions were two assumptions: much of a manager‘s time is spent in human relations, and managers are more reactive than proactive. These assumptions provided the basis for three categories of behaviors: in…
```

### 78. PFQ-fundamentals-000000303 — NURSINGTB contamination

- Severity: **high**
- Category: Contamination
- Question index: 303
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[302].stem`
- Detail: Known source or extraction contamination detected.

```text
The American Nurses Association (ANA) standards of professional performance require nurses to use research findings in practice. How do these standards impact nurses in the workplace? NURSINGTB.CO
```

### 79. PFQ-fundamentals-000000305 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 305
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[304].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Descriptive research stud Ny URSINGTB.COM
```

### 80. PFQ-fundamentals-000000309 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 309
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[308].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Address ethical procedures. U S N
```

### 81. PFQ-fundamentals-000000325 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 325
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[324].stem`
- Detail: Pattern requires human review against the original source.

```text
Nurses use new information NinUthReSir IprNacGtiTceB. .I nCt hOeMp r o c e s s of implementing EBP, the nurse carries out which actions? (Select all that apply.)
```

### 82. PFQ-fundamentals-000000326 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 326
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[325].rationale`
- Detail: Known source or extraction contamination detected.

```text
A Magnet hospital is characterized by excellent patient outcomes resulting from nursing, a high level of nursing job satisfaction with a low nurse turnover rate, and appropriate resolution of any grievances. The Magnet Recognition Program supports an evidence-based environment, …
```

### 83. PFQ-fundamentals-000000329 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 329
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[328].rationale`
- Detail: Pattern requires human review against the original source.

```text
To teach effectively, nurses must recognize that patients of all ages come from diverse cultural and socioeconomic backgrounds. Each has a different ability to comprehend health care information. Results of the NAAL research indicate that among American adults, 30 million (14%) …
```

### 84. PFQ-fundamentals-000000332 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 332
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[331].rationale`
- Detail: Pattern requires human review against the original source.

```text
Formal patient education is delivered throughout the community in the form of media, in a variety of educational and group settings, or in a planned, goal-directed, one-on-one session with a patient in the acute care setting. Informal education is usually learner or patient dire…
```

### 85. PFQ-fundamentals-000000332 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 332
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[331].rationale`
- Detail: Pattern requires human review against the original source.

```text
Formal patient education is delivered throughout the community in the form of media, in a variety of educational and group settings, or in a planned, goal-directed, one-on-one session with a patient in the acute care setting. Informal education is usually learner or patient dire…
```

### 86. PFQ-fundamentals-000000334 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 334
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[333].rationale`
- Detail: Pattern requires human review against the original source.

```text
Some patient education sessions have formal and informal elements, because the nurse and patient may set goals together before the nurse formulates and implements the plan of care, and the patient is free to ask questions that may direct the session. The health care information …
```

### 87. PFQ-fundamentals-000000335 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 335
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[334].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is implementing a patient teaching plan regarding diabetes mellitus. One of the short-term goals of the plan is that the patient will be able to verbalize three symptoms of hypoglycemia. The nurse recognizes that this is what type of teaching?
```

### 88. PFQ-fundamentals-000000338 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 338
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[337].rationale`
- Detail: Pattern requires human review against the original source.

```text
Teaching should be tailored to elderly patients. Reports indicate that two-thirds of U.S. adults 66 years old and older have inadequate or marginal literacy skills, and 81% of patients 60 years old and older at a public hospital could not read or understand basic materials such …
```

### 89. PFQ-fundamentals-000000348 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 348
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[347].rationale`
- Detail: Pattern requires human review against the original source.

```text
Before health care teaching sessions for adults, assess reading level, learning styles, and readiness to learn. Family members should not be used as interpreters of specific medical information to maintain the patient‘s right to privacy and to avoid possible misinterpretation of…
```

### 90. PFQ-fundamentals-000000351 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 351
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[350].rationale`
- Detail: Known source or extraction contamination detected.

```text
On completion of assessment, a nursing diagnosis relevant to the educational nee ds of the patient or caregiver can be determined. Diagnoses specifically related to patient educati on include deficient knowledge, readiness for enhanced knowledge, and noncompliance. 3rd Edition
```

### 91. PFQ-fundamentals-000000352 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 352
- Chapter: Nursing Informatics
- JSON path: `$.questions[351].rationale`
- Detail: Pattern requires human review against the original source.

```text
Informatics is a broad academic field encompassing artificial intelligence, cognitive science, computer science, information science, and social science. Medical informatics refers to informatics related to health care and describes a distinct specialty in the discipline of medi…
```

### 92. PFQ-fundamentals-000000362 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 362
- Chapter: Nursing Informatics
- JSON path: `$.questions[361].rationale`
- Detail: Pattern requires human review against the original source.

```text
Descriptions of nursing informatics competencies often focus on levels that include beginner, experienced, specialist, and innovator. Beginner skills include computer, information, and web literacy; fundamental skills in information management and computer technology; and the ab…
```

### 93. PFQ-fundamentals-000000363 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 363
- Chapter: Nursing Informatics
- JSON path: `$.questions[362].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Technical competencies N R I G B.C M
```

### 94. PFQ-fundamentals-000000372 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 372
- Chapter: Nursing Informatics
- JSON path: `$.questions[371].rationale`
- Detail: Known source or extraction contamination detected.

```text
Access to electronic records requires a user to have system access and verification codes as a measure of security and protection of the patient‘s privacy. The codes leave an electronic trail of authorized users that can be audited. HIPAA sets the standards on how security and c…
```

### 95. PFQ-fundamentals-000000376 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 376
- Chapter: Health and Wellness
- JSON path: `$.questions[375].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is preparing a patient teaching plan and is seeking a way to determine the patient‘s readiness and motivation to aNct rRe ga rId i nGg l i fBe s.t yCl e cMhanges to best manage diabetes mellitus. Which model would be useful Uf o r tSh i s Nn u r sTe ? O
```

### 96. PFQ-fundamentals-000000377 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 377
- Chapter: Health and Wellness
- JSON path: `$.questions[376].rationale`
- Detail: Pattern requires human review against the original source.

```text
In the three primary components of the Health Belief Model, six main constructs influence an individual‘s decision to take action about disease prevention, screening, and controlling illness. The model suggests that individuals are motivated to take action if they believe that t…
```

### 97. PFQ-fundamentals-000000386 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 386
- Chapter: Health and Wellness
- JSON path: `$.questions[385].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
F ocu s on i m pr ovi ng qualNit yUoRf Sli IfeNthGr oTuBgh.p r eOve ntive be ha vi or s .
```

### 98. PFQ-fundamentals-000000390 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 390
- Chapter: Health and Wellness
- JSON path: `$.questions[389].rationale`
- Detail: Pattern requires human review against the original source.

```text
The genetic vulnerability of an organism, or risk of disease expression based on genotype, is involuntarily passed from biologic parents to their offspring. Societal attitudes about testing and management of high-risk populations depend on the potential for expression of genetic…
```

### 99. PFQ-fundamentals-000000397 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 397
- Chapter: Health and Wellness
- JSON path: `$.questions[396].rationale`
- Detail: Known source or extraction contamination detected.

```text
The economic stability of individuals or families can determine whether they are willing to seek preventive care or screening examinations. Even if screening is free or low cost, the patient or family members may decline because of the potential for testing positive for a diseas…
```

### 100. PFQ-fundamentals-000000399 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 399
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[398].rationale`
- Detail: Pattern requires human review against the original source.

```text
The superego is the structure that houses the moral branch of personality . The Id acts strictly on instinct without consideration of reality. The Ego is partly conscious but does not consider right from wrong. Freud‘s theory contains the ―anal phase.‖
```

### 101. PFQ-fundamentals-000000402 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 402
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[401].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient that is actively trying to conceive a child but continues to drink alcohol. The patient states that she‘ll stop drinking once she is pregnant. What is the most appropriate response by the nurse?
```

### 102. PFQ-fundamentals-000000404 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 404
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[403].stem`
- Detail: Pattern requires human review against the original source.

```text
A home health care nurse is making a well-baby visit to the home of a new mother who has an infant. What assessment finding leads the nurse to provide further anticipatory guidance and teaching to the mother?
```

### 103. PFQ-fundamentals-000000406 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 406
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[405].rationale`
- Detail: Pattern requires human review against the original source.

```text
An appropriate serving size is 1 tablespoon per year of age, so an appr opriate amount of meat for this child is 3 tablespoons, not 1/2 cup (which is 8 tablespoons). The nur se should provide more education to the family. The other options are appropriate but are not directly re…
```

### 104. PFQ-fundamentals-000000407 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 407
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[406].rationale`
- Detail: Pattern requires human review against the original source.

```text
It is common for toddlers to hNa v eRi mIa g i nGa r yBf .r i eCn d sM. They are especially important in allowingthe child to express something unpleasant. The other responses are not appropriate. NCLEX Client Needs Category: Health Promotion and Maintenance
```

### 105. PFQ-fundamentals-000000412 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 412
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[411].stem`
- Detail: Pattern requires human review against the original source.

```text
A father expresses frustration that his school-aged child is suddenly ―sick all the time.‖ What action by the nurse is best? U S N
```

### 106. PFQ-fundamentals-000000413 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 413
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[412].rationale`
- Detail: Pattern requires human review against the original source.

```text
School-aged children benefit from simple explanations they can understand. Just telling the child not to worry is dismissive of the child‘s concerns. A school-aged child may not be able to read and/or understand a written pamphlet. Using phrases such as ―put you to sleep‖ should…
```

### 107. PFQ-fundamentals-000000416 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 416
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[415].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Assess the child for signsNof RchilId abGuseBo.r nCe glMe c t .
```

### 108. PFQ-fundamentals-000000416 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 416
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[415].rationale`
- Detail: Pattern requires human review against the original source.

```text
A 3-month-old child should be able to follow a moving object with his or h er eyes. However, one single abnormal assessment finding does not necessarily mean that the child has a growt h and developmental delay. The nurse should assess for other age-appropriate behaviors. Docume…
```

### 109. PFQ-fundamentals-000000417 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 417
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[416].rationale`
- Detail: Pattern requires human review against the original source.

```text
Throwing an object down to watch someone else pick it up is a typical be havior for this age- group. The nurse should teach the parent about how this behavior relates to toddler gro wth and development. The other actions are not appropriate in this situation. U S N T O NCLEX Cli…
```

### 110. PFQ-fundamentals-000000419 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 419
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[418].stem`
- Detail: Pattern requires human review against the original source.

```text
A nurse is assessing a 12 monthNoldRat Ia weGll-bBa. Cby visit. For what developmental milestones does the nurse assess this child? ( Se l e c t a l l that apply.)
```

### 111. PFQ-fundamentals-000000420 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 420
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[419].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Weight loss and malnutrition N R I G
```

### 112. PFQ-fundamentals-000000422 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 422
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[421].stem`
- Detail: Pattern requires human review against the original source.

```text
A pregnant woman in her second trimester is scheduled for quad testing. What conditions does the nurse explain are s creUe n e dSf o Nr in Tt his assOessment? ( Select all that apply.)
```

### 113. PFQ-fundamentals-000000422 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 422
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[421].rationale`
- Detail: Known source or extraction contamination detected.

```text
Quad testing includes assessing for neural tube defects, trisomy 18, and trisomy 21 (Do wn syndrome). It does not screen for heart or blood-clotting problems. 3rd Edition
```

### 114. PFQ-fundamentals-000000425 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 425
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[424].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse plans to develop a comprehensive screening tool to use with young adults , assessing their lifestyles and healthy living habits. What barrier must the nurse plan to overcome to make this screening successful?
```

### 115. PFQ-fundamentals-000000439 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 439
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[438].stem`
- Detail: Pattern requires human review against the original source.

```text
A nurse notes an older adult puts excessive amounts of salt on her food. What intervention by the nurse is best? NUR ISG BN.CTM O
```

### 116. PFQ-fundamentals-000000441 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 441
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[440].rationale`
- Detail: Pattern requires human review against the original source.

```text
Abuse of illicit drugs can cause many symptoms, including panic attacks and aggressive behavior. After assessing for an infectious process, the nurse should determine if the patient has used any recreational drugs. The other assessments are not as important and can be completed …
```

### 117. PFQ-fundamentals-000000441 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 441
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[440].rationale`
- Detail: Pattern requires human review against the original source.

```text
Abuse of illicit drugs can cause many symptoms, including panic attacks and aggressive behavior. After assessing for an infectious process, the nurse should determine if the patient has used any recreational drugs. The other assessments are not as important and can be completed …
```

### 118. PFQ-fundamentals-000000447 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 447
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[446].rationale`
- Detail: Known source or extraction contamination detected.

```text
There are several risk factors for developing delirium, including advanced age, polypharmacy, pain, surgery, and hospitaliz aNtiUonR. SBIeinNgGbTliBnd.iCs nOoMt a risk factor. 3rd Edition
```

### 119. PFQ-fundamentals-000000453 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 453
- Chapter: Vital Signs
- JSON path: `$.questions[452].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Student pulls the pinna of the patient‘s ear up and back. U S N T
```

### 120. PFQ-fundamentals-000000461 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 461
- Chapter: Vital Signs
- JSON path: `$.questions[460].rationale`
- Detail: Pattern requires human review against the original source.

```text
This patient has orthostatic hypotension, which is a drop of 20 mm Hg in systolic reading and 10 mm Hg in diastolic readinNg wRh e nIt h eGp atBi e.n tCs t a nMd s up fr om a sitting or lying position. The patient‘s cardiovascular system does not compensate for this, so the pati…
```

### 121. PFQ-fundamentals-000000464 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 464
- Chapter: Vital Signs
- JSON path: `$.questions[463].rationale`
- Detail: Pattern requires human review against the original source.

```text
A pulse of 42 beats/min is considered bradycardia and the patient should be assessed first because perfusion could be cNo m pRr o mIi s eGd . TBhe.bClooMd pressure, pulse oximetry, and respiratory rate are normal. U S N T O
```

### 122. PFQ-fundamentals-000000464 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 464
- Chapter: Vital Signs
- JSON path: `$.questions[463].rationale`
- Detail: Pattern requires human review against the original source.

```text
A pulse of 42 beats/min is considered bradycardia and the patient should be assessed first because perfusion could be cNo m pRr o mIi s eGd . TBhe.bClooMd pressure, pulse oximetry, and respiratory rate are normal. U S N T O
```

### 123. PFQ-fundamentals-000000472 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 472
- Chapter: Vital Signs
- JSON path: `$.questions[471].rationale`
- Detail: Known source or extraction contamination detected.

```text
Dyspnea is difficult, labored breathing, usually with a rapid, shallow pattern, that may be painful. Anxiety usually is present as well. Accessory muscles in the chest and neck are used in dyspneic breathing. Many patients experiencing dyspnea find it easier to breath in an upri…
```

### 124. PFQ-fundamentals-000000488 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 488
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[487].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Prepare to treat the patient for asthma. U S N
```

### 125. PFQ-fundamentals-000000489 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 489
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[488].rationale`
- Detail: Pattern requires human review against the original source.

```text
Cranial nerve III (oculomotor nerve) is assessed by observing the patient‘s pupil size and reaction to light and the direction of gaze. Identifying a common scent would test cranial nerve I. Assessing the patient‘s visual acuity tests cranial nerve II. Assessing hearing is crani…
```

### 126. PFQ-fundamentals-000000492 — NURSINGTB contamination

- Severity: **high**
- Category: Contamination
- Question index: 492
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[491].rationale`
- Detail: Known source or extraction contamination detected.

```text
During the interview process, the nurse needs to demonstrate interest in the patient by leaning slightly toward him/her, allowing requested family or friends to accompany the patient, and closing the door to the room to ensure privacy. Typing intently when the patient is talking…
```

### 127. PFQ-fundamentals-000000497 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 497
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[496].rationale`
- Detail: Known source or extraction contamination detected.

```text
After finishing the exam, the nurse provides the patient with privacy for changing back into street clothes and any needed hygiene material. The nurse also documents the findings and cleans the room before the next patient is seen. The nurse does not simply tell the patient he/s…
```

### 128. PFQ-fundamentals-000000499 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 499
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[498].stem`
- Detail: Pattern requires human review against the original source.

```text
A nursing student wants to obsNervRe enIcultGuratBio.n practices of an ethnic minority community. What action by the student is bUe s t ?S NT O
```

### 129. PFQ-fundamentals-000000499 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 499
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[498].stem`
- Detail: Pattern requires human review against the original source.

```text
A nursing student wants to obsNervRe enIcultGuratBio.n practices of an ethnic minority community. What action by the student is bUe s t ?S NT O
```

### 130. PFQ-fundamentals-000000504 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 504
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[503].rationale`
- Detail: Pattern requires human review against the original source.

```text
Discrimination can occur at the societal level, so even though this nurse is not prejudiced, patients from ethnic and cultural minorities can still suffer from discrimination. The other answers do not explain how discrimination can occur. N R I GOBBJ:.2C1.2M
```

### 131. PFQ-fundamentals-000000507 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 507
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[506].rationale`
- Detail: Pattern requires human review against the original source.

```text
Rituals are deeply powerful and have great meaning for individuals who practice them. The nurse should work with the patient to facilitate the ritual. Investigating the rit ual for patient harm or illegality is ethnocentric; the nurse‘s first thoughts should not be on the potent…
```

### 132. PFQ-fundamentals-000000511 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 511
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[510].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Communication differences can lead to misunderstandings and possible medical errors. Many cultural groups have verbal and nonverbal communication patterns that differ from other groups. Variations can occur due to personal or social situations. The nurse should attempt…
```

### 133. PFQ-fundamentals-000000518 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 518
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[517].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "B", "C"]
```

### 134. PFQ-fundamentals-000000522 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 522
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[521].rationale`
- Detail: Known source or extraction contamination detected.

```text
The Giger and Davidhizar Transcultural Assessment Model looks at communication, space, social orientation, time, environmental control, and biological variation. The questions all address these factors; however, asking why the patient does not want to shake the nurse‘s hand soun…
```

### 135. PFQ-fundamentals-000000524 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 524
- Chapter: Spiritual Health
- JSON path: `$.questions[523].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Needs to change medicat Ni on sR. IGB.CM
```

### 136. PFQ-fundamentals-000000524 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 524
- Chapter: Spiritual Health
- JSON path: `$.questions[523].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O There are many cues to alert the nurse that a patient might have unmet spiritual needs, including facing a terminal illness. The nurse should conduct spiritual assessments on all patients, but this one is the priority.
```

### 137. PFQ-fundamentals-000000527 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 527
- Chapter: Spiritual Health
- JSON path: `$.questions[526].rationale`
- Detail: Pattern requires human review against the original source.

```text
Moral distress is cultural conflict between medical treatment and religious beliefs, expressions of concern about rejection by religious community, hesitation in accepting blood transfusion . The other diagnoses are not related. aOnning
```

### 138. PFQ-fundamentals-000000532 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 532
- Chapter: Spiritual Health
- JSON path: `$.questions[531].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Ask if the patient and family want to pray. U S N T
```

### 139. PFQ-fundamentals-000000536 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 536
- Chapter: Spiritual Health
- JSON path: `$.questions[535].rationale`
- Detail: Pattern requires human review against the original source.

```text
Promoting connectedness means recognizing that family and friends are providing at least some of the patient‘s spiritual care. The nurse best assists when offering to call someone for the patient or family. The other options may be appropriate but are not directly related to con…
```

### 140. PFQ-fundamentals-000000536 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 536
- Chapter: Spiritual Health
- JSON path: `$.questions[535].rationale`
- Detail: Pattern requires human review against the original source.

```text
Promoting connectedness means recognizing that family and friends are providing at least some of the patient‘s spiritual care. The nurse best assists when offering to call someone for the patient or family. The other options may be appropriate but are not directly related to con…
```

### 141. PFQ-fundamentals-000000540 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 540
- Chapter: Spiritual Health
- JSON path: `$.questions[539].rationale`
- Detail: Pattern requires human review against the original source.

```text
Spirituality focuses on the meanings of life, death, and existence. Religion is an organiz ed and structured method of practicing or expressing one‘s spirituality, so they are interconnected and not mutually exclusive. Religion provides the structure for expressing spiritua lity…
```

### 142. PFQ-fundamentals-000000542 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 542
- Chapter: Spiritual Health
- JSON path: `$.questions[541].rationale`
- Detail: Pattern requires human review against the original source.

```text
Native American, Hindu, and Buddhist practitioners believe that health and illness are a matter of balance or imbalance in the body. M S C : N C L E X C l i e n t N e e d sC NategRor y:IPsyGchosBoi.caCl InMtegrity
```

### 143. PFQ-fundamentals-000000542 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 542
- Chapter: Spiritual Health
- JSON path: `$.questions[541].rationale`
- Detail: Pattern requires human review against the original source.

```text
Native American, Hindu, and Buddhist practitioners believe that health and illness are a matter of balance or imbalance in the body. M S C : N C L E X C l i e n t N e e d sC NategRor y:IPsyGchosBoi.caCl InMtegrity
```

### 144. PFQ-fundamentals-000000547 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 547
- Chapter: Spiritual Health
- JSON path: `$.questions[546].rationale`
- Detail: Known source or extraction contamination detected.

```text
Native Americans often use shamans; prayers, songs, and dances; storytelling; and herbs in health care. The HOPE framework assesses sources of hope, meaning comfort, strength, peace, love, and connection; organized religion; personal spirituality and practice; and effects on med…
```

### 145. PFQ-fundamentals-000000566 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 566
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[565].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["A", "B", "D", "E", "B", "C"]
```

### 146. PFQ-fundamentals-000000572 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 572
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[571].stem`
- Detail: Pattern requires human review against the original source.

```text
The home health care nurse eNd u cRa tUe sIpSa tGiNe n tBs .o nCw hMi c h goals of hospice care? (Select all thatapply.)
```

### 147. PFQ-fundamentals-000000572 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 572
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[571].rationale`
- Detail: Known source or extraction contamination detected.

```text
The goals of hospice care include relief of suffering, supporting the family and patient, and providing grief support after the patient dies. Goals do not include keeping patients out of the hospital or lowering medical costs. 3rd Edition
```

### 148. PFQ-fundamentals-000000583 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 583
- Chapter: Human Sexuality
- JSON path: `$.questions[582].rationale`
- Detail: Pattern requires human review against the original source.

```text
The PLISSIT model is a framework for addressing sexuality. In the SS (specific suggestions) phase, the nurse provides information that allows the patient to proceed with sexual relation s. Informing the patient about sNexUuRalSpIosNitiGoTnsBth.aCt aOr eMl e s s stressful on the …
```

### 149. PFQ-fundamentals-000000587 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 587
- Chapter: Human Sexuality
- JSON path: `$.questions[586].rationale`
- Detail: Pattern requires human review against the original source.

```text
Ineffective sexuality patterns refer to a patient who expresses concern about his/her own sexuality. This patient is concerned about the effect of this surgery on his/her attractiveness and desirability. Sexual dysfunction relates more to the physical problems. The patient may h…
```

### 150. PFQ-fundamentals-000000597 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 597
- Chapter: Human Sexuality
- JSON path: `$.questions[596].rationale`
- Detail: Known source or extraction contamination detected.

```text
Fatigue, medications, pain, and impairments all can have direct effects on sexuality. Lifestyle is another factor, but occupation does not in itself influence sexuality. 3rd Edition
```

### 151. PFQ-fundamentals-000000603 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 603
- Chapter: Safety
- JSON path: `$.questions[602].rationale`
- Detail: Pattern requires human review against the original source.

```text
Firearms should be stored in a secure location with trigger locks in place. Ammunition should be stored in a separate location also locked. Proper permits should be obtained a s appropriate. Loaded firearms should never be stored where children can access them.
```

### 152. PFQ-fundamentals-000000617 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 617
- Chapter: Safety
- JSON path: `$.questions[616].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a confused, combative patient. Which action would be considered last by the nurse to control behavNior Rof thIe clGi entB? .C M
```

### 153. PFQ-fundamentals-000000617 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 617
- Chapter: Safety
- JSON path: `$.questions[616].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Apply restraints. S N T O
```

### 154. PFQ-fundamentals-000000622 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].rationale`
- Detail: Known source or extraction contamination detected.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 155. PFQ-fundamentals-000000622 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].rationale`
- Detail: Pattern requires human review against the original source.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 156. PFQ-fundamentals-000000622 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].rationale`
- Detail: Pattern requires human review against the original source.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 157. PFQ-fundamentals-000000622 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].rationale`
- Detail: Pattern requires human review against the original source.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 158. PFQ-fundamentals-000000624 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 624
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[623].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Humoral immunity is a defense system that involves antibodies and white blood cells that are produced to fight antigens. Cellular immunity involves defense by white blood cells against any microorganisms that the body does not recognize as its own. The innate (nonspeci…
```

### 159. PFQ-fundamentals-000000628 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 628
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[627].rationale`
- Detail: Pattern requires human review against the original source.

```text
The stethoscope would be a means for the pathogen to travel from source t o host. The source is the reservoir or host. The portal of exit is where the pathogen escapes from the reservoir of infection, and the portal of entry is where the microorganism enters the susceptible host.
```

### 160. PFQ-fundamentals-000000631 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 631
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[630].rationale`
- Detail: Pattern requires human review against the original source.

```text
The 80-year-old male has more risk factors because he is elderly and has increased risk of urinary tract infection related to prostate enlargement, so he has two risk factors. A 24-year-old female runner is likely healthy with no additional risk factors. The 50-year-old obese ma…
```

### 161. PFQ-fundamentals-000000636 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 636
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[635].rationale`
- Detail: Pattern requires human review against the original source.

```text
Soap and water must be used to thoroughly clean hands if there is any visible soiling or dirt and with certain infections such as Clostridium difficile and vancomycin-resistant enterococci when preparing for a sterile or surgical procedure, before and after eating, and after usi…
```

### 162. PFQ-fundamentals-000000639 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 639
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[638].rationale`
- Detail: Pattern requires human review against the original source.

```text
Droplet precautions are used when known or suspected contagious diseases can be transmitted through large droplets suspenNdedRin It h e GaUi r. SBCo.nCtNactMprecaution s are used when a known orsuspected contagious disease may be present and is transmitted through direct contact…
```

### 163. PFQ-fundamentals-000000642 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 642
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[641].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
Increased sputum produc NtioUnRSINGTB.COM
```

### 164. PFQ-fundamentals-000000642 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 642
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[641].rationale`
- Detail: Pattern requires human review against the original source.

```text
The elderly are at an increased risk for respiratory infections because of d ecreased cough reflex, decreased elastic recoil of the lungs, decreased activity of the cilia, and abnormal swallowing reflex. They do not generally have increased sputum production.
```

### 165. PFQ-fundamentals-000000646 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 646
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[645].rationale`
- Detail: Known source or extraction contamination detected.

```text
Protective precautions may require a positive-pressure room. No live plants, fresh flowers, fresh raw fruit or vegetables, sushi, or blue cheese may be brought into the room because they may harbor bacteria and fungi. The patient cannot eat just any foods because some are restri…
```

### 166. PFQ-fundamentals-000000654 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 654
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[653].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "B", "C"]
```

### 167. PFQ-fundamentals-000000660 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 660
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[659].rationale`
- Detail: Pattern requires human review against the original source.

```text
Oral care is important regardless of medication, but a soft-bristled toothbrush should be used related to increased risk of bleeding for any patient on an anticoagulant. An electric toothbrush is too aggressive,NanUdRmSoIutNhwGaTsBh .is Cn oOt Ma dequate.
```

### 168. PFQ-fundamentals-000000669 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 669
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[668].stem`
- Detail: Pattern requires human review against the original source.

```text
Regarding perineal care, whiNchUnRuSrsiInNg GacTtioBn.s CarOe Mappropriate? ( Select all that apply.)
```

### 169. PFQ-fundamentals-000000670 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 670
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[669].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Patients with diabetes U S N
```

### 170. PFQ-fundamentals-000000670 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 670
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[669].rationale`
- Detail: Pattern requires human review against the original source.

```text
Soaking the feet of patients with peripheral vascular disease, cardiovascular disease s uch as strokes and diabetes are contraindicated because it may cause skin breakdown or inf ection. Patient with arthritis or malnourished have no contraindications to having their feet soaked.
```

### 171. PFQ-fundamentals-000000671 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 671
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[670].rationale`
- Detail: Known source or extraction contamination detected.

```text
Apply warm water and a conditioner or a detangler, if available, to release tangles and avoid injury to the scalp. Use a comb and/or fingers to work through the tangles individually before shampooing. The nurse avoids cutting the patient‘s hair unless first asking the patient‘s …
```

### 172. PFQ-fundamentals-000000673 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 673
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[672].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
The bed is placed in the lNo w Rp o s iIt io nG. B.CM
```

### 173. PFQ-fundamentals-000000673 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 673
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[672].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
The patient is wearing s oc kUs. SNT O
```

### 174. PFQ-fundamentals-000000673 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 673
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[672].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
The patient is wearing s oc kUs. SNT O
```

### 175. PFQ-fundamentals-000000687 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 687
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[686].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
―I wish I could reduce myNrUisRkSbuItNI GcaTn‘Bt .d oCaOn Myt h i n g.‖
```

### 176. PFQ-fundamentals-000000693 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 693
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[692].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The nurse stands behind tNheUpRaStinIeNt wGhTilBe .a mCbOuMlat ing.
```

### 177. PFQ-fundamentals-000000693 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 693
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[692].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The nurse stands behind tNheUpRaStinIeNt wGhTilBe .a mCbOuMlat ing.
```

### 178. PFQ-fundamentals-000000696 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 696
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[695].rationale`
- Detail: Known source or extraction contamination detected.

```text
Proper positioning of the SCD sleeve allows proper fit and application, which decreases the risk of constricting the blood flow or diminishing optimal outcomes. Wrap the sleeve around the leg and fasten it with Velcro straps. Verify that two fingers fit between the leg and the s…
```

### 179. PFQ-fundamentals-000000706 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 706
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[705].rationale`
- Detail: Pattern requires human review against the original source.

```text
Occlusive dressings such as hydrocolloids and transparent films are used for autolytic debridement and are contraindicated in infected wounds. It is the most comfortable form of debridement for the patient. Nty R IGB.CM U S N T O
```

### 180. PFQ-fundamentals-000000706 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 706
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[705].rationale`
- Detail: Pattern requires human review against the original source.

```text
Occlusive dressings such as hydrocolloids and transparent films are used for autolytic debridement and are contraindicated in infected wounds. It is the most comfortable form of debridement for the patient. Nty R IGB.CM U S N T O
```

### 181. PFQ-fundamentals-000000721 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 721
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[720].rationale`
- Detail: Known source or extraction contamination detected.

```text
Cold should not be used if any of the following is present: edema (cold application slows reabsorption of the fluid), circulatory pathophysiology (cold application causes vasoconstriction, further reducing circulation to the area), and shivering (this is a comfort concern). Blee…
```

### 182. PFQ-fundamentals-000000727 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 727
- Chapter: Nutrition
- JSON path: `$.questions[726].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is performing an oral examination on a patient and notices a beefy-red tongue. The nurse identifies this as a characteristic finding for what condition? U S N
```

### 183. PFQ-fundamentals-000000728 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 728
- Chapter: Nutrition
- JSON path: `$.questions[727].rationale`
- Detail: Pattern requires human review against the original source.

```text
During feeding, the head of the bed needs to be elevated at 30 to 45 degrees or higher. Liquids are thickened, and patients are encouraged to use slow-eating habits and to alternate between bites of food and sips of fluids to facilitate swallowing. N. 6 RIGTOBP:.ECvalMuation Con…
```

### 184. PFQ-fundamentals-000000730 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 730
- Chapter: Nutrition
- JSON path: `$.questions[729].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
―I can give the patient orange juice.‖ U S N
```

### 185. PFQ-fundamentals-000000731 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 731
- Chapter: Nutrition
- JSON path: `$.questions[730].rationale`
- Detail: Pattern requires human review against the original source.

```text
Renal diets restrict potassium, sodium, protein, and phosphorous intake. Fresh fruits (except bananas) and vegetables are excellent dietary choices for individuals on a renal diet. Meats, processed foods, peanut butter, cheese, nuts, caramels, ice cream, and colas are typically …
```

### 186. PFQ-fundamentals-000000733 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 733
- Chapter: Nutrition
- JSON path: `$.questions[732].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Flushes the tube with a small amount of air. U S N
```

### 187. PFQ-fundamentals-000000743 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 743
- Chapter: Nutrition
- JSON path: `$.questions[742].rationale`
- Detail: Pattern requires human review against the original source.

```text
As BMI levels rise, blood pressure and cholesterol levels also rise and the average high- density lipoprotein (HDL), or good, cholesterol levels decrease. Hyperlipidemia (elevation of plasma cholesterol, triglycerides, or both) or low HDL levels contribute to the development of …
```

### 188. PFQ-fundamentals-000000747 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 747
- Chapter: Nutrition
- JSON path: `$.questions[746].rationale`
- Detail: Known source or extraction contamination detected.

```text
Administering an enteral feeding may be delegated, at the nurse‘s discretion, to UAP in accordance with state regulations and facility policies and procedures. The nurse should verify tube placement and assess the patient prior to delegating this procedure. The UAP can perform o…
```

### 189. PFQ-fundamentals-000000747 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 747
- Chapter: Nutrition
- JSON path: `$.questions[746].rationale`
- Detail: Pattern requires human review against the original source.

```text
Administering an enteral feeding may be delegated, at the nurse‘s discretion, to UAP in accordance with state regulations and facility policies and procedures. The nurse should verify tube placement and assess the patient prior to delegating this procedure. The UAP can perform o…
```

### 190. PFQ-fundamentals-000000749 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 749
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[748].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O The frontal lobes of the cerebrum are the areas of the brain responsible for voluntary motor function, concentration, communication, decision making, and personality. The parietal lobes are responsible for the sense of touch, distinguishing the shape and texture of obj…
```

### 191. PFQ-fundamentals-000000754 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 754
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[753].rationale`
- Detail: Pattern requires human review against the original source.

```text
Hearing ability can be determined by observing the patient‘s conversation and responses and by talking with the patient in a normal conversational tone while standing slightly behind t he patient. If the patient does not respond appropriately, a hearing impairment may exist. Sta…
```

### 192. PFQ-fundamentals-000000763 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 763
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[762].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is providing education to the family of a patient being discharged with dementia. Which statement by the family indicates an appropriate level of understanding of dementia? (Select all that apply.)
```

### 193. PFQ-fundamentals-000000766 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 766
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[765].rationale`
- Detail: Pattern requires human review against the original source.

```text
Balance, eyesight, hearing, and sensation are all sensory function. Asking if the patient likes the newspaper does not specifically address vision. M S C : NC L E X C l i e n t Nee d s CNa tegRor y:IP hyGs i o lBo g.i cCa l InMtegrity
```

### 194. PFQ-fundamentals-000000766 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 766
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[765].rationale`
- Detail: Pattern requires human review against the original source.

```text
Balance, eyesight, hearing, and sensation are all sensory function. Asking if the patient likes the newspaper does not specifically address vision. M S C : NC L E X C l i e n t Nee d s CNa tegRor y:IP hyGs i o lBo g.i cCa l InMtegrity
```

### 195. PFQ-fundamentals-000000769 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 769
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[768].rationale`
- Detail: Pattern requires human review against the original source.

```text
If a patient has expressive aphasia, he or she understands language but is unable to answer questions, name common obNjeUctsR, SorIstNatGeTsiBm.plCe Oi dMe a s . The patient can answer yes/no questions by shaking the head. The patient might be able to point to pictures to expres…
```

### 196. PFQ-fundamentals-000000772 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 772
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[771].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient experiencing dizziness or vertigo exercises caution when changing positions. The patient suffering from motion sickness needs to ride in the front seat of the car and look far ahead through the car windshield. Keeping rooms well-lit and focusing ahead when walking, u…
```

### 197. PFQ-fundamentals-000000774 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 774
- Chapter: Stress and Coping
- JSON path: `$.questions[773].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
―I will join a support groupU.‖ SNT O
```

### 198. PFQ-fundamentals-000000776 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 776
- Chapter: Stress and Coping
- JSON path: `$.questions[775].rationale`
- Detail: Pattern requires human review against the original source.

```text
The endocrine system responds to stress on the body such as what happens during an acute MI. Corticosteroids are important in the stress response because they increase serum glucose levels and inhibit the inflammatory response. Although MIs can be seen in diabetics, there is not…
```

### 199. PFQ-fundamentals-000000778 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 778
- Chapter: Stress and Coping
- JSON path: `$.questions[777].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Eat a diet with lots of fiber. U S N T O
```

### 200. PFQ-fundamentals-000000778 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 778
- Chapter: Stress and Coping
- JSON path: `$.questions[777].rationale`
- Detail: Pattern requires human review against the original source.

```text
High stress levels are known to exacerbate multiple sclerosis and other autoimmune diseases. Exercise helps keep muscles loose and helps with balance. Assessing skin for pressure sores and eating a diet with high fiber prevents complications from multiple sclerosis. Analyzing
```

### 201. PFQ-fundamentals-000000780 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 780
- Chapter: Stress and Coping
- JSON path: `$.questions[779].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Blood pressure of 120/84N R I G B.C M
```

### 202. PFQ-fundamentals-000000792 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 792
- Chapter: Stress and Coping
- JSON path: `$.questions[791].rationale`
- Detail: Pattern requires human review against the original source.

```text
The release of hormones increases the heart rate, resulting in increased cardiac output, and elevated blood pressure. TheNre isRanIi n c rGeUa s eBSi.n Ct h e Mf low of blood to muscles at the expense ofthe digestive and other systems not immediately needed in the fight-or-fligh…
```

### 203. PFQ-fundamentals-000000793 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 793
- Chapter: Stress and Coping
- JSON path: `$.questions[792].rationale`
- Detail: Pattern requires human review against the original source.

```text
Personality factors such as resilience, hardiness, and sense of coherence can buffer t he impact of stress, reducing the negative consequences. Gender is not a personality factor . Coping style refers to a pattern of measures taken to relieve stress but is not a personality fact…
```

### 204. PFQ-fundamentals-000000795 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 795
- Chapter: Stress and Coping
- JSON path: `$.questions[794].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "C", "E", "B", "C"]
```

### 205. PFQ-fundamentals-000000797 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 797
- Chapter: Stress and Coping
- JSON path: `$.questions[796].rationale`
- Detail: Known source or extraction contamination detected.

```text
To care most effectively for others, nurses must first take time to care for themselves. Many of the stress reduction interventions incorporated into patient care plans can be effective in addressing the stressors faced by nurses. Exercise, balanced nutrition, and mindfulness th…
```

### 206. PFQ-fundamentals-000000815 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 815
- Chapter: Sleep
- JSON path: `$.questions[814].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Slow rhythmic scanning eye movements U S N
```

### 207. PFQ-fundamentals-000000815 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 815
- Chapter: Sleep
- JSON path: `$.questions[814].rationale`
- Detail: Pattern requires human review against the original source.

```text
During non –rapid eye movement (NREM) sleep, in which REM does not occur, physiological activity is reduced, brain waves, breathing and heart rate slow, and blood p ressure drops. Slow scanning eye movements do not occur in either REM or NREM. Dreaming occurs in REM.
```

### 208. PFQ-fundamentals-000000822 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 822
- Chapter: Sleep
- JSON path: `$.questions[821].rationale`
- Detail: Known source or extraction contamination detected.

```text
Medications would be used cNarUeRf ulSlyIaNnGd dToBn.otCalwMays improve sleep. Addressing the sleep environment, maintaining sleep routines, providing light snacks if allowed, and instituting relaxation measures will all improve sleep. 3rd Edition
```

### 209. PFQ-fundamentals-000000824 — repeated word

- Severity: **medium**
- Category: Text
- Question index: 824
- Chapter: Diagnostic Testing
- JSON path: `$.questions[823].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for an elderly patient with dementia. Which laboratory finding indicates to the nurse that that patient is often forgetting to eat meals?
```

### 210. PFQ-fundamentals-000000825 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 825
- Chapter: Diagnostic Testing
- JSON path: `$.questions[824].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Prothrombin time (PT) 11.5 sec U S N
```

### 211. PFQ-fundamentals-000000832 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 832
- Chapter: Diagnostic Testing
- JSON path: `$.questions[831].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Shrimp and scallops U S N T O
```

### 212. PFQ-fundamentals-000000835 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 835
- Chapter: Diagnostic Testing
- JSON path: `$.questions[834].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Provide a quiet, dark envNiroUnRmSenIt NsoGtThaBt .thCe Op aMt i e n t can rest comfortably.
```

### 213. PFQ-fundamentals-000000843 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 843
- Chapter: Diagnostic Testing
- JSON path: `$.questions[842].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
White blood cell count (WNBCR) 4I5U0 0G/Sm mNB3.CT M O
```

### 214. PFQ-fundamentals-000000843 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 843
- Chapter: Diagnostic Testing
- JSON path: `$.questions[842].rationale`
- Detail: Pattern requires human review against the original source.

```text
Red blood cell count of 5.8 million and hemoglobin value of 14 g/dL are both norm al. Hematocrit level of 25% is very low and indicative of ongoing anemia. White blood cell and platelet counts are not checked for anemia.
```

### 215. PFQ-fundamentals-000000845 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 845
- Chapter: Diagnostic Testing
- JSON path: `$.questions[844].rationale`
- Detail: Pattern requires human review against the original source.

```text
Interventions for the Nursing diagnosis of risk for infection involve monitoring for signs and symptoms of infection, preventing contamination of supplies by maintaining a sterile field during the procedure, and teaching the patient how to care for the site afterward. Providing …
```

### 216. PFQ-fundamentals-000000847 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 847
- Chapter: Diagnostic Testing
- JSON path: `$.questions[846].rationale`
- Detail: Known source or extraction contamination detected.

```text
Alanine aminotransferase (ALT) and alkaline phosphatase (ALP) are indicators of liver function, and increased levels indicate liver damage from a variety of causes. BUN, ANA, ESR, and FDP are not indicators of liver function. NCLEX Client Needs Category: Reduction of Risk Potent…
```

### 217. PFQ-fundamentals-000000850 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 850
- Chapter: Medication Administration
- JSON path: `$.questions[849].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who is in agonizing pain. All the following options are listed on the patient‘s medication order sheet to relive pain. The nurse knows which option that will provide the most rapid pain relief for the patient?
```

### 218. PFQ-fundamentals-000000861 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 861
- Chapter: Medication Administration
- JSON path: `$.questions[860].rationale`
- Detail: Pattern requires human review against the original source.

```text
Asking if the patient has been taking extra doses of the medication will allow the nurse to determine if the patient has been taking too much of the drug or more than was prescribed. Toxicity occurs when the patient receives/takes excessive amounts of the drug. Therapies
```

### 219. PFQ-fundamentals-000000868 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 868
- Chapter: Medication Administration
- JSON path: `$.questions[867].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient with multiple chronic illnesses who is having difficulty remembering to take multiple medications at the correct times. Which is the appropriat e Nursing diagnosis for this patient?
```

### 220. PFQ-fundamentals-000000871 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 871
- Chapter: Medication Administration
- JSON path: `$.questions[870].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "E", "F", "B", "C"]
```

### 221. PFQ-fundamentals-000000872 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 872
- Chapter: Medication Administration
- JSON path: `$.questions[871].rationale`
- Detail: Known source or extraction contamination detected.

```text
Parenteral medications are administered by injection into tissue, muscle, or a vein rather than through the gastrointestinal or respiratory route. Therapies 3rd Edition
```

### 222. PFQ-fundamentals-000000879 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 879
- Chapter: Pain Management
- JSON path: `$.questions[878].rationale`
- Detail: Pattern requires human review against the original source.

```text
Referred pain is pain that occurs when discomfort is felt in a different area than the source of the pain. Phantom pain occurs in amputees when pain is felt in the missing limb. Neuropathic pain occurs in the nervous system and often feels like burning or tingling. Psychogenic p…
```

### 223. PFQ-fundamentals-000000889 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 889
- Chapter: Pain Management
- JSON path: `$.questions[888].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who has a PCA pump following total hyster ectomy surgery. The nurse sees the visitor push the PCA button while the patient is sleeping quietly. What is the best response of the nurse?
```

### 224. PFQ-fundamentals-000000889 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 889
- Chapter: Pain Management
- JSON path: `$.questions[888].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
―PCA pumps are great because she doesn‘t have to wait for me to administer her pain medication.‖
```

### 225. PFQ-fundamentals-000000890 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 890
- Chapter: Pain Management
- JSON path: `$.questions[889].rationale`
- Detail: Pattern requires human review against the original source.

```text
Pain character should be assessed using questions to learn more about what the pain feels like. Examples like stabbing, aching, burning may be used so that patients can under stand what the nurse is requesting. Onset is determined by asking when the pain started. Exacerbating/re…
```

### 226. PFQ-fundamentals-000000892 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 892
- Chapter: Pain Management
- JSON path: `$.questions[891].rationale`
- Detail: Pattern requires human review against the original source.

```text
Goals must be measurable and objective so that nursing staff can determine when each of the goals has been met. Having the patient describe meditation techniques is measurable because the nursing staff can determine whether he can actually describe them. Goals are achieved by th…
```

### 227. PFQ-fundamentals-000000895 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 895
- Chapter: Pain Management
- JSON path: `$.questions[894].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient‘s history of rheumatoid arthritis, previous knee replacement surgery, and marathon running indicate that the patient has had significant experience dealing with pain, which will affect how he or she experiences pain after this surgery. The other factors will not affe…
```

### 228. PFQ-fundamentals-000000898 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 898
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[897].rationale`
- Detail: Pattern requires human review against the original source.

```text
Airway maintenance and protection is the highest priority for this patient, so the nurse should assess the endotracheal tube first to ensure that it is patent and positioned correctl y. The other tubes may be assessed afterward.
```

### 229. PFQ-fundamentals-000000904 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 904
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[903].rationale`
- Detail: Pattern requires human review against the original source.

```text
The large red blood stain over the incision and feeling of ripping open most likely indicates that the patient‘s wound has dehisced or eviscerated. The nurse should immediately lower the patient to the floor to reduce tension on the wound. Patient modesty and privacy should be m…
```

### 230. PFQ-fundamentals-000000910 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 910
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[909].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient must take in a deep breath while holding the spirometer to the mouth s o that the device can indicate how much air is being inhaled into the lungs. The remaining responses are correct components of the procedure.
```

### 231. PFQ-fundamentals-000000915 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 915
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[914].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is obtaining preoperative information for a patient who will be having emergency surgery shortly for a ruptured appendix. Which information is crucial for the nurse to assess? (Select all that apply.)
```

### 232. PFQ-fundamentals-000000915 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 915
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[914].rationale`
- Detail: Pattern requires human review against the original source.

```text
Priority assessment must be completed prior to emergency surgery, including use of medications, alcohol, tobacco, or recreational drugs because these may interact with anesthesia medications. Allergies must be identified to prevent reactions in the operating room. Special precau…
```

### 233. PFQ-fundamentals-000000919 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 919
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[918].rationale`
- Detail: Known source or extraction contamination detected.

```text
Signs of internal bleeding include tachycardia, increased abdominal pain and a drop in hematocrit/hemoglobin. Urinary output would decrease with internal bleeding because the kidneys work to conserve fluids. Itching and constipation are not signs of internal bleeding. 3rd Edition
```

### 234. PFQ-fundamentals-000000932 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 932
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[931].rationale`
- Detail: Pattern requires human review against the original source.

```text
Hemodilution is a common finding when patients are in fluid overload caused by congestive heart failure. A normal hematocrit result is 42% to 52% for a male and 37% to 47% for a female, so the patient‘s 32% Nhe mRat oIcrit Gl eveBl .isCm arMked ly low. The other laboratory resul…
```

### 235. PFQ-fundamentals-000000932 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 932
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[931].rationale`
- Detail: Pattern requires human review against the original source.

```text
Hemodilution is a common finding when patients are in fluid overload caused by congestive heart failure. A normal hematocrit result is 42% to 52% for a male and 37% to 47% for a female, so the patient‘s 32% Nhe mRat oIcrit Gl eveBl .isCm arMked ly low. The other laboratory resul…
```

### 236. PFQ-fundamentals-000000937 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 937
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[936].rationale`
- Detail: Pattern requires human review against the original source.

```text
The goal of long-term therapy for the patient with COPD is usually to have an oxygen saturation level of more than 90%, which represents adequate delivery of oxygen to the tissues. Oxygen saturation may decrease during exercise, sleep, or deterioration of the respiratory status.…
```

### 237. PFQ-fundamentals-000000941 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 941
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[940].rationale`
- Detail: Pattern requires human review against the original source.

```text
Only the inner cannula of the tracheostomy is removed for cleaning. The outer cannul a stays in the trachea to maintain airway patency. Clean gloves are applied before the soiled dress ing is removed. Normal sterile saline is used to remove secretions that have built u p on the …
```

### 238. PFQ-fundamentals-000000942 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 942
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[941].rationale`
- Detail: Known source or extraction contamination detected.

```text
The head of the patient‘s bed should be elevated prior to suctioning to facilitate coughing out secretions. Suction is always applied intermittently as the catheter is withdrawn. Water-soluble lubricant is used when suctioning the naris but not a tracheostomy because the secreti…
```

### 239. PFQ-fundamentals-000000942 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 942
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[941].rationale`
- Detail: Pattern requires human review against the original source.

```text
The head of the patient‘s bed should be elevated prior to suctioning to facilitate coughing out secretions. Suction is always applied intermittently as the catheter is withdrawn. Water-soluble lubricant is used when suctioning the naris but not a tracheostomy because the secreti…
```

### 240. PFQ-fundamentals-000000944 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 944
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[943].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the patient‘s laboratory results. Which result must be communicated to t hephysician immediately? a . Serumchloride level 85 m E qN/ L R I GB.CM
```

### 241. PFQ-fundamentals-000000944 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 944
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[943].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the patient‘s laboratory results. Which result must be communicated to t hephysician immediately? a . Serumchloride level 85 m E qN/ L R I GB.CM
```

### 242. PFQ-fundamentals-000000944 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 944
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[943].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the patient‘s laboratory results. Which result must be communicated to t hephysician immediately? a . Serumchloride level 85 m E qN/ L R I GB.CM
```

### 243. PFQ-fundamentals-000000944 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 944
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[943].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Serum sodium level 134 m UE q / LS NT O
```

### 244. PFQ-fundamentals-000000955 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 955
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[954].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "B", "C"]
```

### 245. PFQ-fundamentals-000000961 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 961
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[960].rationale`
- Detail: Pattern requires human review against the original source.

```text
A serum sodium level of 124 mEq/L is dangerously low and may cause neurol ogic problems including seizures, confusion, and weakness. Regular neurologic checks should be performed and the patient should be placed on seizure precautions until the sodium level is corrected. Encoura…
```

### 246. PFQ-fundamentals-000000962 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 962
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[961].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient should be instructed to take the diuretic early in the morning so that the effects will wear off before the patient goes to bed at night. Decreasing the dose could lead to fluid overload and pulmonary edema. Therapies
```

### 247. PFQ-fundamentals-000000963 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 963
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[962].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
―These medications will iNn c rRea s eIyo Gu r uBr i n.eCo u tMp u t until your kidneys recover.‖
```

### 248. PFQ-fundamentals-000000967 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 967
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[966].rationale`
- Detail: Known source or extraction contamination detected.

```text
If a person produces the B antigen, the blood type is classified as B. Type O blood is classified as universal donors because their blood cells contain no antigens. Rh positive (Rh+) blood which means the person has the Rh factor on the surface of the red blood cells. Those who …
```

### 249. PFQ-fundamentals-000000968 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 968
- Chapter: Bowel Elimination
- JSON path: `$.questions[967].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who periodically has small streaks of fresh red blood in the stool. The patient denies abdominal pain or loss of appetite. The nurse identifies wh at to be the most likely cause of this patient‘s bleeding?
```

### 250. PFQ-fundamentals-000000979 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 979
- Chapter: Bowel Elimination
- JSON path: `$.questions[978].rationale`
- Detail: Pattern requires human review against the original source.

```text
Patients with a traumatic brain injury often have increased intracranial pressure, w hich can be worsened with enema administration, thus putting the patient at risk for additional neurologic damage. The provider should be contacted and the order should be questioned. Constipati…
```

### 251. PFQ-fundamentals-000000989 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 989
- Chapter: Bowel Elimination
- JSON path: `$.questions[988].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a postoperative patient who had a colostomy placed 2 days ago. The appliance needs to be changed for the first time. Which ostomy care actions can the nurse delegate to the nursing assistant? (Select all that apply.)
```

### 252. PFQ-fundamentals-000000990 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 990
- Chapter: Bowel Elimination
- JSON path: `$.questions[989].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who will be having a colonoscopy the following morning. Which items must be removed from the patient‘s dinner tray since they are not allowed prior to the test? (Select all that apply.)
```

### 253. PFQ-fundamentals-000000990 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 990
- Chapter: Bowel Elimination
- JSON path: `$.questions[989].rationale`
- Detail: Known source or extraction contamination detected.

```text
Patients who will undergo colonoscopy testing should have a clear liquid diet the day before the exam, so cream of chicken soup and coffee creamer should not be consumed. Foods with red food coloring should also be avoided prior to colonoscopy. 3rd Edition
```

### 254. PFQ-fundamentals-000000990 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 990
- Chapter: Bowel Elimination
- JSON path: `$.questions[989].rationale`
- Detail: Pattern requires human review against the original source.

```text
Patients who will undergo colonoscopy testing should have a clear liquid diet the day before the exam, so cream of chicken soup and coffee creamer should not be consumed. Foods with red food coloring should also be avoided prior to colonoscopy. 3rd Edition
```

### 255. PFQ-fundamentals-000000997 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 997
- Chapter: Urinary Elimination
- JSON path: `$.questions[996].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a seriously ill patient whose laboratory results show a serum creatinine level of 3.5 mg/dL and a serum BUN of 35 mg/dL. Which conclusion can the nurse draw from these test results?
```

### 256. PFQ-fundamentals-000000998 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 998
- Chapter: Urinary Elimination
- JSON path: `$.questions[997].rationale`
- Detail: Pattern requires human review against the original source.

```text
Patients in renal failure often require dialysis to reduce serum potassium levels to less than 5.5 mmol/L . Critically high serum potassium levels can lead to lethal arrhythmias and must be corrected promptly. Patients with advanced renal failure may require emergency hemodialys…
```

### 257. PFQ-fundamentals-000001004 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 1004
- Chapter: Urinary Elimination
- JSON path: `$.questions[1003].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient has acute urinary retention with overflow as evidenced by 1100 mL of urine in the bladder and frequent passage of small amounts of urine. The priority nursing diagnosi s is thus Impaired urination r/t obstruction of urinary bladder outlet. Urinary retention is the ca…
```

### 258. PFQ-fundamentals-000001008 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 1008
- Chapter: Urinary Elimination
- JSON path: `$.questions[1007].stem`
- Detail: Pattern requires human review against the original source.

```text
The preceptor is watching a nursing student care for a male patient who requires a condom catheter. Which action by theNnUuRrsiSnIg NstuGdTenBt .inCdiOcaMtes that the procedure is performed correctly?
```

### 259. PFQ-fundamentals-000001012 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 1012
- Chapter: Urinary Elimination
- JSON path: `$.questions[1011].rationale`
- Detail: Pattern requires human review against the original source.

```text
Concentrated dark urine indicates dehydration rather than infection of the urinary tract. Urine that smells of sweet fruit contains ketones from high blood sugar . Urine that is cloudy with a foul odor and positive for nitrites is most likely due to urinary tract infection. Freq…
```

### 260. PFQ-fundamentals-000001012 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1012
- Chapter: Urinary Elimination
- JSON path: `$.questions[1011].rationale`
- Detail: Pattern requires human review against the original source.

```text
Concentrated dark urine indicates dehydration rather than infection of the urinary tract. Urine that smells of sweet fruit contains ketones from high blood sugar . Urine that is cloudy with a foul odor and positive for nitrites is most likely due to urinary tract infection. Freq…
```

### 261. PFQ-fundamentals-000001015 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 1015
- Chapter: Urinary Elimination
- JSON path: `$.questions[1014].rationale`
- Detail: Known source or extraction contamination detected.

```text
The nurse assistant can help the nurse by keeping the urine collection container cool on ice, dumping the urine from the patient‘s first void, and reminding the patient not to put toilet tissue in the urine specimen. NTheRnurIse aGsUs i sBSt a.n tCca nMa l so transport the speci…
```

### 262. PFQ-fundamentals-000001016 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1016
- Chapter: Death and Loss
- JSON path: `$.questions[1015].stem`
- Detail: Pattern requires human review against the original source.

```text
The hospice nurse is caring for a terminally ill patient. The patient‘s son is distraught because the patient will probably die within the next few days and there is nothing he can do about it. What is the most appropriate nursing diagnosis for the patient‘s son currently?
```

### 263. PFQ-fundamentals-000001017 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 1017
- Chapter: Death and Loss
- JSON path: `$.questions[1016].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a terminally ill patient whose children have come home to be with their mother during her last few days. They spend time looking through picture albums, watching old home movi es , and r eme mNbUe rRi nSg If uNn Gt iTmBe s.s pCeOn tMto ge th er. The nur s…
```

### 264. PFQ-fundamentals-000001017 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 1017
- Chapter: Death and Loss
- JSON path: `$.questions[1016].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a terminally ill patient whose children have come home to be with their mother during her last few days. They spend time looking through picture albums, watching old home movi es , and r eme mNbUe rRi nSg If uNn Gt iTmBe s.s pCeOn tMto ge th er. The nur s…
```

### 265. PFQ-fundamentals-000001025 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1025
- Chapter: Death and Loss
- JSON path: `$.questions[1024].stem`
- Detail: Pattern requires human review against the original source.

```text
The hospice nurse is caring for a several adult children shortly after the death of a parent. They have various reactions as they deal with their loss. The nurse recognizes which reactions to be in the cognitive domain?
```

### 266. PFQ-fundamentals-000001026 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1026
- Chapter: Death and Loss
- JSON path: `$.questions[1025].rationale`
- Detail: Pattern requires human review against the original source.

```text
Often caregivers neglect their own needs while in the caregiver role. The spouse understands the patient will die soon and is being realistic in understanding his or her o wn physical needs have been neglected. This shows healthy coping.
```

### 267. PFQ-fundamentals-000001029 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1029
- Chapter: Death and Loss
- JSON path: `$.questions[1028].stem`
- Detail: Pattern requires human review against the original source.

```text
The home care nurse is caring for a terminally ill patient who states that he wants to set up a scholarship in his name at the local university before he dies. What is the best action by the nurse?
```

### 268. PFQ-fundamentals-000001039 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 1039
- Chapter: Death and Loss
- JSON path: `$.questions[1038].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who just died after a lengthy illne ss. Which portions of postmortem care may be delegated by the nurse to the nursing assistant? ( Select all that apply.)
```
