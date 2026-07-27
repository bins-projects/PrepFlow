# Fundamentals QA — confirmed-damage

> Review queue only. The Pack has not been modified.

- Findings: **91**
- Questions affected: **85**

## Counts by rule

- possible broken web text: 53
- possible split suffix: 25
- detached taxonomy word: 10
- NURSINGTB contamination: 2
- repeated word: 1

## Findings

### 1. PFQ-fundamentals-000000011 — possible broken web text

- Question index: 11
- Severity: high
- JSON path: `$.questions[10].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Expect that the patient may return to the hospital if the discharge process is poorly done. NUR ISG BN.CTM O
```

### 2. PFQ-fundamentals-000000061 — possible broken web text

- Question index: 61
- Severity: high
- JSON path: `$.questions[60].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Therapeutic touch, such as holding the patient‘s hand or touching the patient‘s shoulder, can provide comfort and may alleviate pain. This is especially true when a patient is undergoing a painful or stressful procedure. Making inappropriate facial expressions may be o…
```

### 3. PFQ-fundamentals-000000064 — possible broken web text

- Question index: 64
- Severity: high
- JSON path: `$.questions[63].rationale`
- Detail: Pattern requires human review against the original source.

```text
The ―B‖ in SBAR stands for ―Background,‖ or what led up to the current situation. The ―S‖ stands for Situation or what is happening right now. The ―A‖ stands for ―Assessment,‖ or what is the identified problem, concern, or need. The ―R‖ stands for ―Recommendation,‖ or what actio…
```

### 4. PFQ-fundamentals-000000068 — possible split suffix

- Question index: 68
- Severity: medium
- JSON path: `$.questions[67].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who is unable to take oral medication s because of persistent nausea and vomiting. When the nurse decides to call the primary care physician and as k for a different medication administration route, this is a demonstration of what act?
```

### 5. PFQ-fundamentals-000000073 — possible broken web text

- Question index: 73
- Severity: high
- JSON path: `$.questions[72].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Tearing down boundariesNR I G B.C M
```

### 6. PFQ-fundamentals-000000074 — possible broken web text

- Question index: 74
- Severity: high
- JSON path: `$.questions[73].rationale`
- Detail: Pattern requires human review against the original source.

```text
N R I G B When communicating with a hearing-impaired patient, the nurse should make sure that the area is well lit with as little background noise as possible. Hearing aids amplify all sounds, making noisy environments confusing and frustrating. Raising the voice level slightly,…
```

### 7. PFQ-fundamentals-000000110 — possible split suffix

- Question index: 110
- Severity: medium
- JSON path: `$.questions[109].rationale`
- Detail: Pattern requires human review against the original source.

```text
A two-part risk, Nursing diagnostic statement contains only: (1) the patient‘s identified need or problem (i.e., NANDA-I Nursing diagnostic label) and (2) factors indicating vulnerability (i.e., risk factors). The risk factor is the history of stroke. The chest discomfort and sh…
```

### 8. PFQ-fundamentals-000000123 — possible broken web text

- Question index: 123
- Severity: high
- JSON path: `$.questions[122].rationale`
- Detail: Pattern requires human review against the original source.

```text
The Nursing diagnosis identifies an actual or potential problem or response to a problem. Accurate identification of Nursing diagnoses for patients results from carefully analyzing, validating, and N R I G B. clustering relateUd pSatieNnt suTbje ctivOe (symptoms) and objective (…
```

### 9. PFQ-fundamentals-000000132 — detached taxonomy word

- Question index: 132
- Severity: medium
- JSON path: `$.questions[131].rationale`
- Detail: Pattern requires human review against the original source.

```text
Triage, a form of emergency assessment, is the classification of patients according to treatment priority. Patients are categorized by the urgency of their condition. Most emergency departments use a five-tier triage system. The five-tier system classifies patients by levels num…
```

### 10. PFQ-fundamentals-000000135 — detached taxonomy word

- Question index: 135
- Severity: medium
- JSON path: `$.questions[134].rationale`
- Detail: Pattern requires human review against the original source.

```text
Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Objective data, also referred to as signs, can be measured or observed. The …
```

### 11. PFQ-fundamentals-000000137 — possible split suffix

- Question index: 137
- Severity: medium
- JSON path: `$.questions[136].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is monitoring the blood sugar results of a patient receiving an intravenou s nutritional supplement. The patient tells the nurse, ―I have never had sugar problems before. My doctor says it is because I am getting this IV.‖ These types of data are considered to be which…
```

### 12. PFQ-fundamentals-000000137 — possible split suffix

- Question index: 137
- Severity: medium
- JSON path: `$.questions[136].rationale`
- Detail: Pattern requires human review against the original source.

```text
Primary data come directly from the patient. Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Family members, friends, and ot…
```

### 13. PFQ-fundamentals-000000139 — possible broken web text

- Question index: 139
- Severity: high
- JSON path: `$.questions[138].rationale`
- Detail: Pattern requires human review against the original source.

```text
As patient information is collected, consistency between subjective and objective data must be confirmed. Sometimes, the nurse can use laboratory and diagnostic test results to validate the subjective data. In this case, checking the urinalysis for congruency with the patient‘s …
```

### 14. PFQ-fundamentals-000000158 — possible split suffix

- Question index: 158
- Severity: medium
- JSON path: `$.questions[157].rationale`
- Detail: Pattern requires human review against the original source.

```text
All patient information should be considered as potentially contributing to the identification of diagnostic labels. This information includes subjective and objective data collected through physical assessment of the patient, interview of the patient and family members, and lab…
```

### 15. PFQ-fundamentals-000000162 — possible split suffix

- Question index: 162
- Severity: medium
- JSON path: `$.questions[161].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Impaired self feeding rel aNt edRt o uIppeGr exBt r.e mCi t yMw e a knes s as manifested by inability to get food onto s pUo o nS. N T O
```

### 16. PFQ-fundamentals-000000162 — possible broken web text

- Question index: 162
- Severity: high
- JSON path: `$.questions[161].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Impaired self feeding rel aNt edRt o uIppeGr exBt r.e mCi t yMw e a knes s as manifested by inability to get food onto s pUo o nS. N T O
```

### 17. PFQ-fundamentals-000000205 — possible broken web text

- Question index: 205
- Severity: high
- JSON path: `$.questions[204].rationale`
- Detail: Pattern requires human review against the original source.

```text
N R I G B. C M Independent nursing interventions are tasks within the nursing scope of practice that the nurse may undertake without a physician or PCP order. Repositioning a patient in bed, performing oral hygiene, and providing emotional support through active listening are ex…
```

### 18. PFQ-fundamentals-000000208 — detached taxonomy word

- Question index: 208
- Severity: medium
- JSON path: `$.questions[207].rationale`
- Detail: Pattern requires human review against the original source.

```text
With the patient‘s permission, the nurse should share instructions with the people who may assist with care. Nurses empower patients and their support systems through effective teaching. When nurses provide patients and their families with opportunities to ask questions and comp…
```

### 19. PFQ-fundamentals-000000217 — possible split suffix

- Question index: 217
- Severity: medium
- JSON path: `$.questions[216].rationale`
- Detail: Pattern requires human review against the original source.

```text
Evaluation is the final step in the nursing process. Evaluation focuses on the patient and the patient‘s response to n ur singNi nUt eRrv eInt ioGn s aBnd.oCutcMome attainment. Evaluation is not a record of care that was implemented. Patient outcomes serve as the criteria agains…
```

### 20. PFQ-fundamentals-000000250 — possible broken web text

- Question index: 250
- Severity: high
- JSON path: `$.questions[249].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Deontology is an ethical theory that stresses the rightness or wrongness of individual behaviors, duties, and obligations without concern for the consequences of specific actions. Meeting the needs of patients while maintaining their right to privacy, confidentiality, …
```

### 21. PFQ-fundamentals-000000274 — possible broken web text

- Question index: 274
- Severity: high
- JSON path: `$.questions[273].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse knows which law protects health care professionals from charges of negligence when providing emergency care at the scene of an accident? U S N
```

### 22. PFQ-fundamentals-000000277 — possible broken web text

- Question index: 277
- Severity: high
- JSON path: `$.questions[276].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The Uniform Anatomical Gift Act GB.CM U S N T O
```

### 23. PFQ-fundamentals-000000280 — possible broken web text

- Question index: 280
- Severity: high
- JSON path: `$.questions[279].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Transformational U S N
```

### 24. PFQ-fundamentals-000000281 — possible split suffix

- Question index: 281
- Severity: medium
- JSON path: `$.questions[280].rationale`
- Detail: Pattern requires human review against the original source.

```text
Transactional leaders use reward and punishment to gain the cooperation of follow ers. Transformational leaders use methods that inspire people to follow their lead. Transformational leaders work toward transforming an organization with the help of others. The authoritarian or a…
```

### 25. PFQ-fundamentals-000000294 — possible broken web text

- Question index: 294
- Severity: high
- JSON path: `$.questions[293].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Assistance with eating breakfast U S N
```

### 26. PFQ-fundamentals-000000303 — NURSINGTB contamination

- Question index: 303
- Severity: high
- JSON path: `$.questions[302].stem`
- Detail: Known source or extraction contamination detected.

```text
The American Nurses Association (ANA) standards of professional performance require nurses to use research findings in practice. How do these standards impact nurses in the workplace? NURSINGTB.CO
```

### 27. PFQ-fundamentals-000000309 — possible broken web text

- Question index: 309
- Severity: high
- JSON path: `$.questions[308].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Address ethical procedures. U S N
```

### 28. PFQ-fundamentals-000000332 — possible split suffix

- Question index: 332
- Severity: medium
- JSON path: `$.questions[331].rationale`
- Detail: Pattern requires human review against the original source.

```text
Formal patient education is delivered throughout the community in the form of media, in a variety of educational and group settings, or in a planned, goal-directed, one-on-one session with a patient in the acute care setting. Informal education is usually learner or patient dire…
```

### 29. PFQ-fundamentals-000000338 — possible split suffix

- Question index: 338
- Severity: medium
- JSON path: `$.questions[337].rationale`
- Detail: Pattern requires human review against the original source.

```text
Teaching should be tailored to elderly patients. Reports indicate that two-thirds of U.S. adults 66 years old and older have inadequate or marginal literacy skills, and 81% of patients 60 years old and older at a public hospital could not read or understand basic materials such …
```

### 30. PFQ-fundamentals-000000362 — detached taxonomy word

- Question index: 362
- Severity: medium
- JSON path: `$.questions[361].rationale`
- Detail: Pattern requires human review against the original source.

```text
Descriptions of nursing informatics competencies often focus on levels that include beginner, experienced, specialist, and innovator. Beginner skills include computer, information, and web literacy; fundamental skills in information management and computer technology; and the ab…
```

### 31. PFQ-fundamentals-000000363 — possible broken web text

- Question index: 363
- Severity: high
- JSON path: `$.questions[362].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Technical competencies N R I G B.C M
```

### 32. PFQ-fundamentals-000000377 — detached taxonomy word

- Question index: 377
- Severity: medium
- JSON path: `$.questions[376].rationale`
- Detail: Pattern requires human review against the original source.

```text
In the three primary components of the Health Belief Model, six main constructs influence an individual‘s decision to take action about disease prevention, screening, and controlling illness. The model suggests that individuals are motivated to take action if they believe that t…
```

### 33. PFQ-fundamentals-000000390 — possible broken web text

- Question index: 390
- Severity: high
- JSON path: `$.questions[389].rationale`
- Detail: Pattern requires human review against the original source.

```text
The genetic vulnerability of an organism, or risk of disease expression based on genotype, is involuntarily passed from biologic parents to their offspring. Societal attitudes about testing and management of high-risk populations depend on the potential for expression of genetic…
```

### 34. PFQ-fundamentals-000000412 — possible broken web text

- Question index: 412
- Severity: high
- JSON path: `$.questions[411].stem`
- Detail: Pattern requires human review against the original source.

```text
A father expresses frustration that his school-aged child is suddenly ―sick all the time.‖ What action by the nurse is best? U S N
```

### 35. PFQ-fundamentals-000000413 — detached taxonomy word

- Question index: 413
- Severity: medium
- JSON path: `$.questions[412].rationale`
- Detail: Pattern requires human review against the original source.

```text
School-aged children benefit from simple explanations they can understand. Just telling the child not to worry is dismissive of the child‘s concerns. A school-aged child may not be able to read and/or understand a written pamphlet. Using phrases such as ―put you to sleep‖ should…
```

### 36. PFQ-fundamentals-000000416 — possible split suffix

- Question index: 416
- Severity: medium
- JSON path: `$.questions[415].rationale`
- Detail: Pattern requires human review against the original source.

```text
A 3-month-old child should be able to follow a moving object with his or h er eyes. However, one single abnormal assessment finding does not necessarily mean that the child has a growt h and developmental delay. The nurse should assess for other age-appropriate behaviors. Docume…
```

### 37. PFQ-fundamentals-000000417 — possible broken web text

- Question index: 417
- Severity: high
- JSON path: `$.questions[416].rationale`
- Detail: Pattern requires human review against the original source.

```text
Throwing an object down to watch someone else pick it up is a typical be havior for this age- group. The nurse should teach the parent about how this behavior relates to toddler gro wth and development. The other actions are not appropriate in this situation. U S N T O NCLEX Cli…
```

### 38. PFQ-fundamentals-000000420 — possible broken web text

- Question index: 420
- Severity: high
- JSON path: `$.questions[419].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Weight loss and malnutrition N R I G
```

### 39. PFQ-fundamentals-000000439 — possible broken web text

- Question index: 439
- Severity: high
- JSON path: `$.questions[438].stem`
- Detail: Pattern requires human review against the original source.

```text
A nurse notes an older adult puts excessive amounts of salt on her food. What intervention by the nurse is best? NUR ISG BN.CTM O
```

### 40. PFQ-fundamentals-000000441 — possible broken web text

- Question index: 441
- Severity: high
- JSON path: `$.questions[440].rationale`
- Detail: Pattern requires human review against the original source.

```text
Abuse of illicit drugs can cause many symptoms, including panic attacks and aggressive behavior. After assessing for an infectious process, the nurse should determine if the patient has used any recreational drugs. The other assessments are not as important and can be completed …
```

### 41. PFQ-fundamentals-000000453 — possible broken web text

- Question index: 453
- Severity: high
- JSON path: `$.questions[452].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Student pulls the pinna of the patient‘s ear up and back. U S N T
```

### 42. PFQ-fundamentals-000000461 — detached taxonomy word

- Question index: 461
- Severity: medium
- JSON path: `$.questions[460].rationale`
- Detail: Pattern requires human review against the original source.

```text
This patient has orthostatic hypotension, which is a drop of 20 mm Hg in systolic reading and 10 mm Hg in diastolic readinNg wRh e nIt h eGp atBi e.n tCs t a nMd s up fr om a sitting or lying position. The patient‘s cardiovascular system does not compensate for this, so the pati…
```

### 43. PFQ-fundamentals-000000464 — possible broken web text

- Question index: 464
- Severity: high
- JSON path: `$.questions[463].rationale`
- Detail: Pattern requires human review against the original source.

```text
A pulse of 42 beats/min is considered bradycardia and the patient should be assessed first because perfusion could be cNo m pRr o mIi s eGd . TBhe.bClooMd pressure, pulse oximetry, and respiratory rate are normal. U S N T O
```

### 44. PFQ-fundamentals-000000488 — possible broken web text

- Question index: 488
- Severity: high
- JSON path: `$.questions[487].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Prepare to treat the patient for asthma. U S N
```

### 45. PFQ-fundamentals-000000489 — possible broken web text

- Question index: 489
- Severity: high
- JSON path: `$.questions[488].rationale`
- Detail: Pattern requires human review against the original source.

```text
Cranial nerve III (oculomotor nerve) is assessed by observing the patient‘s pupil size and reaction to light and the direction of gaze. Identifying a common scent would test cranial nerve I. Assessing the patient‘s visual acuity tests cranial nerve II. Assessing hearing is crani…
```

### 46. PFQ-fundamentals-000000492 — NURSINGTB contamination

- Question index: 492
- Severity: high
- JSON path: `$.questions[491].rationale`
- Detail: Known source or extraction contamination detected.

```text
During the interview process, the nurse needs to demonstrate interest in the patient by leaning slightly toward him/her, allowing requested family or friends to accompany the patient, and closing the door to the room to ensure privacy. Typing intently when the patient is talking…
```

### 47. PFQ-fundamentals-000000499 — possible broken web text

- Question index: 499
- Severity: high
- JSON path: `$.questions[498].stem`
- Detail: Pattern requires human review against the original source.

```text
A nursing student wants to obsNervRe enIcultGuratBio.n practices of an ethnic minority community. What action by the student is bUe s t ?S NT O
```

### 48. PFQ-fundamentals-000000504 — possible broken web text

- Question index: 504
- Severity: high
- JSON path: `$.questions[503].rationale`
- Detail: Pattern requires human review against the original source.

```text
Discrimination can occur at the societal level, so even though this nurse is not prejudiced, patients from ethnic and cultural minorities can still suffer from discrimination. The other answers do not explain how discrimination can occur. N R I GOBBJ:.2C1.2M
```

### 49. PFQ-fundamentals-000000511 — possible broken web text

- Question index: 511
- Severity: high
- JSON path: `$.questions[510].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Communication differences can lead to misunderstandings and possible medical errors. Many cultural groups have verbal and nonverbal communication patterns that differ from other groups. Variations can occur due to personal or social situations. The nurse should attempt…
```

### 50. PFQ-fundamentals-000000524 — possible broken web text

- Question index: 524
- Severity: high
- JSON path: `$.questions[523].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O There are many cues to alert the nurse that a patient might have unmet spiritual needs, including facing a terminal illness. The nurse should conduct spiritual assessments on all patients, but this one is the priority.
```

### 51. PFQ-fundamentals-000000532 — possible broken web text

- Question index: 532
- Severity: high
- JSON path: `$.questions[531].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Ask if the patient and family want to pray. U S N T
```

### 52. PFQ-fundamentals-000000536 — possible broken web text

- Question index: 536
- Severity: high
- JSON path: `$.questions[535].rationale`
- Detail: Pattern requires human review against the original source.

```text
Promoting connectedness means recognizing that family and friends are providing at least some of the patient‘s spiritual care. The nurse best assists when offering to call someone for the patient or family. The other options may be appropriate but are not directly related to con…
```

### 53. PFQ-fundamentals-000000540 — possible split suffix

- Question index: 540
- Severity: medium
- JSON path: `$.questions[539].rationale`
- Detail: Pattern requires human review against the original source.

```text
Spirituality focuses on the meanings of life, death, and existence. Religion is an organiz ed and structured method of practicing or expressing one‘s spirituality, so they are interconnected and not mutually exclusive. Religion provides the structure for expressing spiritua lity…
```

### 54. PFQ-fundamentals-000000542 — possible broken web text

- Question index: 542
- Severity: high
- JSON path: `$.questions[541].rationale`
- Detail: Pattern requires human review against the original source.

```text
Native American, Hindu, and Buddhist practitioners believe that health and illness are a matter of balance or imbalance in the body. M S C : N C L E X C l i e n t N e e d sC NategRor y:IPsyGchosBoi.caCl InMtegrity
```

### 55. PFQ-fundamentals-000000583 — possible split suffix

- Question index: 583
- Severity: medium
- JSON path: `$.questions[582].rationale`
- Detail: Pattern requires human review against the original source.

```text
The PLISSIT model is a framework for addressing sexuality. In the SS (specific suggestions) phase, the nurse provides information that allows the patient to proceed with sexual relation s. Informing the patient about sNexUuRalSpIosNitiGoTnsBth.aCt aOr eMl e s s stressful on the …
```

### 56. PFQ-fundamentals-000000587 — detached taxonomy word

- Question index: 587
- Severity: medium
- JSON path: `$.questions[586].rationale`
- Detail: Pattern requires human review against the original source.

```text
Ineffective sexuality patterns refer to a patient who expresses concern about his/her own sexuality. This patient is concerned about the effect of this surgery on his/her attractiveness and desirability. Sexual dysfunction relates more to the physical problems. The patient may h…
```

### 57. PFQ-fundamentals-000000617 — possible broken web text

- Question index: 617
- Severity: high
- JSON path: `$.questions[616].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Apply restraints. S N T O
```

### 58. PFQ-fundamentals-000000622 — possible broken web text

- Question index: 622
- Severity: high
- JSON path: `$.questions[621].rationale`
- Detail: Pattern requires human review against the original source.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 59. PFQ-fundamentals-000000624 — possible broken web text

- Question index: 624
- Severity: high
- JSON path: `$.questions[623].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Humoral immunity is a defense system that involves antibodies and white blood cells that are produced to fight antigens. Cellular immunity involves defense by white blood cells against any microorganisms that the body does not recognize as its own. The innate (nonspeci…
```

### 60. PFQ-fundamentals-000000631 — possible broken web text

- Question index: 631
- Severity: high
- JSON path: `$.questions[630].rationale`
- Detail: Pattern requires human review against the original source.

```text
The 80-year-old male has more risk factors because he is elderly and has increased risk of urinary tract infection related to prostate enlargement, so he has two risk factors. A 24-year-old female runner is likely healthy with no additional risk factors. The 50-year-old obese ma…
```

### 61. PFQ-fundamentals-000000636 — possible broken web text

- Question index: 636
- Severity: high
- JSON path: `$.questions[635].rationale`
- Detail: Pattern requires human review against the original source.

```text
Soap and water must be used to thoroughly clean hands if there is any visible soiling or dirt and with certain infections such as Clostridium difficile and vancomycin-resistant enterococci when preparing for a sterile or surgical procedure, before and after eating, and after usi…
```

### 62. PFQ-fundamentals-000000639 — possible split suffix

- Question index: 639
- Severity: medium
- JSON path: `$.questions[638].rationale`
- Detail: Pattern requires human review against the original source.

```text
Droplet precautions are used when known or suspected contagious diseases can be transmitted through large droplets suspenNdedRin It h e GaUi r. SBCo.nCtNactMprecaution s are used when a known orsuspected contagious disease may be present and is transmitted through direct contact…
```

### 63. PFQ-fundamentals-000000670 — possible broken web text

- Question index: 670
- Severity: high
- JSON path: `$.questions[669].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Patients with diabetes U S N
```

### 64. PFQ-fundamentals-000000670 — possible split suffix

- Question index: 670
- Severity: medium
- JSON path: `$.questions[669].rationale`
- Detail: Pattern requires human review against the original source.

```text
Soaking the feet of patients with peripheral vascular disease, cardiovascular disease s uch as strokes and diabetes are contraindicated because it may cause skin breakdown or inf ection. Patient with arthritis or malnourished have no contraindications to having their feet soaked.
```

### 65. PFQ-fundamentals-000000673 — possible split suffix

- Question index: 673
- Severity: medium
- JSON path: `$.questions[672].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
The patient is wearing s oc kUs. SNT O
```

### 66. PFQ-fundamentals-000000693 — possible split suffix

- Question index: 693
- Severity: medium
- JSON path: `$.questions[692].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The nurse stands behind tNheUpRaStinIeNt wGhTilBe .a mCbOuMlat ing.
```

### 67. PFQ-fundamentals-000000706 — possible broken web text

- Question index: 706
- Severity: high
- JSON path: `$.questions[705].rationale`
- Detail: Pattern requires human review against the original source.

```text
Occlusive dressings such as hydrocolloids and transparent films are used for autolytic debridement and are contraindicated in infected wounds. It is the most comfortable form of debridement for the patient. Nty R IGB.CM U S N T O
```

### 68. PFQ-fundamentals-000000727 — possible broken web text

- Question index: 727
- Severity: high
- JSON path: `$.questions[726].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is performing an oral examination on a patient and notices a beefy-red tongue. The nurse identifies this as a characteristic finding for what condition? U S N
```

### 69. PFQ-fundamentals-000000730 — possible broken web text

- Question index: 730
- Severity: high
- JSON path: `$.questions[729].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
―I can give the patient orange juice.‖ U S N
```

### 70. PFQ-fundamentals-000000733 — possible broken web text

- Question index: 733
- Severity: high
- JSON path: `$.questions[732].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Flushes the tube with a small amount of air. U S N
```

### 71. PFQ-fundamentals-000000749 — possible broken web text

- Question index: 749
- Severity: high
- JSON path: `$.questions[748].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O The frontal lobes of the cerebrum are the areas of the brain responsible for voluntary motor function, concentration, communication, decision making, and personality. The parietal lobes are responsible for the sense of touch, distinguishing the shape and texture of obj…
```

### 72. PFQ-fundamentals-000000766 — possible broken web text

- Question index: 766
- Severity: high
- JSON path: `$.questions[765].rationale`
- Detail: Pattern requires human review against the original source.

```text
Balance, eyesight, hearing, and sensation are all sensory function. Asking if the patient likes the newspaper does not specifically address vision. M S C : NC L E X C l i e n t Nee d s CNa tegRor y:IP hyGs i o lBo g.i cCa l InMtegrity
```

### 73. PFQ-fundamentals-000000776 — detached taxonomy word

- Question index: 776
- Severity: medium
- JSON path: `$.questions[775].rationale`
- Detail: Pattern requires human review against the original source.

```text
The endocrine system responds to stress on the body such as what happens during an acute MI. Corticosteroids are important in the stress response because they increase serum glucose levels and inhibit the inflammatory response. Although MIs can be seen in diabetics, there is not…
```

### 74. PFQ-fundamentals-000000778 — possible broken web text

- Question index: 778
- Severity: high
- JSON path: `$.questions[777].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Eat a diet with lots of fiber. U S N T O
```

### 75. PFQ-fundamentals-000000778 — detached taxonomy word

- Question index: 778
- Severity: medium
- JSON path: `$.questions[777].rationale`
- Detail: Pattern requires human review against the original source.

```text
High stress levels are known to exacerbate multiple sclerosis and other autoimmune diseases. Exercise helps keep muscles loose and helps with balance. Assessing skin for pressure sores and eating a diet with high fiber prevents complications from multiple sclerosis. Analyzing
```

### 76. PFQ-fundamentals-000000780 — possible broken web text

- Question index: 780
- Severity: high
- JSON path: `$.questions[779].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Blood pressure of 120/84N R I G B.C M
```

### 77. PFQ-fundamentals-000000792 — possible split suffix

- Question index: 792
- Severity: medium
- JSON path: `$.questions[791].rationale`
- Detail: Pattern requires human review against the original source.

```text
The release of hormones increases the heart rate, resulting in increased cardiac output, and elevated blood pressure. TheNre isRanIi n c rGeUa s eBSi.n Ct h e Mf low of blood to muscles at the expense ofthe digestive and other systems not immediately needed in the fight-or-fligh…
```

### 78. PFQ-fundamentals-000000815 — possible broken web text

- Question index: 815
- Severity: high
- JSON path: `$.questions[814].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Slow rhythmic scanning eye movements U S N
```

### 79. PFQ-fundamentals-000000824 — repeated word

- Question index: 824
- Severity: medium
- JSON path: `$.questions[823].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for an elderly patient with dementia. Which laboratory finding indicates to the nurse that that patient is often forgetting to eat meals?
```

### 80. PFQ-fundamentals-000000825 — possible broken web text

- Question index: 825
- Severity: high
- JSON path: `$.questions[824].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Prothrombin time (PT) 11.5 sec U S N
```

### 81. PFQ-fundamentals-000000832 — possible broken web text

- Question index: 832
- Severity: high
- JSON path: `$.questions[831].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Shrimp and scallops U S N T O
```

### 82. PFQ-fundamentals-000000843 — possible broken web text

- Question index: 843
- Severity: high
- JSON path: `$.questions[842].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
White blood cell count (WNBCR) 4I5U0 0G/Sm mNB3.CT M O
```

### 83. PFQ-fundamentals-000000843 — possible split suffix

- Question index: 843
- Severity: medium
- JSON path: `$.questions[842].rationale`
- Detail: Pattern requires human review against the original source.

```text
Red blood cell count of 5.8 million and hemoglobin value of 14 g/dL are both norm al. Hematocrit level of 25% is very low and indicative of ongoing anemia. White blood cell and platelet counts are not checked for anemia.
```

### 84. PFQ-fundamentals-000000910 — possible split suffix

- Question index: 910
- Severity: medium
- JSON path: `$.questions[909].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient must take in a deep breath while holding the spirometer to the mouth s o that the device can indicate how much air is being inhaled into the lungs. The remaining responses are correct components of the procedure.
```

### 85. PFQ-fundamentals-000000932 — possible split suffix

- Question index: 932
- Severity: medium
- JSON path: `$.questions[931].rationale`
- Detail: Pattern requires human review against the original source.

```text
Hemodilution is a common finding when patients are in fluid overload caused by congestive heart failure. A normal hematocrit result is 42% to 52% for a male and 37% to 47% for a female, so the patient‘s 32% Nhe mRat oIcrit Gl eveBl .isCm arMked ly low. The other laboratory resul…
```

### 86. PFQ-fundamentals-000000941 — possible split suffix

- Question index: 941
- Severity: medium
- JSON path: `$.questions[940].rationale`
- Detail: Pattern requires human review against the original source.

```text
Only the inner cannula of the tracheostomy is removed for cleaning. The outer cannul a stays in the trachea to maintain airway patency. Clean gloves are applied before the soiled dress ing is removed. Normal sterile saline is used to remove secretions that have built u p on the …
```

### 87. PFQ-fundamentals-000000944 — possible broken web text

- Question index: 944
- Severity: high
- JSON path: `$.questions[943].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the patient‘s laboratory results. Which result must be communicated to t hephysician immediately? a . Serumchloride level 85 m E qN/ L R I GB.CM
```

### 88. PFQ-fundamentals-000000944 — possible broken web text

- Question index: 944
- Severity: high
- JSON path: `$.questions[943].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Serum sodium level 134 m UE q / LS NT O
```

### 89. PFQ-fundamentals-000000963 — possible split suffix

- Question index: 963
- Severity: medium
- JSON path: `$.questions[962].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
―These medications will iNn c rRea s eIyo Gu r uBr i n.eCo u tMp u t until your kidneys recover.‖
```

### 90. PFQ-fundamentals-000001004 — possible split suffix

- Question index: 1004
- Severity: medium
- JSON path: `$.questions[1003].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient has acute urinary retention with overflow as evidenced by 1100 mL of urine in the bladder and frequent passage of small amounts of urine. The priority nursing diagnosi s is thus Impaired urination r/t obstruction of urinary bladder outlet. Urinary retention is the ca…
```

### 91. PFQ-fundamentals-000001017 — possible split suffix

- Question index: 1017
- Severity: medium
- JSON path: `$.questions[1016].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a terminally ill patient whose children have come home to be with their mother during her last few days. They spend time looking through picture albums, watching old home movi es , and r eme mNbUe rRi nSg If uNn Gt iTmBe s.s pCeOn tMto ge th er. The nur s…
```
