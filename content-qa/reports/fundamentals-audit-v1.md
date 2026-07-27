# Fundamentals Pack QA Audit

> Read-only scan. The original Pack was not modified.

## Summary

- Pack: `packs/fundamentals.prepflow.json`
- Questions scanned: **1040**
- Text fields scanned: **15577**
- Questions with findings: **1035**
- Total findings: **1807**

### Findings by severity

- high: 1644
- medium: 163

### Findings by category

- Contamination: 109
- Structure: 9
- Text: 1689

### Findings by rule

- abrupt ending: 1473
- multiple spaces: 70
- test-bank metadata: 66
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

### 1. PFQ-fundamentals-000000001 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[0].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 2. PFQ-fundamentals-000000001 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 1
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[0].rationale`
- Detail: Pattern requires human review against the original source.

```text
Maslow‘s hierarchy of needs specifies the psychological and physiologic factors that affect each person‘s physical and mental health. The nurse‘s understanding of these factors helps with formulating Nursing diagnoses that address the patient‘s needs and values to prioritize car…
```

### 3. PFQ-fundamentals-000000002 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 2
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[1].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 4. PFQ-fundamentals-000000002 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 2
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[1].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 5. PFQ-fundamentals-000000003 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 3
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[2].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 6. PFQ-fundamentals-000000004 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 4
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[3].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 7. PFQ-fundamentals-000000004 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 4
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[3].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 8. PFQ-fundamentals-000000004 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 4
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[3].rationale`
- Detail: Pattern requires human review against the original source.

```text
The Institute of Medicine r e pNo r t ,RH eIa l thGP r oBf e.s sCi o nMs Education: A Bridge to Quality (2003),outlines five core competencies. These include patient-centered care, interdisciplinary teamwork, use of evidence-based medicine, quality improvement, and use of inform…
```

### 9. PFQ-fundamentals-000000005 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 5
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[4].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 10. PFQ-fundamentals-000000005 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 5
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[4].choices[0].text`
- Detail: Known source or extraction contamination detected.

```text
They graduate and pass NCLEX.
```

### 11. PFQ-fundamentals-000000005 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 5
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[4].rationale`
- Detail: Known source or extraction contamination detected.

```text
Benner‘s model identifies five levels of proficiency: novice, advanced beginner, competent, proficient, and expert. The student nurse progresses from novice to advanced beginner during nursing school and attains the competent level after approximately 2 to 3 years of work experi…
```

### 12. PFQ-fundamentals-000000006 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 6
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[5].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 13. PFQ-fundamentals-000000007 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 7
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[6].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 14. PFQ-fundamentals-000000008 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 8
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[7].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 15. PFQ-fundamentals-000000009 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 9
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[8].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 16. PFQ-fundamentals-000000009 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 9
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[8].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 17. PFQ-fundamentals-000000010 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 10
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[9].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 18. PFQ-fundamentals-000000011 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 11
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[10].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 19. PFQ-fundamentals-000000011 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 11
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[10].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Expect that the patient may return to the hospital if the discharge process is poorly done. NUR ISG BN.CTM O
```

### 20. PFQ-fundamentals-000000012 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 12
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[11].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 21. PFQ-fundamentals-000000013 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 13
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[12].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 22. PFQ-fundamentals-000000013 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 13
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[12].rationale`
- Detail: Known source or extraction contamination detected.

```text
Hildegard Peplau focused on the roles played by the nurse and the interpersonal process between a nurse and a patient. The interpersonal process occurs in overlapping phases: (1) orientation, (2) working, consisting of two subphases: identification and exploitation, and (3) reso…
```

### 23. PFQ-fundamentals-000000014 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 14
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[13].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 24. PFQ-fundamentals-000000014 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 14
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[13].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 25. PFQ-fundamentals-000000015 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 15
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[14].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 26. PFQ-fundamentals-000000016 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 16
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[15].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 27. PFQ-fundamentals-000000016 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 16
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[15].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 28. PFQ-fundamentals-000000017 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 17
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[16].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 29. PFQ-fundamentals-000000018 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 18
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[17].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 30. PFQ-fundamentals-000000019 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 19
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[18].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 31. PFQ-fundamentals-000000019 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 19
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[18].rationale`
- Detail: Known source or extraction contamination detected.

```text
LPNs, or LVNs in California and Texas, are not RNs. They complete an educational program consisting of 12 to 18 months of training, and then they must pass the National Council Licensure Examination for Practical Nurses (NCLEX-PN) to practice as an LPN/LVN. They are under the su…
```

### 32. PFQ-fundamentals-000000020 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 20
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[19].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 33. PFQ-fundamentals-000000020 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 20
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[19].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 34. PFQ-fundamentals-000000021 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 21
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[20].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 35. PFQ-fundamentals-000000021 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 21
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[20].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 36. PFQ-fundamentals-000000022 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 22
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[21].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 37. PFQ-fundamentals-000000022 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 22
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[21].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 38. PFQ-fundamentals-000000023 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 23
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[22].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 39. PFQ-fundamentals-000000023 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 23
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[22].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 40. PFQ-fundamentals-000000024 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 24
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[23].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["A", "B", "C", "D", "B", "C"]
```

### 41. PFQ-fundamentals-000000024 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 24
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[23].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 42. PFQ-fundamentals-000000024 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 24
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[23].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 43. PFQ-fundamentals-000000025 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 25
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[24].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 44. PFQ-fundamentals-000000025 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 25
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[24].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 45. PFQ-fundamentals-000000025 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 25
- Chapter: Nursing, Theory, and Professional Practice
- JSON path: `$.questions[24].rationale`
- Detail: Known source or extraction contamination detected.

```text
The process of using evidence-based practice (EBP) starts with the identification of a problem. The nurse then conducts a literature search to find the best evidence pertaining to the problem. Facility resources may impact the ability to implement the chosen decision. Patient pr…
```

### 46. PFQ-fundamentals-000000026 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 26
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[25].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 47. PFQ-fundamentals-000000026 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 26
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[25].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 48. PFQ-fundamentals-000000027 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 27
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[26].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 49. PFQ-fundamentals-000000028 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 28
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[27].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 50. PFQ-fundamentals-000000028 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 28
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[27].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 51. PFQ-fundamentals-000000029 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 29
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[28].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 52. PFQ-fundamentals-000000030 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 30
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[29].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 53. PFQ-fundamentals-000000031 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 31
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[30].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 54. PFQ-fundamentals-000000032 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 32
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[31].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 55. PFQ-fundamentals-000000032 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 32
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[31].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 56. PFQ-fundamentals-000000033 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 33
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[32].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 57. PFQ-fundamentals-000000034 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 34
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[33].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 58. PFQ-fundamentals-000000035 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 35
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[34].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 59. PFQ-fundamentals-000000035 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 35
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[34].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Doing for
```

### 60. PFQ-fundamentals-000000035 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 35
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[34].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Being with
```

### 61. PFQ-fundamentals-000000035 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 35
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[34].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 62. PFQ-fundamentals-000000036 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 36
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[35].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 63. PFQ-fundamentals-000000036 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 36
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[35].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 64. PFQ-fundamentals-000000037 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 37
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[36].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 65. PFQ-fundamentals-000000037 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 37
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[36].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 66. PFQ-fundamentals-000000038 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 38
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[37].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 67. PFQ-fundamentals-000000038 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 38
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[37].rationale`
- Detail: Pattern requires human review against the original source.

```text
Values clarification is a process used to help people reflect on, clarify, and prioritize personal values to increase self-awareness or to make decisions. Nurses can use values clari fication to help patients identify the nature of a conflict and reach a decision based on their …
```

### 68. PFQ-fundamentals-000000039 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 39
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[38].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 69. PFQ-fundamentals-000000039 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 39
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[38].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 70. PFQ-fundamentals-000000040 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 40
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[39].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 71. PFQ-fundamentals-000000041 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 41
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[40].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 72. PFQ-fundamentals-000000042 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 42
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[41].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 73. PFQ-fundamentals-000000042 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 42
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[41].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 74. PFQ-fundamentals-000000043 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 43
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[42].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 75. PFQ-fundamentals-000000044 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 44
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[43].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 76. PFQ-fundamentals-000000044 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 44
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[43].rationale`
- Detail: Known source or extraction contamination detected.

```text
Swanson‘s Theory of Caring is composed of five interrelated caring processes: having faith in the ability of others to have meaningful lives; striving to understand the meaning of events in other‘s lives; being emotionally present to the other person; doing for others what the y…
```

### 77. PFQ-fundamentals-000000044 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 44
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[43].rationale`
- Detail: Pattern requires human review against the original source.

```text
Swanson‘s Theory of Caring is composed of five interrelated caring processes: having faith in the ability of others to have meaningful lives; striving to understand the meaning of events in other‘s lives; being emotionally present to the other person; doing for others what the y…
```

### 78. PFQ-fundamentals-000000045 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 45
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[44].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 79. PFQ-fundamentals-000000045 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 45
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[44].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 80. PFQ-fundamentals-000000046 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 46
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[45].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 81. PFQ-fundamentals-000000046 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 46
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[45].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 82. PFQ-fundamentals-000000046 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 46
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[45].rationale`
- Detail: Pattern requires human review against the original source.

```text
First-order beliefs serve as the foundation or the basis of an individual‘s belief system. People begin developing first-order beliefs about what is correct, real, and true in early childhood directly through experiences NandRUindIiSrecGtNl y fBr o.mCi n fMo rm a t i o n shared …
```

### 83. PFQ-fundamentals-000000047 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 47
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[46].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 84. PFQ-fundamentals-000000047 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 47
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[46].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 85. PFQ-fundamentals-000000048 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 48
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[47].stem`
- Detail: Pattern requires human review against the original source.

```text
Caring, according to the American Nurses Association (ANA) Code of Ethics (2 015), is having concern or regard for that which affects the welfare of another. The nurse recognizes that as a profession, nursing can trace its earliest beginnings to what types of nurturing activitie…
```

### 86. PFQ-fundamentals-000000048 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 48
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[47].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 87. PFQ-fundamentals-000000048 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 48
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[47].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 88. PFQ-fundamentals-000000049 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 49
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[48].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 89. PFQ-fundamentals-000000050 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 50
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[49].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 90. PFQ-fundamentals-000000050 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 50
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[49].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 91. PFQ-fundamentals-000000050 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 50
- Chapter: Values, Beliefs, and Caring
- JSON path: `$.questions[49].rationale`
- Detail: Known source or extraction contamination detected.

```text
Compassion fatigue is an extreme state of distress experienced as the progressive and cumulative result of exposure to stress in the therapeutic use of self in caring for others. Compassion fatigue involves the nurse experiencing a feeling of being unable to meet the needs of pa…
```

### 92. PFQ-fundamentals-000000051 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 51
- Chapter: Communication
- JSON path: `$.questions[50].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 93. PFQ-fundamentals-000000052 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 52
- Chapter: Communication
- JSON path: `$.questions[51].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 94. PFQ-fundamentals-000000052 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 52
- Chapter: Communication
- JSON path: `$.questions[51].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 95. PFQ-fundamentals-000000053 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 53
- Chapter: Communication
- JSON path: `$.questions[52].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 96. PFQ-fundamentals-000000054 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 54
- Chapter: Communication
- JSON path: `$.questions[53].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 97. PFQ-fundamentals-000000055 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 55
- Chapter: Communication
- JSON path: `$.questions[54].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 98. PFQ-fundamentals-000000056 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 56
- Chapter: Communication
- JSON path: `$.questions[55].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 99. PFQ-fundamentals-000000057 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 57
- Chapter: Communication
- JSON path: `$.questions[56].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 100. PFQ-fundamentals-000000058 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 58
- Chapter: Communication
- JSON path: `$.questions[57].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 101. PFQ-fundamentals-000000059 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 59
- Chapter: Communication
- JSON path: `$.questions[58].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 102. PFQ-fundamentals-000000061 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 61
- Chapter: Communication
- JSON path: `$.questions[60].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 103. PFQ-fundamentals-000000061 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 61
- Chapter: Communication
- JSON path: `$.questions[60].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Therapeutic touch, such as holding the patient‘s hand or touching the patient‘s shoulder, can provide comfort and may alleviate pain. This is especially true when a patient is undergoing a painful or stressful procedure. Making inappropriate facial expressions may be o…
```

### 104. PFQ-fundamentals-000000062 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 62
- Chapter: Communication
- JSON path: `$.questions[61].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 105. PFQ-fundamentals-000000062 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 62
- Chapter: Communication
- JSON path: `$.questions[61].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 106. PFQ-fundamentals-000000063 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 63
- Chapter: Communication
- JSON path: `$.questions[62].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 107. PFQ-fundamentals-000000063 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 63
- Chapter: Communication
- JSON path: `$.questions[62].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 108. PFQ-fundamentals-000000064 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 64
- Chapter: Communication
- JSON path: `$.questions[63].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 109. PFQ-fundamentals-000000064 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 64
- Chapter: Communication
- JSON path: `$.questions[63].rationale`
- Detail: Pattern requires human review against the original source.

```text
The ―B‖ in SBAR stands for ―Background,‖ or what led up to the current situation. The ―S‖ stands for Situation or what is happening right now. The ―A‖ stands for ―Assessment,‖ or what is the identified problem, concern, or need. The ―R‖ stands for ―Recommendation,‖ or what actio…
```

### 110. PFQ-fundamentals-000000065 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 65
- Chapter: Communication
- JSON path: `$.questions[64].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 111. PFQ-fundamentals-000000065 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 65
- Chapter: Communication
- JSON path: `$.questions[64].rationale`
- Detail: Known source or extraction contamination detected.

```text
In the working phase, there is the development of a contract or plan of care to achieve identified patient goals; implementation of the care plan or contract; collaborative work among the nurse, patient, and other health care providers, as needed; enhancement of trust and rappor…
```

### 112. PFQ-fundamentals-000000066 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 66
- Chapter: Communication
- JSON path: `$.questions[65].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 113. PFQ-fundamentals-000000067 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 67
- Chapter: Communication
- JSON path: `$.questions[66].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 114. PFQ-fundamentals-000000068 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 68
- Chapter: Communication
- JSON path: `$.questions[67].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who is unable to take oral medication s because of persistent nausea and vomiting. When the nurse decides to call the primary care physician and as k for a different medication administration route, this is a demonstration of what act?
```

### 115. PFQ-fundamentals-000000068 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 68
- Chapter: Communication
- JSON path: `$.questions[67].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 116. PFQ-fundamentals-000000069 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 69
- Chapter: Communication
- JSON path: `$.questions[68].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 117. PFQ-fundamentals-000000069 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 69
- Chapter: Communication
- JSON path: `$.questions[68].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 118. PFQ-fundamentals-000000070 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 70
- Chapter: Communication
- JSON path: `$.questions[69].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 119. PFQ-fundamentals-000000070 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 70
- Chapter: Communication
- JSON path: `$.questions[69].rationale`
- Detail: Pattern requires human review against the original source.

```text
The primary source from which data are collected is the patient. A secondary source would include a significant other, family members, caregivers, other members of the health team, and medical records.
```

### 120. PFQ-fundamentals-000000071 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 71
- Chapter: Communication
- JSON path: `$.questions[70].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 121. PFQ-fundamentals-000000072 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 72
- Chapter: Communication
- JSON path: `$.questions[71].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 122. PFQ-fundamentals-000000073 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 73
- Chapter: Communication
- JSON path: `$.questions[72].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 123. PFQ-fundamentals-000000073 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 73
- Chapter: Communication
- JSON path: `$.questions[72].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Tearing down boundariesNR I G B.C M
```

### 124. PFQ-fundamentals-000000073 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 73
- Chapter: Communication
- JSON path: `$.questions[72].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 125. PFQ-fundamentals-000000074 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 74
- Chapter: Communication
- JSON path: `$.questions[73].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 126. PFQ-fundamentals-000000074 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 74
- Chapter: Communication
- JSON path: `$.questions[73].rationale`
- Detail: Pattern requires human review against the original source.

```text
N R I G B When communicating with a hearing-impaired patient, the nurse should make sure that the area is well lit with as little background noise as possible. Hearing aids amplify all sounds, making noisy environments confusing and frustrating. Raising the voice level slightly,…
```

### 127. PFQ-fundamentals-000000075 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 75
- Chapter: Communication
- JSON path: `$.questions[74].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 128. PFQ-fundamentals-000000075 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 75
- Chapter: Communication
- JSON path: `$.questions[74].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 129. PFQ-fundamentals-000000075 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 75
- Chapter: Communication
- JSON path: `$.questions[74].rationale`
- Detail: Known source or extraction contamination detected.

```text
Providing a backrub is considered therapeutic touch; additional examples include holding a patient‘s hand and gently touching a patient‘s arm. Silence refers to being present with a patient without verbal communication. Facing the patient and refraining from unusual body movemen…
```

### 130. PFQ-fundamentals-000000076 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 76
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[75].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 131. PFQ-fundamentals-000000076 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 76
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[75].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 132. PFQ-fundamentals-000000077 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 77
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[76].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the last 3 days of a patient‘s pain history and notes that the pain level has remained constant. The nurse validates the pain level with the patient and decides to contact the provider for furthNerUoRrdSerIs.NInGtThBis .s cCe nOa r i o , which process is t…
```

### 133. PFQ-fundamentals-000000077 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 77
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[76].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 134. PFQ-fundamentals-000000078 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 78
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[77].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 135. PFQ-fundamentals-000000079 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 79
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[78].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 136. PFQ-fundamentals-000000079 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 79
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[78].rationale`
- Detail: Pattern requires human review against the original source.

```text
A role-play strategy involves assigning learners to different roles based on expected outcomes in a particular setting. Other learners and facilitators observe the role playing, and then all are involved in the debriefing or discussion of the scenario. As with simulation, this a…
```

### 137. PFQ-fundamentals-000000080 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 80
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[79].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 138. PFQ-fundamentals-000000081 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 81
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[80].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is preparing to restart a patient‘s intravenous line and discovers that the patient has no usable veins in either arm. When working to solve this problem, the nurse should carry out which action?
```

### 139. PFQ-fundamentals-000000081 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 81
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[80].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 140. PFQ-fundamentals-000000081 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 81
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[80].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 141. PFQ-fundamentals-000000082 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 82
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[81].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 142. PFQ-fundamentals-000000083 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 83
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[82].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 143. PFQ-fundamentals-000000083 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 83
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[82].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 144. PFQ-fundamentals-000000084 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 84
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[83].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 145. PFQ-fundamentals-000000085 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 85
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[84].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 146. PFQ-fundamentals-000000086 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 86
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[85].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 147. PFQ-fundamentals-000000087 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 87
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[86].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 148. PFQ-fundamentals-000000087 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 87
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[86].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 149. PFQ-fundamentals-000000088 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 88
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[87].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 150. PFQ-fundamentals-000000089 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 89
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[88].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 151. PFQ-fundamentals-000000090 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 90
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[89].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 152. PFQ-fundamentals-000000091 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 91
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[90].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 153. PFQ-fundamentals-000000091 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 91
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[90].choices[4].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 154. PFQ-fundamentals-000000091 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 91
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[90].rationale`
- Detail: Pattern requires human review against the original source.

```text
Decisions may be unduly influenced by bias, which is an inclination or tendency to favoritism or partiality. Bias may be related to a preconceived notion or prejudice such as believing that ―these people seek their medication.‖ It is important for nurses to examine personal bias…
```

### 155. PFQ-fundamentals-000000092 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 92
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[91].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 156. PFQ-fundamentals-000000093 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 93
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[92].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "B", "C"]
```

### 157. PFQ-fundamentals-000000093 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 93
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[92].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 158. PFQ-fundamentals-000000094 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 94
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[93].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 159. PFQ-fundamentals-000000095 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 95
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[94].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 160. PFQ-fundamentals-000000095 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 95
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[94].rationale`
- Detail: Pattern requires human review against the original source.

```text
Intuition is the feeling that you know something without specific evidence. Inferences are intellectual acts that involve a conclusion being made on the basis of something. The accuracy of an inference is directly related to the accuracy of what the inference is based on. Deduct…
```

### 161. PFQ-fundamentals-000000096 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 96
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[95].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 162. PFQ-fundamentals-000000096 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 96
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[95].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 163. PFQ-fundamentals-000000097 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 97
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[96].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 164. PFQ-fundamentals-000000097 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 97
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[96].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 165. PFQ-fundamentals-000000098 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 98
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[97].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 166. PFQ-fundamentals-000000098 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 98
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[97].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 167. PFQ-fundamentals-000000099 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 99
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[98].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 168. PFQ-fundamentals-000000099 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 99
- Chapter: Critical Thinking in Nursing
- JSON path: `$.questions[98].rationale`
- Detail: Known source or extraction contamination detected.

```text
Because nursing requires the application of knowledge to make clinical decisions and guide care, it involves active participation by the nurse. The application of knowledge requires development of a questioning attitude. This process is sometimes referred to as thinking like a n…
```

### 169. PFQ-fundamentals-000000100 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 100
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[99].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 170. PFQ-fundamentals-000000100 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 100
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[99].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 171. PFQ-fundamentals-000000100 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 100
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[99].rationale`
- Detail: Pattern requires human review against the original source.

```text
The nursing process is the foundation of professional nursing practice. It is the framework within which nurses provide care to patients in an organized and effective manner. Paul describes critical thinking as a complex process during which individuals think about their thinkin…
```

### 172. PFQ-fundamentals-000000101 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 101
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[100].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 173. PFQ-fundamentals-000000102 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 102
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[101].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 174. PFQ-fundamentals-000000103 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 103
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[102].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 175. PFQ-fundamentals-000000104 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 104
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[103].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 176. PFQ-fundamentals-000000105 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 105
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[104].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 177. PFQ-fundamentals-000000106 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 106
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[105].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 178. PFQ-fundamentals-000000107 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 107
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[106].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 179. PFQ-fundamentals-000000107 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 107
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[106].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 180. PFQ-fundamentals-000000108 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 108
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[107].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 181. PFQ-fundamentals-000000108 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 108
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[107].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 182. PFQ-fundamentals-000000109 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 109
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[108].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 183. PFQ-fundamentals-000000109 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 109
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[108].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 184. PFQ-fundamentals-000000110 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 110
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[109].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 185. PFQ-fundamentals-000000110 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 110
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[109].rationale`
- Detail: Pattern requires human review against the original source.

```text
A two-part risk, Nursing diagnostic statement contains only: (1) the patient‘s identified need or problem (i.e., NANDA-I Nursing diagnostic label) and (2) factors indicating vulnerability (i.e., risk factors). The risk factor is the history of stroke. The chest discomfort and sh…
```

### 186. PFQ-fundamentals-000000111 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 111
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[110].choices[1].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 187. PFQ-fundamentals-000000111 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 111
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[110].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 188. PFQ-fundamentals-000000112 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 112
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[111].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 189. PFQ-fundamentals-000000113 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 113
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[112].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 190. PFQ-fundamentals-000000113 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 113
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[112].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 191. PFQ-fundamentals-000000114 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 114
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[113].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 192. PFQ-fundamentals-000000115 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 115
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[114].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 193. PFQ-fundamentals-000000116 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 116
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[115].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 194. PFQ-fundamentals-000000117 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 117
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[116].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 195. PFQ-fundamentals-000000117 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 117
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[116].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 196. PFQ-fundamentals-000000118 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 118
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[117].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 197. PFQ-fundamentals-000000119 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 119
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[118].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 198. PFQ-fundamentals-000000120 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 120
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[119].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 199. PFQ-fundamentals-000000120 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 120
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[119].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 200. PFQ-fundamentals-000000121 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 121
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[120].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 201. PFQ-fundamentals-000000121 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 121
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[120].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 202. PFQ-fundamentals-000000122 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 122
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[121].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 203. PFQ-fundamentals-000000123 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 123
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[122].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 204. PFQ-fundamentals-000000123 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 123
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[122].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 205. PFQ-fundamentals-000000123 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 123
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[122].rationale`
- Detail: Pattern requires human review against the original source.

```text
The Nursing diagnosis identifies an actual or potential problem or response to a problem. Accurate identification of Nursing diagnoses for patients results from carefully analyzing, validating, and N R I G B. clustering relateUd pSatieNnt suTbje ctivOe (symptoms) and objective (…
```

### 206. PFQ-fundamentals-000000123 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 123
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[122].rationale`
- Detail: Pattern requires human review against the original source.

```text
The Nursing diagnosis identifies an actual or potential problem or response to a problem. Accurate identification of Nursing diagnoses for patients results from carefully analyzing, validating, and N R I G B. clustering relateUd pSatieNnt suTbje ctivOe (symptoms) and objective (…
```

### 207. PFQ-fundamentals-000000124 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 124
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[123].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 208. PFQ-fundamentals-000000124 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 124
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[123].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 209. PFQ-fundamentals-000000124 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 124
- Chapter: Introduction to the Nursing Process
- JSON path: `$.questions[123].rationale`
- Detail: Known source or extraction contamination detected.

```text
Establishing short- and long-term goals to address Nursing diagnoses involves discussion with the patient and often requires collaboration with family members and other members of the health care team. Coordinated, team-based patient care is called collaborative care. The patien…
```

### 210. PFQ-fundamentals-000000125 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 125
- Chapter: Assessment
- JSON path: `$.questions[124].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 211. PFQ-fundamentals-000000125 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 125
- Chapter: Assessment
- JSON path: `$.questions[124].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 212. PFQ-fundamentals-000000126 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 126
- Chapter: Assessment
- JSON path: `$.questions[125].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 213. PFQ-fundamentals-000000126 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 126
- Chapter: Assessment
- JSON path: `$.questions[125].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient interview consists of three phases: orientation (introductory), working, and termination. Each phase contributes to the development of trust and engagement between the nurse and the patient. During the orientation phase of the interview, the nurse should establish th…
```

### 214. PFQ-fundamentals-000000127 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 127
- Chapter: Assessment
- JSON path: `$.questions[126].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 215. PFQ-fundamentals-000000128 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 128
- Chapter: Assessment
- JSON path: `$.questions[127].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 216. PFQ-fundamentals-000000129 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 129
- Chapter: Assessment
- JSON path: `$.questions[128].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 217. PFQ-fundamentals-000000129 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 129
- Chapter: Assessment
- JSON path: `$.questions[128].rationale`
- Detail: Pattern requires human review against the original source.

```text
Auscultation is a technique of listening with the assistance of a stethoscope to sounds made by organs or systems such as the heart, blood vessels, lungs, and abdominal cavity. Inspection involves the use of vision, hearing, and smell to closely scrutinize physical characteristi…
```

### 218. PFQ-fundamentals-000000130 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 130
- Chapter: Assessment
- JSON path: `$.questions[129].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 219. PFQ-fundamentals-000000131 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 131
- Chapter: Assessment
- JSON path: `$.questions[130].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 220. PFQ-fundamentals-000000132 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 132
- Chapter: Assessment
- JSON path: `$.questions[131].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 221. PFQ-fundamentals-000000132 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 132
- Chapter: Assessment
- JSON path: `$.questions[131].rationale`
- Detail: Pattern requires human review against the original source.

```text
Triage, a form of emergency assessment, is the classification of patients according to treatment priority. Patients are categorized by the urgency of their condition. Most emergency departments use a five-tier triage system. The five-tier system classifies patients by levels num…
```

### 222. PFQ-fundamentals-000000132 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 132
- Chapter: Assessment
- JSON path: `$.questions[131].rationale`
- Detail: Pattern requires human review against the original source.

```text
Triage, a form of emergency assessment, is the classification of patients according to treatment priority. Patients are categorized by the urgency of their condition. Most emergency departments use a five-tier triage system. The five-tier system classifies patients by levels num…
```

### 223. PFQ-fundamentals-000000133 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 133
- Chapter: Assessment
- JSON path: `$.questions[132].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 224. PFQ-fundamentals-000000133 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 133
- Chapter: Assessment
- JSON path: `$.questions[132].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 225. PFQ-fundamentals-000000134 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 134
- Chapter: Assessment
- JSON path: `$.questions[133].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 226. PFQ-fundamentals-000000135 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 135
- Chapter: Assessment
- JSON path: `$.questions[134].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 227. PFQ-fundamentals-000000135 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 135
- Chapter: Assessment
- JSON path: `$.questions[134].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 228. PFQ-fundamentals-000000135 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 135
- Chapter: Assessment
- JSON path: `$.questions[134].rationale`
- Detail: Pattern requires human review against the original source.

```text
Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Objective data, also referred to as signs, can be measured or observed. The …
```

### 229. PFQ-fundamentals-000000135 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 135
- Chapter: Assessment
- JSON path: `$.questions[134].rationale`
- Detail: Pattern requires human review against the original source.

```text
Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Objective data, also referred to as signs, can be measured or observed. The …
```

### 230. PFQ-fundamentals-000000136 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 136
- Chapter: Assessment
- JSON path: `$.questions[135].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 231. PFQ-fundamentals-000000137 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 137
- Chapter: Assessment
- JSON path: `$.questions[136].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is monitoring the blood sugar results of a patient receiving an intravenou s nutritional supplement. The patient tells the nurse, ―I have never had sugar problems before. My doctor says it is because I am getting this IV.‖ These types of data are considered to be which…
```

### 232. PFQ-fundamentals-000000137 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 137
- Chapter: Assessment
- JSON path: `$.questions[136].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 233. PFQ-fundamentals-000000137 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 137
- Chapter: Assessment
- JSON path: `$.questions[136].rationale`
- Detail: Pattern requires human review against the original source.

```text
Primary data come directly from the patient. Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Family members, friends, and ot…
```

### 234. PFQ-fundamentals-000000137 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 137
- Chapter: Assessment
- JSON path: `$.questions[136].rationale`
- Detail: Pattern requires human review against the original source.

```text
Primary data come directly from the patient. Subjective data are spoken information or symptoms that cannot be authenticated. Subjective data usually are gathered during the interview process if patients are well enough to describe their symptoms. Family members, friends, and ot…
```

### 235. PFQ-fundamentals-000000138 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 138
- Chapter: Assessment
- JSON path: `$.questions[137].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 236. PFQ-fundamentals-000000139 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 139
- Chapter: Assessment
- JSON path: `$.questions[138].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 237. PFQ-fundamentals-000000139 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 139
- Chapter: Assessment
- JSON path: `$.questions[138].rationale`
- Detail: Pattern requires human review against the original source.

```text
As patient information is collected, consistency between subjective and objective data must be confirmed. Sometimes, the nurse can use laboratory and diagnostic test results to validate the subjective data. In this case, checking the urinalysis for congruency with the patient‘s …
```

### 238. PFQ-fundamentals-000000139 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 139
- Chapter: Assessment
- JSON path: `$.questions[138].rationale`
- Detail: Pattern requires human review against the original source.

```text
As patient information is collected, consistency between subjective and objective data must be confirmed. Sometimes, the nurse can use laboratory and diagnostic test results to validate the subjective data. In this case, checking the urinalysis for congruency with the patient‘s …
```

### 239. PFQ-fundamentals-000000140 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 140
- Chapter: Assessment
- JSON path: `$.questions[139].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is attempting to get the patient to sign the operative consent. When asked if the health care provider explained the procedure to the patient, the patient replies ―Not much.‖ What action will the nurse take next?
```

### 240. PFQ-fundamentals-000000140 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 140
- Chapter: Assessment
- JSON path: `$.questions[139].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 241. PFQ-fundamentals-000000141 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 141
- Chapter: Assessment
- JSON path: `$.questions[140].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 242. PFQ-fundamentals-000000142 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 142
- Chapter: Assessment
- JSON path: `$.questions[141].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 243. PFQ-fundamentals-000000142 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 142
- Chapter: Assessment
- JSON path: `$.questions[141].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 244. PFQ-fundamentals-000000143 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 143
- Chapter: Assessment
- JSON path: `$.questions[142].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 245. PFQ-fundamentals-000000144 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 144
- Chapter: Assessment
- JSON path: `$.questions[143].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 246. PFQ-fundamentals-000000144 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 144
- Chapter: Assessment
- JSON path: `$.questions[143].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 247. PFQ-fundamentals-000000145 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 145
- Chapter: Assessment
- JSON path: `$.questions[144].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 248. PFQ-fundamentals-000000146 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 146
- Chapter: Assessment
- JSON path: `$.questions[145].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 249. PFQ-fundamentals-000000146 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 146
- Chapter: Assessment
- JSON path: `$.questions[145].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 250. PFQ-fundamentals-000000147 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 147
- Chapter: Assessment
- JSON path: `$.questions[146].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 251. PFQ-fundamentals-000000147 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 147
- Chapter: Assessment
- JSON path: `$.questions[146].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 252. PFQ-fundamentals-000000148 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 148
- Chapter: Assessment
- JSON path: `$.questions[147].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 253. PFQ-fundamentals-000000148 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 148
- Chapter: Assessment
- JSON path: `$.questions[147].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 254. PFQ-fundamentals-000000149 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 149
- Chapter: Assessment
- JSON path: `$.questions[148].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 255. PFQ-fundamentals-000000149 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 149
- Chapter: Assessment
- JSON path: `$.questions[148].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 256. PFQ-fundamentals-000000149 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 149
- Chapter: Assessment
- JSON path: `$.questions[148].rationale`
- Detail: Known source or extraction contamination detected.

```text
Patient-centered care requires the nurse to understand patient and family preferences and values. Nurses must recognize patients‘ expectations for care and provide care with respect for the diversity of human experience. While interpreting data, the nurse must be careful to avoi…
```

### 257. PFQ-fundamentals-000000150 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 150
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[149].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 258. PFQ-fundamentals-000000150 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 150
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[149].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 259. PFQ-fundamentals-000000151 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 151
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[150].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 260. PFQ-fundamentals-000000152 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 152
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[151].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 261. PFQ-fundamentals-000000152 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 152
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[151].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 262. PFQ-fundamentals-000000153 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 153
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[152].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 263. PFQ-fundamentals-000000153 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 153
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[152].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 264. PFQ-fundamentals-000000154 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 154
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[153].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 265. PFQ-fundamentals-000000155 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 155
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[154].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 266. PFQ-fundamentals-000000155 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 155
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[154].rationale`
- Detail: Pattern requires human review against the original source.

```text
The second part of the Nursing diagnosis consists of related factors (for actual Nu rsing diagnoses) and risk factors (for risk Nursing diagnoses). Related factors are the underlying cause or etiology of a patient‘s problem. Risk factors are environmental, physical, psychologica…
```

### 267. PFQ-fundamentals-000000156 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 156
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[155].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 268. PFQ-fundamentals-000000157 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 157
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[156].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 269. PFQ-fundamentals-000000157 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 157
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[156].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 270. PFQ-fundamentals-000000158 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 158
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[157].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 271. PFQ-fundamentals-000000158 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 158
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[157].rationale`
- Detail: Pattern requires human review against the original source.

```text
All patient information should be considered as potentially contributing to the identification of diagnostic labels. This information includes subjective and objective data collected through physical assessment of the patient, interview of the patient and family members, and lab…
```

### 272. PFQ-fundamentals-000000158 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 158
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[157].rationale`
- Detail: Pattern requires human review against the original source.

```text
All patient information should be considered as potentially contributing to the identification of diagnostic labels. This information includes subjective and objective data collected through physical assessment of the patient, interview of the patient and family members, and lab…
```

### 273. PFQ-fundamentals-000000159 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 159
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[158].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 274. PFQ-fundamentals-000000160 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 160
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[159].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 275. PFQ-fundamentals-000000160 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 160
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[159].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 276. PFQ-fundamentals-000000161 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 161
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[160].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 277. PFQ-fundamentals-000000162 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 162
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[161].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 278. PFQ-fundamentals-000000162 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 162
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[161].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Impaired self feeding rel aNt edRt o uIppeGr exBt r.e mCi t yMw e a knes s as manifested by inability to get food onto s pUo o nS. N T O
```

### 279. PFQ-fundamentals-000000162 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 162
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[161].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Impaired self feeding rel aNt edRt o uIppeGr exBt r.e mCi t yMw e a knes s as manifested by inability to get food onto s pUo o nS. N T O
```

### 280. PFQ-fundamentals-000000163 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 163
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[162].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 281. PFQ-fundamentals-000000164 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 164
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[163].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 282. PFQ-fundamentals-000000164 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 164
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[163].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 283. PFQ-fundamentals-000000165 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 165
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[164].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 284. PFQ-fundamentals-000000166 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 166
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[165].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 285. PFQ-fundamentals-000000166 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 166
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[165].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 286. PFQ-fundamentals-000000167 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 167
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[166].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 287. PFQ-fundamentals-000000167 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 167
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[166].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 288. PFQ-fundamentals-000000168 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 168
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[167].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is creating a care plan for a patient admitted with severe bone pain related t o an infected leg wound. Which diagnosis written on the plan indicates an understanding of the components of a Nursing diagnosis? (Select all that apply.)
```

### 289. PFQ-fundamentals-000000168 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 168
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[167].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 290. PFQ-fundamentals-000000168 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 168
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[167].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 291. PFQ-fundamentals-000000169 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 169
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[168].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 292. PFQ-fundamentals-000000169 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 169
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[168].rationale`
- Detail: Pattern requires human review against the original source.

```text
Each type of Nursing diagnostic statement contains sections or parts. Actual Nursing diagnostic statements are written with three parts: a diagnosis label, related factors, and defining characteristics. Risk Nursing diagnoses have two segments: a diagnosis label and risk factors…
```

### 293. PFQ-fundamentals-000000170 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 170
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[169].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 294. PFQ-fundamentals-000000170 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 170
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[169].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 295. PFQ-fundamentals-000000171 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 171
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[170].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 296. PFQ-fundamentals-000000171 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 171
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[170].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 297. PFQ-fundamentals-000000172 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 172
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[171].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 298. PFQ-fundamentals-000000172 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 172
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[171].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 299. PFQ-fundamentals-000000172 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 172
- Chapter: Nursing Diagnosis
- JSON path: `$.questions[171].rationale`
- Detail: Known source or extraction contamination detected.

```text
Risk factors may be environmental, physical, psychological, or situational concerns. The nurse is concerned that the patient may be at risk for suicide. Verbal statements by the patient, physical illness such as chronic pain, prior attempts to commit suicide, and a lack of socia…
```

### 300. PFQ-fundamentals-000000173 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 173
- Chapter: Planning
- JSON path: `$.questions[172].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 301. PFQ-fundamentals-000000173 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 173
- Chapter: Planning
- JSON path: `$.questions[172].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 302. PFQ-fundamentals-000000174 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 174
- Chapter: Planning
- JSON path: `$.questions[173].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 303. PFQ-fundamentals-000000174 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 174
- Chapter: Planning
- JSON path: `$.questions[173].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 304. PFQ-fundamentals-000000175 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 175
- Chapter: Planning
- JSON path: `$.questions[174].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 305. PFQ-fundamentals-000000176 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 176
- Chapter: Planning
- JSON path: `$.questions[175].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 306. PFQ-fundamentals-000000177 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 177
- Chapter: Planning
- JSON path: `$.questions[176].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 307. PFQ-fundamentals-000000177 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 177
- Chapter: Planning
- JSON path: `$.questions[176].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 308. PFQ-fundamentals-000000178 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 178
- Chapter: Planning
- JSON path: `$.questions[177].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 309. PFQ-fundamentals-000000178 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 178
- Chapter: Planning
- JSON path: `$.questions[177].rationale`
- Detail: Pattern requires human review against the original source.

```text
Goals are broad statements of purpose that describe the aim of nursing care. Goals represent short- or long-term objectives that are determined during the planning step. Some sources establish time parameters for short- and long-term goals, whereas others do not. According to Ca…
```

### 310. PFQ-fundamentals-000000179 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 179
- Chapter: Planning
- JSON path: `$.questions[178].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 311. PFQ-fundamentals-000000179 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 179
- Chapter: Planning
- JSON path: `$.questions[178].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 312. PFQ-fundamentals-000000180 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 180
- Chapter: Planning
- JSON path: `$.questions[179].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 313. PFQ-fundamentals-000000181 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 181
- Chapter: Planning
- JSON path: `$.questions[180].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 314. PFQ-fundamentals-000000182 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 182
- Chapter: Planning
- JSON path: `$.questions[181].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 315. PFQ-fundamentals-000000183 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 183
- Chapter: Planning
- JSON path: `$.questions[182].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 316. PFQ-fundamentals-000000183 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 183
- Chapter: Planning
- JSON path: `$.questions[182].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 317. PFQ-fundamentals-000000184 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 184
- Chapter: Planning
- JSON path: `$.questions[183].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 318. PFQ-fundamentals-000000185 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 185
- Chapter: Planning
- JSON path: `$.questions[184].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 319. PFQ-fundamentals-000000185 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 185
- Chapter: Planning
- JSON path: `$.questions[184].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 320. PFQ-fundamentals-000000186 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 186
- Chapter: Planning
- JSON path: `$.questions[185].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 321. PFQ-fundamentals-000000187 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 187
- Chapter: Planning
- JSON path: `$.questions[186].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 322. PFQ-fundamentals-000000187 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 187
- Chapter: Planning
- JSON path: `$.questions[186].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 323. PFQ-fundamentals-000000188 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 188
- Chapter: Planning
- JSON path: `$.questions[187].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 324. PFQ-fundamentals-000000188 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 188
- Chapter: Planning
- JSON path: `$.questions[187].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 325. PFQ-fundamentals-000000189 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 189
- Chapter: Planning
- JSON path: `$.questions[188].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 326. PFQ-fundamentals-000000190 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 190
- Chapter: Planning
- JSON path: `$.questions[189].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 327. PFQ-fundamentals-000000191 — correct answer not found in choices

- Severity: **high**
- Category: Structure
- Question index: 191
- Chapter: Planning
- JSON path: `$.questions[190].correct_answers`
- Detail: Available choice labels: ['B', 'C', 'D']

```text
A
```

### 328. PFQ-fundamentals-000000191 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 191
- Chapter: Planning
- JSON path: `$.questions[190].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 329. PFQ-fundamentals-000000192 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 192
- Chapter: Planning
- JSON path: `$.questions[191].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 330. PFQ-fundamentals-000000193 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 193
- Chapter: Planning
- JSON path: `$.questions[192].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 331. PFQ-fundamentals-000000193 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 193
- Chapter: Planning
- JSON path: `$.questions[192].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 332. PFQ-fundamentals-000000194 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 194
- Chapter: Planning
- JSON path: `$.questions[193].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 333. PFQ-fundamentals-000000194 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 194
- Chapter: Planning
- JSON path: `$.questions[193].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 334. PFQ-fundamentals-000000195 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 195
- Chapter: Planning
- JSON path: `$.questions[194].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 335. PFQ-fundamentals-000000195 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 195
- Chapter: Planning
- JSON path: `$.questions[194].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 336. PFQ-fundamentals-000000196 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 196
- Chapter: Planning
- JSON path: `$.questions[195].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 337. PFQ-fundamentals-000000196 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 196
- Chapter: Planning
- JSON path: `$.questions[195].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 338. PFQ-fundamentals-000000196 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 196
- Chapter: Planning
- JSON path: `$.questions[195].rationale`
- Detail: Pattern requires human review against the original source.

```text
Patients should be included in the planning process. Involving patients in planning their care helps them to: (1) be aware oNf i d Re n t i If i e dGn e eBd s., C( 2 ) Maccept realistic and measurable goals, and (3) embrace interventions to best achieve the mutually agreed-on go…
```

### 339. PFQ-fundamentals-000000197 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 197
- Chapter: Planning
- JSON path: `$.questions[196].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 340. PFQ-fundamentals-000000197 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 197
- Chapter: Planning
- JSON path: `$.questions[196].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 341. PFQ-fundamentals-000000197 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 197
- Chapter: Planning
- JSON path: `$.questions[196].rationale`
- Detail: Known source or extraction contamination detected.

```text
Measurable goals are specific, with numeric parameters or other concrete methods of judging whether the goal was met. When writing a goal statement with a patient, the nurse needs to clearly identify how achievement of the goal will be evaluated. When terms such as acceptable or…
```

### 342. PFQ-fundamentals-000000198 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 198
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[197].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 343. PFQ-fundamentals-000000198 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 198
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[197].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 344. PFQ-fundamentals-000000199 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 199
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[198].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 345. PFQ-fundamentals-000000199 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 199
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[198].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 346. PFQ-fundamentals-000000200 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 200
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[199].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 347. PFQ-fundamentals-000000201 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 201
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[200].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 348. PFQ-fundamentals-000000201 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 201
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[200].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 349. PFQ-fundamentals-000000202 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 202
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[201].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 350. PFQ-fundamentals-000000202 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 202
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[201].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 351. PFQ-fundamentals-000000203 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 203
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[202].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 352. PFQ-fundamentals-000000204 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 204
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[203].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 353. PFQ-fundamentals-000000205 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 205
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[204].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 354. PFQ-fundamentals-000000205 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 205
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[204].rationale`
- Detail: Pattern requires human review against the original source.

```text
N R I G B. C M Independent nursing interventions are tasks within the nursing scope of practice that the nurse may undertake without a physician or PCP order. Repositioning a patient in bed, performing oral hygiene, and providing emotional support through active listening are ex…
```

### 355. PFQ-fundamentals-000000205 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 205
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[204].rationale`
- Detail: Pattern requires human review against the original source.

```text
N R I G B. C M Independent nursing interventions are tasks within the nursing scope of practice that the nurse may undertake without a physician or PCP order. Repositioning a patient in bed, performing oral hygiene, and providing emotional support through active listening are ex…
```

### 356. PFQ-fundamentals-000000206 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 206
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[205].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 357. PFQ-fundamentals-000000207 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 207
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[206].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 358. PFQ-fundamentals-000000208 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 208
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[207].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 359. PFQ-fundamentals-000000208 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 208
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[207].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 360. PFQ-fundamentals-000000208 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 208
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[207].rationale`
- Detail: Pattern requires human review against the original source.

```text
With the patient‘s permission, the nurse should share instructions with the people who may assist with care. Nurses empower patients and their support systems through effective teaching. When nurses provide patients and their families with opportunities to ask questions and comp…
```

### 361. PFQ-fundamentals-000000208 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 208
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[207].rationale`
- Detail: Pattern requires human review against the original source.

```text
With the patient‘s permission, the nurse should share instructions with the people who may assist with care. Nurses empower patients and their support systems through effective teaching. When nurses provide patients and their families with opportunities to ask questions and comp…
```

### 362. PFQ-fundamentals-000000209 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 209
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[208].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 363. PFQ-fundamentals-000000209 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 209
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[208].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 364. PFQ-fundamentals-000000210 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 210
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[209].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 365. PFQ-fundamentals-000000211 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 211
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[210].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 366. PFQ-fundamentals-000000212 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 212
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[211].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 367. PFQ-fundamentals-000000212 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 212
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[211].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 368. PFQ-fundamentals-000000213 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 213
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[212].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 369. PFQ-fundamentals-000000214 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 214
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[213].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 370. PFQ-fundamentals-000000215 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 215
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[214].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 371. PFQ-fundamentals-000000216 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 216
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[215].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 372. PFQ-fundamentals-000000216 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 216
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[215].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 373. PFQ-fundamentals-000000217 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 217
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[216].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 374. PFQ-fundamentals-000000217 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 217
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[216].rationale`
- Detail: Pattern requires human review against the original source.

```text
Evaluation is the final step in the nursing process. Evaluation focuses on the patient and the patient‘s response to n ur singNi nUt eRrv eInt ioGn s aBnd.oCutcMome attainment. Evaluation is not a record of care that was implemented. Patient outcomes serve as the criteria agains…
```

### 375. PFQ-fundamentals-000000217 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 217
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[216].rationale`
- Detail: Pattern requires human review against the original source.

```text
Evaluation is the final step in the nursing process. Evaluation focuses on the patient and the patient‘s response to n ur singNi nUt eRrv eInt ioGn s aBnd.oCutcMome attainment. Evaluation is not a record of care that was implemented. Patient outcomes serve as the criteria agains…
```

### 376. PFQ-fundamentals-000000218 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 218
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[217].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 377. PFQ-fundamentals-000000218 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 218
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[217].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 378. PFQ-fundamentals-000000219 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 219
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[218].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 379. PFQ-fundamentals-000000220 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 220
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[219].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 380. PFQ-fundamentals-000000220 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 220
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[219].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 381. PFQ-fundamentals-000000221 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 221
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[220].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 382. PFQ-fundamentals-000000222 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 222
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[221].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 383. PFQ-fundamentals-000000222 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 222
- Chapter: Implementation and Evaluation
- JSON path: `$.questions[221].rationale`
- Detail: Known source or extraction contamination detected.

```text
Delegation principles focus on the appropriate intervention (task) being performed under the correct circumstances, by the correct personnel, and with the correct direction and supervision. The right patienNt a n dRt hIe ri gGhUt tBimS.eCreNfeMr Tto components of the ―6 Rights‖ …
```

### 384. PFQ-fundamentals-000000223 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 223
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[222].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 385. PFQ-fundamentals-000000223 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 223
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[222].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 386. PFQ-fundamentals-000000224 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 224
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[223].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 387. PFQ-fundamentals-000000225 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 225
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[224].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 388. PFQ-fundamentals-000000226 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 226
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[225].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 389. PFQ-fundamentals-000000226 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 226
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[225].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 390. PFQ-fundamentals-000000227 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 227
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[226].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 391. PFQ-fundamentals-000000228 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 228
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[227].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 392. PFQ-fundamentals-000000229 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 229
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[228].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 393. PFQ-fundamentals-000000229 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 229
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[228].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 394. PFQ-fundamentals-000000230 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 230
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[229].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 395. PFQ-fundamentals-000000231 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 231
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[230].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 396. PFQ-fundamentals-000000231 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 231
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[230].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 397. PFQ-fundamentals-000000232 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 232
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[231].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 398. PFQ-fundamentals-000000232 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 232
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[231].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 399. PFQ-fundamentals-000000233 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 233
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[232].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 400. PFQ-fundamentals-000000234 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 234
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[233].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 401. PFQ-fundamentals-000000235 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 235
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[234].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 402. PFQ-fundamentals-000000236 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 236
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[235].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 403. PFQ-fundamentals-000000236 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 236
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[235].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 404. PFQ-fundamentals-000000236 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 236
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[235].rationale`
- Detail: Pattern requires human review against the original source.

```text
An admission summary includes the patient‘s history, a medication reconciliation, and an initial assessment that a dd res Ns eUs tRhSe pIaNtieGnTt‘Bs .p r obOle m s , including identification of needs pertinent to discharge planning and formulation of a plan of care based on tho…
```

### 405. PFQ-fundamentals-000000237 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 237
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[236].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 406. PFQ-fundamentals-000000238 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 238
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[237].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 407. PFQ-fundamentals-000000239 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 239
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[238].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 408. PFQ-fundamentals-000000240 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 240
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[239].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 409. PFQ-fundamentals-000000241 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 241
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[240].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 410. PFQ-fundamentals-000000241 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 241
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[240].rationale`
- Detail: Pattern requires human review against the original source.

```text
An ineffective handoff may lead to wrong treatments, wrong medications, or other life-threatening events, increasing the length of stay and causing patient injury or death. Improvement in the hand-off process can increase patient safety and promote positive patient outcomes. The…
```

### 411. PFQ-fundamentals-000000242 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 242
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[241].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 412. PFQ-fundamentals-000000242 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 242
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[241].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 413. PFQ-fundamentals-000000243 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 243
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[242].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 414. PFQ-fundamentals-000000243 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 243
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[242].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 415. PFQ-fundamentals-000000244 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 244
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[243].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 416. PFQ-fundamentals-000000245 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 245
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[244].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 417. PFQ-fundamentals-000000245 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 245
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[244].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 418. PFQ-fundamentals-000000246 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 246
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[245].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 419. PFQ-fundamentals-000000246 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 246
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[245].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 420. PFQ-fundamentals-000000247 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 247
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[246].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 421. PFQ-fundamentals-000000247 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 247
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[246].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 422. PFQ-fundamentals-000000248 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 248
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[247].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 423. PFQ-fundamentals-000000248 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 248
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[247].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Patient is hemorrhaging with four saturated dressings in an hour: A
```

### 424. PFQ-fundamentals-000000248 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 248
- Chapter: Documentation, Electronic Health Records, and Reporting
- JSON path: `$.questions[247].rationale`
- Detail: Known source or extraction contamination detected.

```text
SBAR stands for situation (what is happening the current time), background (circumstances leading up to this situation), assessment (what the nurse thinks the problem is), and recommendation (what needs to be done to correct the situation). A history of hypertension would be bac…
```

### 425. PFQ-fundamentals-000000249 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 249
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[248].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 426. PFQ-fundamentals-000000250 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 250
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[249].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 427. PFQ-fundamentals-000000250 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 250
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[249].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 428. PFQ-fundamentals-000000250 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 250
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[249].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Deontology is an ethical theory that stresses the rightness or wrongness of individual behaviors, duties, and obligations without concern for the consequences of specific actions. Meeting the needs of patients while maintaining their right to privacy, confidentiality, …
```

### 429. PFQ-fundamentals-000000251 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 251
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[250].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 430. PFQ-fundamentals-000000252 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 252
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[251].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 431. PFQ-fundamentals-000000253 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 253
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[252].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 432. PFQ-fundamentals-000000253 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 253
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[252].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 433. PFQ-fundamentals-000000254 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 254
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[253].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 434. PFQ-fundamentals-000000254 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 254
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[253].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 435. PFQ-fundamentals-000000255 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 255
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[254].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 436. PFQ-fundamentals-000000256 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 256
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[255].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 437. PFQ-fundamentals-000000257 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 257
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[256].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 438. PFQ-fundamentals-000000257 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 257
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[256].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 439. PFQ-fundamentals-000000258 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 258
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[257].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 440. PFQ-fundamentals-000000259 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 259
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[258].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 441. PFQ-fundamentals-000000259 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 259
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[258].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 442. PFQ-fundamentals-000000260 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 260
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[259].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 443. PFQ-fundamentals-000000261 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 261
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[260].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 444. PFQ-fundamentals-000000262 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 262
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[261].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 445. PFQ-fundamentals-000000263 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 263
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[262].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 446. PFQ-fundamentals-000000264 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 264
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[263].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 447. PFQ-fundamentals-000000265 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 265
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[264].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 448. PFQ-fundamentals-000000266 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 266
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[265].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 449. PFQ-fundamentals-000000267 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 267
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[266].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 450. PFQ-fundamentals-000000268 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 268
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[267].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who has had many admissions and readmissions. T he nurse believes that the patient keeps coming to the hospital because the patient ―wants his drugs,‖ and is ―non-compliant‖ at home with diabetic therapy. To reduce the risk of slander against t …
```

### 451. PFQ-fundamentals-000000268 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 268
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[267].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 452. PFQ-fundamentals-000000268 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 268
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[267].rationale`
- Detail: Pattern requires human review against the original source.

```text
Defamation of character occurs when a public statement is made that is false and injurious to another person. Oral defamation of character is slander. Slander is spoken information that is untrue, causing prejudice against someone or jeopardizing that person‘s reputation. The nu…
```

### 453. PFQ-fundamentals-000000269 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 269
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[268].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 454. PFQ-fundamentals-000000269 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 269
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[268].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 455. PFQ-fundamentals-000000270 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 270
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[269].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 456. PFQ-fundamentals-000000270 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 270
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[269].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 457. PFQ-fundamentals-000000271 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 271
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[270].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 458. PFQ-fundamentals-000000272 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 272
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[271].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 459. PFQ-fundamentals-000000272 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 272
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[271].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 460. PFQ-fundamentals-000000273 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 273
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[272].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 461. PFQ-fundamentals-000000274 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 274
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[273].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse knows which law protects health care professionals from charges of negligence when providing emergency care at the scene of an accident? U S N
```

### 462. PFQ-fundamentals-000000274 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 274
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[273].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 463. PFQ-fundamentals-000000274 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 274
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[273].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 464. PFQ-fundamentals-000000274 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 274
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[273].rationale`
- Detail: Known source or extraction contamination detected.

```text
All 50 states have enacted Good Samaritan laws offering protection for physicians and other health care professionals who provide emergency care at the scene of a disaster, emergency, or accident. Good Samaritan laws protect health care professionals from charges of negligence i…
```

### 465. PFQ-fundamentals-000000275 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 275
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[274].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 466. PFQ-fundamentals-000000275 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 275
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[274].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 467. PFQ-fundamentals-000000276 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 276
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[275].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 468. PFQ-fundamentals-000000276 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 276
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[275].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 469. PFQ-fundamentals-000000277 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 277
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[276].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 470. PFQ-fundamentals-000000277 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 277
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[276].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The Uniform Anatomical Gift Act GB.CM U S N T O
```

### 471. PFQ-fundamentals-000000277 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 277
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[276].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The Uniform Anatomical Gift Act GB.CM U S N T O
```

### 472. PFQ-fundamentals-000000277 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 277
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[276].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 473. PFQ-fundamentals-000000277 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 277
- Chapter: Ethical and Legal Considerations
- JSON path: `$.questions[276].rationale`
- Detail: Known source or extraction contamination detected.

```text
Advance directives consist of three documents: (1) living will, (2) durable power of attorney, and (3) health care proxy, commonly referred to as a durable power of attorney for health care. The Patient‘s Bill of Rights informs consumers of health care about specific privileges …
```

### 474. PFQ-fundamentals-000000278 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 278
- Chapter: Leadership and Management
- JSON path: `$.questions[277].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 475. PFQ-fundamentals-000000279 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 279
- Chapter: Leadership and Management
- JSON path: `$.questions[278].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 476. PFQ-fundamentals-000000280 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 280
- Chapter: Leadership and Management
- JSON path: `$.questions[279].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is acting as a leader in the role of charge nurse and notes that the unlicen sed assistive personnel (UAP) on the floor are stressed related to their increased workload. The nurse changes the original planned approach based on the presenting situation. Which theory of …
```

### 477. PFQ-fundamentals-000000280 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 280
- Chapter: Leadership and Management
- JSON path: `$.questions[279].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 478. PFQ-fundamentals-000000280 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 280
- Chapter: Leadership and Management
- JSON path: `$.questions[279].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Transformational U S N
```

### 479. PFQ-fundamentals-000000280 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 280
- Chapter: Leadership and Management
- JSON path: `$.questions[279].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 480. PFQ-fundamentals-000000281 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 281
- Chapter: Leadership and Management
- JSON path: `$.questions[280].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 481. PFQ-fundamentals-000000281 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 281
- Chapter: Leadership and Management
- JSON path: `$.questions[280].rationale`
- Detail: Pattern requires human review against the original source.

```text
Transactional leaders use reward and punishment to gain the cooperation of follow ers. Transformational leaders use methods that inspire people to follow their lead. Transformational leaders work toward transforming an organization with the help of others. The authoritarian or a…
```

### 482. PFQ-fundamentals-000000281 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 281
- Chapter: Leadership and Management
- JSON path: `$.questions[280].rationale`
- Detail: Pattern requires human review against the original source.

```text
Transactional leaders use reward and punishment to gain the cooperation of follow ers. Transformational leaders use methods that inspire people to follow their lead. Transformational leaders work toward transforming an organization with the help of others. The authoritarian or a…
```

### 483. PFQ-fundamentals-000000282 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 282
- Chapter: Leadership and Management
- JSON path: `$.questions[281].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 484. PFQ-fundamentals-000000282 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 282
- Chapter: Leadership and Management
- JSON path: `$.questions[281].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 485. PFQ-fundamentals-000000283 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 283
- Chapter: Leadership and Management
- JSON path: `$.questions[282].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 486. PFQ-fundamentals-000000284 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 284
- Chapter: Leadership and Management
- JSON path: `$.questions[283].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 487. PFQ-fundamentals-000000284 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 284
- Chapter: Leadership and Management
- JSON path: `$.questions[283].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 488. PFQ-fundamentals-000000285 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 285
- Chapter: Leadership and Management
- JSON path: `$.questions[284].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 489. PFQ-fundamentals-000000285 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 285
- Chapter: Leadership and Management
- JSON path: `$.questions[284].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 490. PFQ-fundamentals-000000285 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 285
- Chapter: Leadership and Management
- JSON path: `$.questions[284].rationale`
- Detail: Pattern requires human review against the original source.

```text
Although autocratic leadership is a strict form of leadership, it is useful in crisis situations. A nurse may act as an autocratic leader when taking charge after a patient is found unresponsive. In this situation, it is helpful to have a leader who takes control and directs oth…
```

### 491. PFQ-fundamentals-000000286 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 286
- Chapter: Leadership and Management
- JSON path: `$.questions[285].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse has made patient care assignments and expects all team members to set their own goals for the day and manage their time to meet their goals. The nurse is implementing w hat style of leadership?
```

### 492. PFQ-fundamentals-000000286 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 286
- Chapter: Leadership and Management
- JSON path: `$.questions[285].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 493. PFQ-fundamentals-000000287 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 287
- Chapter: Leadership and Management
- JSON path: `$.questions[286].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 494. PFQ-fundamentals-000000288 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 288
- Chapter: Leadership and Management
- JSON path: `$.questions[287].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 495. PFQ-fundamentals-000000289 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 289
- Chapter: Leadership and Management
- JSON path: `$.questions[288].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 496. PFQ-fundamentals-000000289 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 289
- Chapter: Leadership and Management
- JSON path: `$.questions[288].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 497. PFQ-fundamentals-000000290 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 290
- Chapter: Leadership and Management
- JSON path: `$.questions[289].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 498. PFQ-fundamentals-000000291 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 291
- Chapter: Leadership and Management
- JSON path: `$.questions[290].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 499. PFQ-fundamentals-000000291 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 291
- Chapter: Leadership and Management
- JSON path: `$.questions[290].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 500. PFQ-fundamentals-000000292 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 292
- Chapter: Leadership and Management
- JSON path: `$.questions[291].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 501. PFQ-fundamentals-000000292 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 292
- Chapter: Leadership and Management
- JSON path: `$.questions[291].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 502. PFQ-fundamentals-000000294 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 294
- Chapter: Leadership and Management
- JSON path: `$.questions[293].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 503. PFQ-fundamentals-000000294 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 294
- Chapter: Leadership and Management
- JSON path: `$.questions[293].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Assistance with eating breakfast U S N
```

### 504. PFQ-fundamentals-000000295 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 295
- Chapter: Leadership and Management
- JSON path: `$.questions[294].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 505. PFQ-fundamentals-000000295 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 295
- Chapter: Leadership and Management
- JSON path: `$.questions[294].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 506. PFQ-fundamentals-000000295 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 295
- Chapter: Leadership and Management
- JSON path: `$.questions[294].rationale`
- Detail: Pattern requires human review against the original source.

```text
The person to whom the assignment was delegated cannot delegate that assignment to someone else. If the person cannot carry out the assignment, the individual needs to notify the delegating RN so that the task may be reassigned or completed by the RN. The RN must remember to del…
```

### 507. PFQ-fundamentals-000000296 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 296
- Chapter: Leadership and Management
- JSON path: `$.questions[295].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 508. PFQ-fundamentals-000000296 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 296
- Chapter: Leadership and Management
- JSON path: `$.questions[295].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 509. PFQ-fundamentals-000000297 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 297
- Chapter: Leadership and Management
- JSON path: `$.questions[296].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 510. PFQ-fundamentals-000000297 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 297
- Chapter: Leadership and Management
- JSON path: `$.questions[296].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 511. PFQ-fundamentals-000000298 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 298
- Chapter: Leadership and Management
- JSON path: `$.questions[297].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 512. PFQ-fundamentals-000000298 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 298
- Chapter: Leadership and Management
- JSON path: `$.questions[297].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 513. PFQ-fundamentals-000000299 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 299
- Chapter: Leadership and Management
- JSON path: `$.questions[298].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 514. PFQ-fundamentals-000000299 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 299
- Chapter: Leadership and Management
- JSON path: `$.questions[298].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 515. PFQ-fundamentals-000000300 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 300
- Chapter: Leadership and Management
- JSON path: `$.questions[299].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 516. PFQ-fundamentals-000000300 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 300
- Chapter: Leadership and Management
- JSON path: `$.questions[299].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 517. PFQ-fundamentals-000000301 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 301
- Chapter: Leadership and Management
- JSON path: `$.questions[300].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 518. PFQ-fundamentals-000000301 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 301
- Chapter: Leadership and Management
- JSON path: `$.questions[300].rationale`
- Detail: Known source or extraction contamination detected.

```text
Mintzberg described management in terms of behaviors. Underlying his descriptions were two assumptions: much of a manager‘s time is spent in human relations, and managers are more reactive than proactive. These assumptions provided the basis for three categories of behaviors: in…
```

### 519. PFQ-fundamentals-000000302 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 302
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[301].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 520. PFQ-fundamentals-000000302 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 302
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[301].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 521. PFQ-fundamentals-000000303 — NURSINGTB contamination

- Severity: **high**
- Category: Contamination
- Question index: 303
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[302].stem`
- Detail: Known source or extraction contamination detected.

```text
The American Nurses Association (ANA) standards of professional performance require nurses to use research findings in practice. How do these standards impact nurses in the workplace? NURSINGTB.CO
```

### 522. PFQ-fundamentals-000000303 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 303
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[302].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 523. PFQ-fundamentals-000000304 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 304
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[303].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 524. PFQ-fundamentals-000000305 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 305
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[304].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 525. PFQ-fundamentals-000000305 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 305
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[304].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Descriptive research stud Ny URSINGTB.COM
```

### 526. PFQ-fundamentals-000000306 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 306
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[305].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 527. PFQ-fundamentals-000000306 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 306
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[305].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 528. PFQ-fundamentals-000000307 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 307
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[306].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 529. PFQ-fundamentals-000000307 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 307
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[306].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 530. PFQ-fundamentals-000000308 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 308
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[307].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 531. PFQ-fundamentals-000000309 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 309
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[308].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 532. PFQ-fundamentals-000000309 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 309
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[308].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Address ethical procedures. U S N
```

### 533. PFQ-fundamentals-000000309 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 309
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[308].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 534. PFQ-fundamentals-000000310 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 310
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[309].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 535. PFQ-fundamentals-000000310 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 310
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[309].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 536. PFQ-fundamentals-000000311 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 311
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[310].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 537. PFQ-fundamentals-000000312 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 312
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[311].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 538. PFQ-fundamentals-000000313 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 313
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[312].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 539. PFQ-fundamentals-000000314 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 314
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[313].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 540. PFQ-fundamentals-000000314 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 314
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[313].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 541. PFQ-fundamentals-000000315 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 315
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[314].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 542. PFQ-fundamentals-000000316 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 316
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[315].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 543. PFQ-fundamentals-000000317 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 317
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[316].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 544. PFQ-fundamentals-000000317 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 317
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[316].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 545. PFQ-fundamentals-000000318 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 318
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[317].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 546. PFQ-fundamentals-000000319 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 319
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[318].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 547. PFQ-fundamentals-000000320 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 320
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[319].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 548. PFQ-fundamentals-000000321 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 321
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[320].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 549. PFQ-fundamentals-000000321 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 321
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[320].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 550. PFQ-fundamentals-000000322 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 322
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[321].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 551. PFQ-fundamentals-000000322 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 322
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[321].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 552. PFQ-fundamentals-000000323 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 323
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[322].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 553. PFQ-fundamentals-000000323 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 323
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[322].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 554. PFQ-fundamentals-000000324 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 324
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[323].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 555. PFQ-fundamentals-000000325 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 325
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[324].stem`
- Detail: Pattern requires human review against the original source.

```text
Nurses use new information NinUthReSir IprNacGtiTceB. .I nCt hOeMp r o c e s s of implementing EBP, the nurse carries out which actions? (Select all that apply.)
```

### 556. PFQ-fundamentals-000000325 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 325
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[324].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 557. PFQ-fundamentals-000000325 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 325
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[324].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 558. PFQ-fundamentals-000000326 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 326
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[325].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 559. PFQ-fundamentals-000000326 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 326
- Chapter: Evidence-Based Practice and Nursing Research
- JSON path: `$.questions[325].rationale`
- Detail: Known source or extraction contamination detected.

```text
A Magnet hospital is characterized by excellent patient outcomes resulting from nursing, a high level of nursing job satisfaction with a low nurse turnover rate, and appropriate resolution of any grievances. The Magnet Recognition Program supports an evidence-based environment, …
```

### 560. PFQ-fundamentals-000000327 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 327
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[326].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 561. PFQ-fundamentals-000000327 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 327
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[326].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 562. PFQ-fundamentals-000000328 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 328
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[327].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 563. PFQ-fundamentals-000000329 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 329
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[328].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 564. PFQ-fundamentals-000000329 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 329
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[328].rationale`
- Detail: Pattern requires human review against the original source.

```text
To teach effectively, nurses must recognize that patients of all ages come from diverse cultural and socioeconomic backgrounds. Each has a different ability to comprehend health care information. Results of the NAAL research indicate that among American adults, 30 million (14%) …
```

### 565. PFQ-fundamentals-000000330 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 330
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[329].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 566. PFQ-fundamentals-000000331 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 331
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[330].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 567. PFQ-fundamentals-000000332 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 332
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[331].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 568. PFQ-fundamentals-000000332 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 332
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[331].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 569. PFQ-fundamentals-000000332 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 332
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[331].rationale`
- Detail: Pattern requires human review against the original source.

```text
Formal patient education is delivered throughout the community in the form of media, in a variety of educational and group settings, or in a planned, goal-directed, one-on-one session with a patient in the acute care setting. Informal education is usually learner or patient dire…
```

### 570. PFQ-fundamentals-000000332 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 332
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[331].rationale`
- Detail: Pattern requires human review against the original source.

```text
Formal patient education is delivered throughout the community in the form of media, in a variety of educational and group settings, or in a planned, goal-directed, one-on-one session with a patient in the acute care setting. Informal education is usually learner or patient dire…
```

### 571. PFQ-fundamentals-000000333 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 333
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[332].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 572. PFQ-fundamentals-000000334 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 334
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[333].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 573. PFQ-fundamentals-000000334 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 334
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[333].rationale`
- Detail: Pattern requires human review against the original source.

```text
Some patient education sessions have formal and informal elements, because the nurse and patient may set goals together before the nurse formulates and implements the plan of care, and the patient is free to ask questions that may direct the session. The health care information …
```

### 574. PFQ-fundamentals-000000335 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 335
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[334].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is implementing a patient teaching plan regarding diabetes mellitus. One of the short-term goals of the plan is that the patient will be able to verbalize three symptoms of hypoglycemia. The nurse recognizes that this is what type of teaching?
```

### 575. PFQ-fundamentals-000000335 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 335
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[334].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 576. PFQ-fundamentals-000000336 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 336
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[335].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 577. PFQ-fundamentals-000000337 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 337
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[336].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 578. PFQ-fundamentals-000000337 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 337
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[336].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 579. PFQ-fundamentals-000000338 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 338
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[337].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 580. PFQ-fundamentals-000000338 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 338
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[337].rationale`
- Detail: Pattern requires human review against the original source.

```text
Teaching should be tailored to elderly patients. Reports indicate that two-thirds of U.S. adults 66 years old and older have inadequate or marginal literacy skills, and 81% of patients 60 years old and older at a public hospital could not read or understand basic materials such …
```

### 581. PFQ-fundamentals-000000339 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 339
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[338].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 582. PFQ-fundamentals-000000340 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 340
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[339].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 583. PFQ-fundamentals-000000341 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 341
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[340].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 584. PFQ-fundamentals-000000341 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 341
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[340].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 585. PFQ-fundamentals-000000342 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 342
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[341].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 586. PFQ-fundamentals-000000343 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 343
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[342].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 587. PFQ-fundamentals-000000343 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 343
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[342].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 588. PFQ-fundamentals-000000344 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 344
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[343].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 589. PFQ-fundamentals-000000344 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 344
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[343].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 590. PFQ-fundamentals-000000345 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 345
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[344].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 591. PFQ-fundamentals-000000345 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 345
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[344].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 592. PFQ-fundamentals-000000346 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 346
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[345].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 593. PFQ-fundamentals-000000346 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 346
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[345].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 594. PFQ-fundamentals-000000347 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 347
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[346].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 595. PFQ-fundamentals-000000347 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 347
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[346].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 596. PFQ-fundamentals-000000348 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 348
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[347].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 597. PFQ-fundamentals-000000348 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 348
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[347].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 598. PFQ-fundamentals-000000348 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 348
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[347].rationale`
- Detail: Pattern requires human review against the original source.

```text
Before health care teaching sessions for adults, assess reading level, learning styles, and readiness to learn. Family members should not be used as interpreters of specific medical information to maintain the patient‘s right to privacy and to avoid possible misinterpretation of…
```

### 599. PFQ-fundamentals-000000349 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 349
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[348].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 600. PFQ-fundamentals-000000350 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 350
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[349].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 601. PFQ-fundamentals-000000351 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 351
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[350].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 602. PFQ-fundamentals-000000351 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 351
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[350].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 603. PFQ-fundamentals-000000351 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 351
- Chapter: Health Literacy and Patient Education
- JSON path: `$.questions[350].rationale`
- Detail: Known source or extraction contamination detected.

```text
On completion of assessment, a nursing diagnosis relevant to the educational nee ds of the patient or caregiver can be determined. Diagnoses specifically related to patient educati on include deficient knowledge, readiness for enhanced knowledge, and noncompliance. 3rd Edition
```

### 604. PFQ-fundamentals-000000352 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 352
- Chapter: Nursing Informatics
- JSON path: `$.questions[351].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 605. PFQ-fundamentals-000000352 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 352
- Chapter: Nursing Informatics
- JSON path: `$.questions[351].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 606. PFQ-fundamentals-000000352 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 352
- Chapter: Nursing Informatics
- JSON path: `$.questions[351].rationale`
- Detail: Pattern requires human review against the original source.

```text
Informatics is a broad academic field encompassing artificial intelligence, cognitive science, computer science, information science, and social science. Medical informatics refers to informatics related to health care and describes a distinct specialty in the discipline of medi…
```

### 607. PFQ-fundamentals-000000353 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 353
- Chapter: Nursing Informatics
- JSON path: `$.questions[352].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 608. PFQ-fundamentals-000000354 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 354
- Chapter: Nursing Informatics
- JSON path: `$.questions[353].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 609. PFQ-fundamentals-000000355 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 355
- Chapter: Nursing Informatics
- JSON path: `$.questions[354].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 610. PFQ-fundamentals-000000355 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 355
- Chapter: Nursing Informatics
- JSON path: `$.questions[354].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 611. PFQ-fundamentals-000000356 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 356
- Chapter: Nursing Informatics
- JSON path: `$.questions[355].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 612. PFQ-fundamentals-000000357 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 357
- Chapter: Nursing Informatics
- JSON path: `$.questions[356].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 613. PFQ-fundamentals-000000358 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 358
- Chapter: Nursing Informatics
- JSON path: `$.questions[357].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 614. PFQ-fundamentals-000000358 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 358
- Chapter: Nursing Informatics
- JSON path: `$.questions[357].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 615. PFQ-fundamentals-000000359 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 359
- Chapter: Nursing Informatics
- JSON path: `$.questions[358].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 616. PFQ-fundamentals-000000359 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 359
- Chapter: Nursing Informatics
- JSON path: `$.questions[358].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 617. PFQ-fundamentals-000000360 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 360
- Chapter: Nursing Informatics
- JSON path: `$.questions[359].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 618. PFQ-fundamentals-000000360 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 360
- Chapter: Nursing Informatics
- JSON path: `$.questions[359].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 619. PFQ-fundamentals-000000361 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 361
- Chapter: Nursing Informatics
- JSON path: `$.questions[360].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 620. PFQ-fundamentals-000000362 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 362
- Chapter: Nursing Informatics
- JSON path: `$.questions[361].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 621. PFQ-fundamentals-000000362 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 362
- Chapter: Nursing Informatics
- JSON path: `$.questions[361].rationale`
- Detail: Pattern requires human review against the original source.

```text
Descriptions of nursing informatics competencies often focus on levels that include beginner, experienced, specialist, and innovator. Beginner skills include computer, information, and web literacy; fundamental skills in information management and computer technology; and the ab…
```

### 622. PFQ-fundamentals-000000362 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 362
- Chapter: Nursing Informatics
- JSON path: `$.questions[361].rationale`
- Detail: Pattern requires human review against the original source.

```text
Descriptions of nursing informatics competencies often focus on levels that include beginner, experienced, specialist, and innovator. Beginner skills include computer, information, and web literacy; fundamental skills in information management and computer technology; and the ab…
```

### 623. PFQ-fundamentals-000000363 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 363
- Chapter: Nursing Informatics
- JSON path: `$.questions[362].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 624. PFQ-fundamentals-000000363 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 363
- Chapter: Nursing Informatics
- JSON path: `$.questions[362].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Technical competencies N R I G B.C M
```

### 625. PFQ-fundamentals-000000363 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 363
- Chapter: Nursing Informatics
- JSON path: `$.questions[362].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 626. PFQ-fundamentals-000000364 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 364
- Chapter: Nursing Informatics
- JSON path: `$.questions[363].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 627. PFQ-fundamentals-000000365 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 365
- Chapter: Nursing Informatics
- JSON path: `$.questions[364].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 628. PFQ-fundamentals-000000366 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 366
- Chapter: Nursing Informatics
- JSON path: `$.questions[365].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 629. PFQ-fundamentals-000000366 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 366
- Chapter: Nursing Informatics
- JSON path: `$.questions[365].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 630. PFQ-fundamentals-000000367 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 367
- Chapter: Nursing Informatics
- JSON path: `$.questions[366].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 631. PFQ-fundamentals-000000368 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 368
- Chapter: Nursing Informatics
- JSON path: `$.questions[367].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 632. PFQ-fundamentals-000000368 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 368
- Chapter: Nursing Informatics
- JSON path: `$.questions[367].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 633. PFQ-fundamentals-000000369 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 369
- Chapter: Nursing Informatics
- JSON path: `$.questions[368].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 634. PFQ-fundamentals-000000369 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 369
- Chapter: Nursing Informatics
- JSON path: `$.questions[368].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 635. PFQ-fundamentals-000000370 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 370
- Chapter: Nursing Informatics
- JSON path: `$.questions[369].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 636. PFQ-fundamentals-000000370 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 370
- Chapter: Nursing Informatics
- JSON path: `$.questions[369].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 637. PFQ-fundamentals-000000371 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 371
- Chapter: Nursing Informatics
- JSON path: `$.questions[370].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 638. PFQ-fundamentals-000000371 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 371
- Chapter: Nursing Informatics
- JSON path: `$.questions[370].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 639. PFQ-fundamentals-000000372 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 372
- Chapter: Nursing Informatics
- JSON path: `$.questions[371].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 640. PFQ-fundamentals-000000372 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 372
- Chapter: Nursing Informatics
- JSON path: `$.questions[371].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 641. PFQ-fundamentals-000000372 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 372
- Chapter: Nursing Informatics
- JSON path: `$.questions[371].rationale`
- Detail: Known source or extraction contamination detected.

```text
Access to electronic records requires a user to have system access and verification codes as a measure of security and protection of the patient‘s privacy. The codes leave an electronic trail of authorized users that can be audited. HIPAA sets the standards on how security and c…
```

### 642. PFQ-fundamentals-000000373 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 373
- Chapter: Health and Wellness
- JSON path: `$.questions[372].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 643. PFQ-fundamentals-000000374 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 374
- Chapter: Health and Wellness
- JSON path: `$.questions[373].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 644. PFQ-fundamentals-000000374 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 374
- Chapter: Health and Wellness
- JSON path: `$.questions[373].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 645. PFQ-fundamentals-000000375 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 375
- Chapter: Health and Wellness
- JSON path: `$.questions[374].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 646. PFQ-fundamentals-000000376 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 376
- Chapter: Health and Wellness
- JSON path: `$.questions[375].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is preparing a patient teaching plan and is seeking a way to determine the patient‘s readiness and motivation to aNct rRe ga rId i nGg l i fBe s.t yCl e cMhanges to best manage diabetes mellitus. Which model would be useful Uf o r tSh i s Nn u r sTe ? O
```

### 647. PFQ-fundamentals-000000376 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 376
- Chapter: Health and Wellness
- JSON path: `$.questions[375].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 648. PFQ-fundamentals-000000377 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 377
- Chapter: Health and Wellness
- JSON path: `$.questions[376].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 649. PFQ-fundamentals-000000377 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 377
- Chapter: Health and Wellness
- JSON path: `$.questions[376].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 650. PFQ-fundamentals-000000377 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 377
- Chapter: Health and Wellness
- JSON path: `$.questions[376].rationale`
- Detail: Pattern requires human review against the original source.

```text
In the three primary components of the Health Belief Model, six main constructs influence an individual‘s decision to take action about disease prevention, screening, and controlling illness. The model suggests that individuals are motivated to take action if they believe that t…
```

### 651. PFQ-fundamentals-000000377 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 377
- Chapter: Health and Wellness
- JSON path: `$.questions[376].rationale`
- Detail: Pattern requires human review against the original source.

```text
In the three primary components of the Health Belief Model, six main constructs influence an individual‘s decision to take action about disease prevention, screening, and controlling illness. The model suggests that individuals are motivated to take action if they believe that t…
```

### 652. PFQ-fundamentals-000000378 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 378
- Chapter: Health and Wellness
- JSON path: `$.questions[377].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 653. PFQ-fundamentals-000000379 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 379
- Chapter: Health and Wellness
- JSON path: `$.questions[378].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 654. PFQ-fundamentals-000000379 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 379
- Chapter: Health and Wellness
- JSON path: `$.questions[378].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 655. PFQ-fundamentals-000000380 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 380
- Chapter: Health and Wellness
- JSON path: `$.questions[379].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 656. PFQ-fundamentals-000000380 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 380
- Chapter: Health and Wellness
- JSON path: `$.questions[379].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 657. PFQ-fundamentals-000000381 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 381
- Chapter: Health and Wellness
- JSON path: `$.questions[380].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 658. PFQ-fundamentals-000000381 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 381
- Chapter: Health and Wellness
- JSON path: `$.questions[380].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 659. PFQ-fundamentals-000000382 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 382
- Chapter: Health and Wellness
- JSON path: `$.questions[381].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 660. PFQ-fundamentals-000000383 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 383
- Chapter: Health and Wellness
- JSON path: `$.questions[382].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 661. PFQ-fundamentals-000000384 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 384
- Chapter: Health and Wellness
- JSON path: `$.questions[383].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 662. PFQ-fundamentals-000000385 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 385
- Chapter: Health and Wellness
- JSON path: `$.questions[384].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 663. PFQ-fundamentals-000000385 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 385
- Chapter: Health and Wellness
- JSON path: `$.questions[384].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 664. PFQ-fundamentals-000000386 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 386
- Chapter: Health and Wellness
- JSON path: `$.questions[385].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 665. PFQ-fundamentals-000000386 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 386
- Chapter: Health and Wellness
- JSON path: `$.questions[385].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
F ocu s on i m pr ovi ng qualNit yUoRf Sli IfeNthGr oTuBgh.p r eOve ntive be ha vi or s .
```

### 666. PFQ-fundamentals-000000387 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 387
- Chapter: Health and Wellness
- JSON path: `$.questions[386].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 667. PFQ-fundamentals-000000388 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 388
- Chapter: Health and Wellness
- JSON path: `$.questions[387].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 668. PFQ-fundamentals-000000389 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 389
- Chapter: Health and Wellness
- JSON path: `$.questions[388].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 669. PFQ-fundamentals-000000389 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 389
- Chapter: Health and Wellness
- JSON path: `$.questions[388].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 670. PFQ-fundamentals-000000390 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 390
- Chapter: Health and Wellness
- JSON path: `$.questions[389].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 671. PFQ-fundamentals-000000390 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 390
- Chapter: Health and Wellness
- JSON path: `$.questions[389].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 672. PFQ-fundamentals-000000390 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 390
- Chapter: Health and Wellness
- JSON path: `$.questions[389].rationale`
- Detail: Pattern requires human review against the original source.

```text
The genetic vulnerability of an organism, or risk of disease expression based on genotype, is involuntarily passed from biologic parents to their offspring. Societal attitudes about testing and management of high-risk populations depend on the potential for expression of genetic…
```

### 673. PFQ-fundamentals-000000391 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 391
- Chapter: Health and Wellness
- JSON path: `$.questions[390].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 674. PFQ-fundamentals-000000392 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 392
- Chapter: Health and Wellness
- JSON path: `$.questions[391].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 675. PFQ-fundamentals-000000393 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 393
- Chapter: Health and Wellness
- JSON path: `$.questions[392].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 676. PFQ-fundamentals-000000394 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 394
- Chapter: Health and Wellness
- JSON path: `$.questions[393].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 677. PFQ-fundamentals-000000395 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 395
- Chapter: Health and Wellness
- JSON path: `$.questions[394].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 678. PFQ-fundamentals-000000395 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 395
- Chapter: Health and Wellness
- JSON path: `$.questions[394].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 679. PFQ-fundamentals-000000396 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 396
- Chapter: Health and Wellness
- JSON path: `$.questions[395].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 680. PFQ-fundamentals-000000396 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 396
- Chapter: Health and Wellness
- JSON path: `$.questions[395].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 681. PFQ-fundamentals-000000397 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 397
- Chapter: Health and Wellness
- JSON path: `$.questions[396].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 682. PFQ-fundamentals-000000397 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 397
- Chapter: Health and Wellness
- JSON path: `$.questions[396].rationale`
- Detail: Known source or extraction contamination detected.

```text
The economic stability of individuals or families can determine whether they are willing to seek preventive care or screening examinations. Even if screening is free or low cost, the patient or family members may decline because of the potential for testing positive for a diseas…
```

### 683. PFQ-fundamentals-000000398 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 398
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[397].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 684. PFQ-fundamentals-000000398 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 398
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[397].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 685. PFQ-fundamentals-000000399 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 399
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[398].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 686. PFQ-fundamentals-000000399 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 399
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[398].rationale`
- Detail: Pattern requires human review against the original source.

```text
The superego is the structure that houses the moral branch of personality . The Id acts strictly on instinct without consideration of reality. The Ego is partly conscious but does not consider right from wrong. Freud‘s theory contains the ―anal phase.‖
```

### 687. PFQ-fundamentals-000000400 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 400
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[399].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 688. PFQ-fundamentals-000000400 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 400
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[399].rationale`
- Detail: Known source or extraction contamination detected.

```text
The phallic stage occurs between the ages of 3 and 6 years, and pleasure centers on the child‘s discovery that self-stimulation is enjoyable. The oral stage is seen in infants where pleasure centers around the mouth and putting things in the mouth. The Anal stage occurs between …
```

### 689. PFQ-fundamentals-000000401 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 401
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[400].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 690. PFQ-fundamentals-000000401 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 401
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[400].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 691. PFQ-fundamentals-000000401 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 401
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[400].rationale`
- Detail: Known source or extraction contamination detected.

```text
The most important item needed for a child to master this stage of development is a consistent caregiver who provides food and attention. If the caregiver is inconsistent or unable to meet these needs, the child will develop mistrust of those around him. Ensuring that someone fe…
```

### 692. PFQ-fundamentals-000000402 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 402
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[401].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient that is actively trying to conceive a child but continues to drink alcohol. The patient states that she‘ll stop drinking once she is pregnant. What is the most appropriate response by the nurse?
```

### 693. PFQ-fundamentals-000000402 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 402
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[401].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 694. PFQ-fundamentals-000000402 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 402
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[401].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 695. PFQ-fundamentals-000000402 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 402
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[401].rationale`
- Detail: Known source or extraction contamination detected.

```text
Rapid development occurs before many women know that they are pregnant, making alcohol consumption unsafe at any time during pregnancy. NCLEX Client Needs Category: Health Promotion and Maintenance
```

### 696. PFQ-fundamentals-000000403 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 403
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[402].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 697. PFQ-fundamentals-000000404 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 404
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[403].stem`
- Detail: Pattern requires human review against the original source.

```text
A home health care nurse is making a well-baby visit to the home of a new mother who has an infant. What assessment finding leads the nurse to provide further anticipatory guidance and teaching to the mother?
```

### 698. PFQ-fundamentals-000000404 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 404
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[403].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 699. PFQ-fundamentals-000000405 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 405
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[404].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 700. PFQ-fundamentals-000000406 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 406
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[405].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 701. PFQ-fundamentals-000000406 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 406
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[405].rationale`
- Detail: Pattern requires human review against the original source.

```text
An appropriate serving size is 1 tablespoon per year of age, so an appr opriate amount of meat for this child is 3 tablespoons, not 1/2 cup (which is 8 tablespoons). The nur se should provide more education to the family. The other options are appropriate but are not directly re…
```

### 702. PFQ-fundamentals-000000407 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 407
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[406].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 703. PFQ-fundamentals-000000407 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 407
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[406].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 704. PFQ-fundamentals-000000407 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 407
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[406].rationale`
- Detail: Known source or extraction contamination detected.

```text
It is common for toddlers to hNa v eRi mIa g i nGa r yBf .r i eCn d sM. They are especially important in allowingthe child to express something unpleasant. The other responses are not appropriate. NCLEX Client Needs Category: Health Promotion and Maintenance
```

### 705. PFQ-fundamentals-000000407 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 407
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[406].rationale`
- Detail: Pattern requires human review against the original source.

```text
It is common for toddlers to hNa v eRi mIa g i nGa r yBf .r i eCn d sM. They are especially important in allowingthe child to express something unpleasant. The other responses are not appropriate. NCLEX Client Needs Category: Health Promotion and Maintenance
```

### 706. PFQ-fundamentals-000000408 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 408
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[407].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 707. PFQ-fundamentals-000000409 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 409
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[408].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 708. PFQ-fundamentals-000000410 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 410
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[409].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 709. PFQ-fundamentals-000000410 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 410
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[409].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 710. PFQ-fundamentals-000000411 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 411
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[410].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 711. PFQ-fundamentals-000000412 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 412
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[411].stem`
- Detail: Pattern requires human review against the original source.

```text
A father expresses frustration that his school-aged child is suddenly ―sick all the time.‖ What action by the nurse is best? U S N
```

### 712. PFQ-fundamentals-000000412 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 412
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[411].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 713. PFQ-fundamentals-000000412 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 412
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[411].rationale`
- Detail: Known source or extraction contamination detected.

```text
Children in this age-group tend to have a higher incidence of minor illnesses because of exposure to others. The nurse can reassure the father by explaining this. No other action is needed at this point. NCLEX Client Needs Category: Health Promotion and Maintenance
```

### 714. PFQ-fundamentals-000000413 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 413
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[412].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 715. PFQ-fundamentals-000000413 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 413
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[412].rationale`
- Detail: Pattern requires human review against the original source.

```text
School-aged children benefit from simple explanations they can understand. Just telling the child not to worry is dismissive of the child‘s concerns. A school-aged child may not be able to read and/or understand a written pamphlet. Using phrases such as ―put you to sleep‖ should…
```

### 716. PFQ-fundamentals-000000413 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 413
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[412].rationale`
- Detail: Pattern requires human review against the original source.

```text
School-aged children benefit from simple explanations they can understand. Just telling the child not to worry is dismissive of the child‘s concerns. A school-aged child may not be able to read and/or understand a written pamphlet. Using phrases such as ―put you to sleep‖ should…
```

### 717. PFQ-fundamentals-000000414 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 414
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[413].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 718. PFQ-fundamentals-000000415 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 415
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[414].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 719. PFQ-fundamentals-000000416 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 416
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[415].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 720. PFQ-fundamentals-000000416 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 416
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[415].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Assess the child for signsNof RchilId abGuseBo.r nCe glMe c t .
```

### 721. PFQ-fundamentals-000000416 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 416
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[415].rationale`
- Detail: Pattern requires human review against the original source.

```text
A 3-month-old child should be able to follow a moving object with his or h er eyes. However, one single abnormal assessment finding does not necessarily mean that the child has a growt h and developmental delay. The nurse should assess for other age-appropriate behaviors. Docume…
```

### 722. PFQ-fundamentals-000000417 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 417
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[416].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 723. PFQ-fundamentals-000000417 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 417
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[416].rationale`
- Detail: Known source or extraction contamination detected.

```text
Throwing an object down to watch someone else pick it up is a typical be havior for this age- group. The nurse should teach the parent about how this behavior relates to toddler gro wth and development. The other actions are not appropriate in this situation. U S N T O NCLEX Cli…
```

### 724. PFQ-fundamentals-000000417 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 417
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[416].rationale`
- Detail: Pattern requires human review against the original source.

```text
Throwing an object down to watch someone else pick it up is a typical be havior for this age- group. The nurse should teach the parent about how this behavior relates to toddler gro wth and development. The other actions are not appropriate in this situation. U S N T O NCLEX Cli…
```

### 725. PFQ-fundamentals-000000418 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 418
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[417].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 726. PFQ-fundamentals-000000418 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 418
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[417].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 727. PFQ-fundamentals-000000419 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 419
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[418].stem`
- Detail: Pattern requires human review against the original source.

```text
A nurse is assessing a 12 monthNoldRat Ia weGll-bBa. Cby visit. For what developmental milestones does the nurse assess this child? ( Se l e c t a l l that apply.)
```

### 728. PFQ-fundamentals-000000419 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 419
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[418].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 729. PFQ-fundamentals-000000419 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 419
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[418].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 730. PFQ-fundamentals-000000420 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 420
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[419].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 731. PFQ-fundamentals-000000420 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 420
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[419].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Weight loss and malnutrition N R I G
```

### 732. PFQ-fundamentals-000000420 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 420
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[419].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 733. PFQ-fundamentals-000000421 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 421
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[420].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 734. PFQ-fundamentals-000000421 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 421
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[420].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 735. PFQ-fundamentals-000000421 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 421
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[420].rationale`
- Detail: Known source or extraction contamination detected.

```text
Adolescents need education on drinking and driving, suicide and depression, safer sexual practices, and physical changes that occur during puberty. A bicycle helmet fitting st ation would not be a priority for this age-group. NCLEX Client Needs Category: Health Promotion and Mai…
```

### 736. PFQ-fundamentals-000000422 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 422
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[421].stem`
- Detail: Pattern requires human review against the original source.

```text
A pregnant woman in her second trimester is scheduled for quad testing. What conditions does the nurse explain are s creUe n e dSf o Nr in Tt his assOessment? ( Select all that apply.)
```

### 737. PFQ-fundamentals-000000422 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 422
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[421].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 738. PFQ-fundamentals-000000422 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 422
- Chapter: Human Development: Conception Through Adolescence
- JSON path: `$.questions[421].rationale`
- Detail: Known source or extraction contamination detected.

```text
Quad testing includes assessing for neural tube defects, trisomy 18, and trisomy 21 (Do wn syndrome). It does not screen for heart or blood-clotting problems. 3rd Edition
```

### 739. PFQ-fundamentals-000000423 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 423
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[422].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 740. PFQ-fundamentals-000000424 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 424
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[423].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 741. PFQ-fundamentals-000000425 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 425
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[424].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse plans to develop a comprehensive screening tool to use with young adults , assessing their lifestyles and healthy living habits. What barrier must the nurse plan to overcome to make this screening successful?
```

### 742. PFQ-fundamentals-000000425 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 425
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[424].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 743. PFQ-fundamentals-000000425 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 425
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[424].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 744. PFQ-fundamentals-000000426 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 426
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[425].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 745. PFQ-fundamentals-000000427 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 427
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[426].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 746. PFQ-fundamentals-000000428 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 428
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[427].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 747. PFQ-fundamentals-000000429 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 429
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[428].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 748. PFQ-fundamentals-000000429 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 429
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[428].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 749. PFQ-fundamentals-000000430 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 430
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[429].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 750. PFQ-fundamentals-000000431 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 431
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[430].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 751. PFQ-fundamentals-000000432 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 432
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[431].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 752. PFQ-fundamentals-000000432 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 432
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[431].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 753. PFQ-fundamentals-000000433 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 433
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[432].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 754. PFQ-fundamentals-000000434 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 434
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[433].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 755. PFQ-fundamentals-000000434 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 434
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[433].rationale`
- Detail: Known source or extraction contamination detected.

```text
One normal age-related change seen in the older adult is decreased immune function. The older adult should place high priority on avoiding illness by staying away from people who are sick and avoiding large crowds during peak communicable illness periods. The other instructions …
```

### 756. PFQ-fundamentals-000000435 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 435
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[434].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 757. PFQ-fundamentals-000000436 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 436
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[435].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 758. PFQ-fundamentals-000000437 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 437
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[436].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 759. PFQ-fundamentals-000000437 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 437
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[436].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 760. PFQ-fundamentals-000000438 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 438
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[437].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 761. PFQ-fundamentals-000000438 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 438
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[437].rationale`
- Detail: Known source or extraction contamination detected.

```text
The health consequences of using e-cigarettes are not yet known because they are new products. The nurse educates the young adult to this fact. NCLEX Client Needs Category: Health Promotion and Maintenance
```

### 762. PFQ-fundamentals-000000439 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 439
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[438].stem`
- Detail: Pattern requires human review against the original source.

```text
A nurse notes an older adult puts excessive amounts of salt on her food. What intervention by the nurse is best? NUR ISG BN.CTM O
```

### 763. PFQ-fundamentals-000000439 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 439
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[438].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 764. PFQ-fundamentals-000000440 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 440
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[439].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 765. PFQ-fundamentals-000000441 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 441
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[440].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 766. PFQ-fundamentals-000000441 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 441
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[440].rationale`
- Detail: Pattern requires human review against the original source.

```text
Abuse of illicit drugs can cause many symptoms, including panic attacks and aggressive behavior. After assessing for an infectious process, the nurse should determine if the patient has used any recreational drugs. The other assessments are not as important and can be completed …
```

### 767. PFQ-fundamentals-000000441 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 441
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[440].rationale`
- Detail: Pattern requires human review against the original source.

```text
Abuse of illicit drugs can cause many symptoms, including panic attacks and aggressive behavior. After assessing for an infectious process, the nurse should determine if the patient has used any recreational drugs. The other assessments are not as important and can be completed …
```

### 768. PFQ-fundamentals-000000442 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 442
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[441].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 769. PFQ-fundamentals-000000443 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 443
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[442].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 770. PFQ-fundamentals-000000443 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 443
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[442].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 771. PFQ-fundamentals-000000444 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 444
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[443].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 772. PFQ-fundamentals-000000444 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 444
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[443].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 773. PFQ-fundamentals-000000445 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 445
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[444].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 774. PFQ-fundamentals-000000445 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 445
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[444].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 775. PFQ-fundamentals-000000446 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 446
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[445].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 776. PFQ-fundamentals-000000447 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 447
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[446].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 777. PFQ-fundamentals-000000447 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 447
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[446].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 778. PFQ-fundamentals-000000447 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 447
- Chapter: Human Development: Young Adult Through Older Adult
- JSON path: `$.questions[446].rationale`
- Detail: Known source or extraction contamination detected.

```text
There are several risk factors for developing delirium, including advanced age, polypharmacy, pain, surgery, and hospitaliz aNtiUonR. SBIeinNgGbTliBnd.iCs nOoMt a risk factor. 3rd Edition
```

### 779. PFQ-fundamentals-000000448 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 448
- Chapter: Vital Signs
- JSON path: `$.questions[447].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 780. PFQ-fundamentals-000000449 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 449
- Chapter: Vital Signs
- JSON path: `$.questions[448].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 781. PFQ-fundamentals-000000450 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 450
- Chapter: Vital Signs
- JSON path: `$.questions[449].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 782. PFQ-fundamentals-000000450 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 450
- Chapter: Vital Signs
- JSON path: `$.questions[449].rationale`
- Detail: Known source or extraction contamination detected.

```text
A temperature of 98.4 °F is normal. ―Afebrile‖ means having a normal temperature. The other readings are not related to this term. NCLEX Client Needs Category: Physiological Integrity: Reduction of Risk Potential
```

### 783. PFQ-fundamentals-000000451 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 451
- Chapter: Vital Signs
- JSON path: `$.questions[450].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 784. PFQ-fundamentals-000000452 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 452
- Chapter: Vital Signs
- JSON path: `$.questions[451].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 785. PFQ-fundamentals-000000453 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 453
- Chapter: Vital Signs
- JSON path: `$.questions[452].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 786. PFQ-fundamentals-000000453 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 453
- Chapter: Vital Signs
- JSON path: `$.questions[452].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Student pulls the pinna of the patient‘s ear up and back. U S N T
```

### 787. PFQ-fundamentals-000000454 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 454
- Chapter: Vital Signs
- JSON path: `$.questions[453].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 788. PFQ-fundamentals-000000454 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 454
- Chapter: Vital Signs
- JSON path: `$.questions[453].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 789. PFQ-fundamentals-000000455 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 455
- Chapter: Vital Signs
- JSON path: `$.questions[454].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 790. PFQ-fundamentals-000000456 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 456
- Chapter: Vital Signs
- JSON path: `$.questions[455].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 791. PFQ-fundamentals-000000456 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 456
- Chapter: Vital Signs
- JSON path: `$.questions[455].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 792. PFQ-fundamentals-000000457 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 457
- Chapter: Vital Signs
- JSON path: `$.questions[456].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 793. PFQ-fundamentals-000000458 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 458
- Chapter: Vital Signs
- JSON path: `$.questions[457].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 794. PFQ-fundamentals-000000459 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 459
- Chapter: Vital Signs
- JSON path: `$.questions[458].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 795. PFQ-fundamentals-000000460 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 460
- Chapter: Vital Signs
- JSON path: `$.questions[459].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 796. PFQ-fundamentals-000000461 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 461
- Chapter: Vital Signs
- JSON path: `$.questions[460].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 797. PFQ-fundamentals-000000461 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 461
- Chapter: Vital Signs
- JSON path: `$.questions[460].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 798. PFQ-fundamentals-000000461 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 461
- Chapter: Vital Signs
- JSON path: `$.questions[460].rationale`
- Detail: Pattern requires human review against the original source.

```text
This patient has orthostatic hypotension, which is a drop of 20 mm Hg in systolic reading and 10 mm Hg in diastolic readinNg wRh e nIt h eGp atBi e.n tCs t a nMd s up fr om a sitting or lying position. The patient‘s cardiovascular system does not compensate for this, so the pati…
```

### 799. PFQ-fundamentals-000000461 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 461
- Chapter: Vital Signs
- JSON path: `$.questions[460].rationale`
- Detail: Pattern requires human review against the original source.

```text
This patient has orthostatic hypotension, which is a drop of 20 mm Hg in systolic reading and 10 mm Hg in diastolic readinNg wRh e nIt h eGp atBi e.n tCs t a nMd s up fr om a sitting or lying position. The patient‘s cardiovascular system does not compensate for this, so the pati…
```

### 800. PFQ-fundamentals-000000462 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 462
- Chapter: Vital Signs
- JSON path: `$.questions[461].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 801. PFQ-fundamentals-000000462 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 462
- Chapter: Vital Signs
- JSON path: `$.questions[461].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 802. PFQ-fundamentals-000000463 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 463
- Chapter: Vital Signs
- JSON path: `$.questions[462].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 803. PFQ-fundamentals-000000464 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 464
- Chapter: Vital Signs
- JSON path: `$.questions[463].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 804. PFQ-fundamentals-000000464 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 464
- Chapter: Vital Signs
- JSON path: `$.questions[463].rationale`
- Detail: Pattern requires human review against the original source.

```text
A pulse of 42 beats/min is considered bradycardia and the patient should be assessed first because perfusion could be cNo m pRr o mIi s eGd . TBhe.bClooMd pressure, pulse oximetry, and respiratory rate are normal. U S N T O
```

### 805. PFQ-fundamentals-000000464 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 464
- Chapter: Vital Signs
- JSON path: `$.questions[463].rationale`
- Detail: Pattern requires human review against the original source.

```text
A pulse of 42 beats/min is considered bradycardia and the patient should be assessed first because perfusion could be cNo m pRr o mIi s eGd . TBhe.bClooMd pressure, pulse oximetry, and respiratory rate are normal. U S N T O
```

### 806. PFQ-fundamentals-000000465 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 465
- Chapter: Vital Signs
- JSON path: `$.questions[464].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 807. PFQ-fundamentals-000000466 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 466
- Chapter: Vital Signs
- JSON path: `$.questions[465].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 808. PFQ-fundamentals-000000466 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 466
- Chapter: Vital Signs
- JSON path: `$.questions[465].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 809. PFQ-fundamentals-000000466 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 466
- Chapter: Vital Signs
- JSON path: `$.questions[465].rationale`
- Detail: Known source or extraction contamination detected.

```text
Vital signs give information on the functioning of body systems, can lead the nurse to identify early signs of problems, can be used to evaluate the effectiveness of interventions, and provide a baseline to compare against subsequent readings. They are not used to solely determi…
```

### 810. PFQ-fundamentals-000000467 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 467
- Chapter: Vital Signs
- JSON path: `$.questions[466].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 811. PFQ-fundamentals-000000468 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 468
- Chapter: Vital Signs
- JSON path: `$.questions[467].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 812. PFQ-fundamentals-000000468 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 468
- Chapter: Vital Signs
- JSON path: `$.questions[467].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 813. PFQ-fundamentals-000000468 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 468
- Chapter: Vital Signs
- JSON path: `$.questions[467].rationale`
- Detail: Known source or extraction contamination detected.

```text
Head injury, increasing age, recent food intake, pain, and increased (not decreased) fluid volume all can increase blood pressure. NCLEX Client Needs Category: Physiological Integrity: Reduction of Risk Potential
```

### 814. PFQ-fundamentals-000000469 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 469
- Chapter: Vital Signs
- JSON path: `$.questions[468].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 815. PFQ-fundamentals-000000469 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 469
- Chapter: Vital Signs
- JSON path: `$.questions[468].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 816. PFQ-fundamentals-000000469 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 469
- Chapter: Vital Signs
- JSON path: `$.questions[468].rationale`
- Detail: Known source or extraction contamination detected.

```text
Problems in the brain, heart, and lungs can directly lead to changes in respiratory rate and effort. Problems in the liver and skeletal muscle do not affect respirations directly. NCLEX Client Needs Category: Physiological Integrity: Reduction of Risk Potential
```

### 817. PFQ-fundamentals-000000470 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 470
- Chapter: Vital Signs
- JSON path: `$.questions[469].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 818. PFQ-fundamentals-000000471 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 471
- Chapter: Vital Signs
- JSON path: `$.questions[470].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 819. PFQ-fundamentals-000000471 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 471
- Chapter: Vital Signs
- JSON path: `$.questions[470].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 820. PFQ-fundamentals-000000472 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 472
- Chapter: Vital Signs
- JSON path: `$.questions[471].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 821. PFQ-fundamentals-000000472 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 472
- Chapter: Vital Signs
- JSON path: `$.questions[471].rationale`
- Detail: Known source or extraction contamination detected.

```text
Dyspnea is difficult, labored breathing, usually with a rapid, shallow pattern, that may be painful. Anxiety usually is present as well. Accessory muscles in the chest and neck are used in dyspneic breathing. Many patients experiencing dyspnea find it easier to breath in an upri…
```

### 822. PFQ-fundamentals-000000473 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 473
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[472].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 823. PFQ-fundamentals-000000474 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 474
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[473].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 824. PFQ-fundamentals-000000475 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 475
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[474].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 825. PFQ-fundamentals-000000476 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 476
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[475].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 826. PFQ-fundamentals-000000477 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 477
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[476].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 827. PFQ-fundamentals-000000478 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 478
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[477].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 828. PFQ-fundamentals-000000478 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 478
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[477].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 829. PFQ-fundamentals-000000479 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 479
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[478].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 830. PFQ-fundamentals-000000480 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 480
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[479].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 831. PFQ-fundamentals-000000480 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 480
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[479].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Start with the eye the patient wants you to start with
```

### 832. PFQ-fundamentals-000000481 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 481
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[480].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 833. PFQ-fundamentals-000000481 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 481
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[480].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 834. PFQ-fundamentals-000000482 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 482
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[481].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 835. PFQ-fundamentals-000000483 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 483
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[482].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 836. PFQ-fundamentals-000000483 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 483
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[482].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 837. PFQ-fundamentals-000000484 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 484
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[483].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 838. PFQ-fundamentals-000000485 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 485
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[484].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 839. PFQ-fundamentals-000000486 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 486
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[485].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 840. PFQ-fundamentals-000000487 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 487
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[486].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 841. PFQ-fundamentals-000000487 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 487
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[486].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 842. PFQ-fundamentals-000000488 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 488
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[487].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 843. PFQ-fundamentals-000000488 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 488
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[487].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Prepare to treat the patient for asthma. U S N
```

### 844. PFQ-fundamentals-000000489 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 489
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[488].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 845. PFQ-fundamentals-000000489 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 489
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[488].rationale`
- Detail: Pattern requires human review against the original source.

```text
Cranial nerve III (oculomotor nerve) is assessed by observing the patient‘s pupil size and reaction to light and the direction of gaze. Identifying a common scent would test cranial nerve I. Assessing the patient‘s visual acuity tests cranial nerve II. Assessing hearing is crani…
```

### 846. PFQ-fundamentals-000000490 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 490
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[489].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 847. PFQ-fundamentals-000000490 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 490
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[489].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 848. PFQ-fundamentals-000000491 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 491
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[490].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 849. PFQ-fundamentals-000000492 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 492
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[491].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 850. PFQ-fundamentals-000000492 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 492
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[491].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 851. PFQ-fundamentals-000000492 — NURSINGTB contamination

- Severity: **high**
- Category: Contamination
- Question index: 492
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[491].rationale`
- Detail: Known source or extraction contamination detected.

```text
During the interview process, the nurse needs to demonstrate interest in the patient by leaning slightly toward him/her, allowing requested family or friends to accompany the patient, and closing the door to the room to ensure privacy. Typing intently when the patient is talking…
```

### 852. PFQ-fundamentals-000000493 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 493
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[492].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 853. PFQ-fundamentals-000000493 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 493
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[492].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 854. PFQ-fundamentals-000000494 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 494
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[493].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 855. PFQ-fundamentals-000000494 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 494
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[493].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 856. PFQ-fundamentals-000000495 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 495
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[494].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 857. PFQ-fundamentals-000000495 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 495
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[494].rationale`
- Detail: Known source or extraction contamination detected.

```text
Peripheral cyanosis can result from poor circulation. Purpura can be seen in patients with clotting disorders. Jaundice often indicates liver disorders such as liver failure. Albinism is genetically determined. Vitiligo is thought to be an autoimmune response. NCLEX Client Needs…
```

### 858. PFQ-fundamentals-000000496 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 496
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[495].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 859. PFQ-fundamentals-000000496 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 496
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[495].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 860. PFQ-fundamentals-000000497 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 497
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[496].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 861. PFQ-fundamentals-000000497 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 497
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[496].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 862. PFQ-fundamentals-000000497 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 497
- Chapter: Health History and Physical Assessment
- JSON path: `$.questions[496].rationale`
- Detail: Known source or extraction contamination detected.

```text
After finishing the exam, the nurse provides the patient with privacy for changing back into street clothes and any needed hygiene material. The nurse also documents the findings and cleans the room before the next patient is seen. The nurse does not simply tell the patient he/s…
```

### 863. PFQ-fundamentals-000000498 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 498
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[497].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 864. PFQ-fundamentals-000000499 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 499
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[498].stem`
- Detail: Pattern requires human review against the original source.

```text
A nursing student wants to obsNervRe enIcultGuratBio.n practices of an ethnic minority community. What action by the student is bUe s t ?S NT O
```

### 865. PFQ-fundamentals-000000499 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 499
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[498].stem`
- Detail: Pattern requires human review against the original source.

```text
A nursing student wants to obsNervRe enIcultGuratBio.n practices of an ethnic minority community. What action by the student is bUe s t ?S NT O
```

### 866. PFQ-fundamentals-000000499 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 499
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[498].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 867. PFQ-fundamentals-000000500 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 500
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[499].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 868. PFQ-fundamentals-000000501 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 501
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[500].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 869. PFQ-fundamentals-000000502 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 502
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[501].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 870. PFQ-fundamentals-000000503 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 503
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[502].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 871. PFQ-fundamentals-000000504 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 504
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[503].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 872. PFQ-fundamentals-000000504 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 504
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[503].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 873. PFQ-fundamentals-000000504 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 504
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[503].rationale`
- Detail: Pattern requires human review against the original source.

```text
Discrimination can occur at the societal level, so even though this nurse is not prejudiced, patients from ethnic and cultural minorities can still suffer from discrimination. The other answers do not explain how discrimination can occur. N R I GOBBJ:.2C1.2M
```

### 874. PFQ-fundamentals-000000505 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 505
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[504].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 875. PFQ-fundamentals-000000506 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 506
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[505].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 876. PFQ-fundamentals-000000507 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 507
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[506].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 877. PFQ-fundamentals-000000507 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 507
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[506].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 878. PFQ-fundamentals-000000507 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 507
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[506].rationale`
- Detail: Pattern requires human review against the original source.

```text
Rituals are deeply powerful and have great meaning for individuals who practice them. The nurse should work with the patient to facilitate the ritual. Investigating the rit ual for patient harm or illegality is ethnocentric; the nurse‘s first thoughts should not be on the potent…
```

### 879. PFQ-fundamentals-000000508 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 508
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[507].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 880. PFQ-fundamentals-000000509 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 509
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[508].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 881. PFQ-fundamentals-000000509 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 509
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[508].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 882. PFQ-fundamentals-000000510 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 510
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[509].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 883. PFQ-fundamentals-000000511 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 511
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[510].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 884. PFQ-fundamentals-000000511 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 511
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[510].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Communication differences can lead to misunderstandings and possible medical errors. Many cultural groups have verbal and nonverbal communication patterns that differ from other groups. Variations can occur due to personal or social situations. The nurse should attempt…
```

### 885. PFQ-fundamentals-000000512 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 512
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[511].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 886. PFQ-fundamentals-000000513 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 513
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[512].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 887. PFQ-fundamentals-000000513 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 513
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[512].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 888. PFQ-fundamentals-000000514 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 514
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[513].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 889. PFQ-fundamentals-000000514 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 514
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[513].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 890. PFQ-fundamentals-000000515 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 515
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[514].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 891. PFQ-fundamentals-000000516 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 516
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[515].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 892. PFQ-fundamentals-000000517 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 517
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[516].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 893. PFQ-fundamentals-000000517 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 517
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[516].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 894. PFQ-fundamentals-000000518 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 518
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[517].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "B", "C"]
```

### 895. PFQ-fundamentals-000000518 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 518
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[517].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 896. PFQ-fundamentals-000000519 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 519
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[518].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 897. PFQ-fundamentals-000000519 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 519
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[518].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 898. PFQ-fundamentals-000000520 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 520
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[519].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 899. PFQ-fundamentals-000000520 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 520
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[519].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 900. PFQ-fundamentals-000000521 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 521
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[520].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 901. PFQ-fundamentals-000000522 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 522
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[521].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 902. PFQ-fundamentals-000000522 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 522
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[521].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 903. PFQ-fundamentals-000000522 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 522
- Chapter: Ethnicity and Cultural Assessment
- JSON path: `$.questions[521].rationale`
- Detail: Known source or extraction contamination detected.

```text
The Giger and Davidhizar Transcultural Assessment Model looks at communication, space, social orientation, time, environmental control, and biological variation. The questions all address these factors; however, asking why the patient does not want to shake the nurse‘s hand soun…
```

### 904. PFQ-fundamentals-000000523 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 523
- Chapter: Spiritual Health
- JSON path: `$.questions[522].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 905. PFQ-fundamentals-000000524 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 524
- Chapter: Spiritual Health
- JSON path: `$.questions[523].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 906. PFQ-fundamentals-000000524 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 524
- Chapter: Spiritual Health
- JSON path: `$.questions[523].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Needs to change medicat Ni on sR. IGB.CM
```

### 907. PFQ-fundamentals-000000524 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 524
- Chapter: Spiritual Health
- JSON path: `$.questions[523].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O There are many cues to alert the nurse that a patient might have unmet spiritual needs, including facing a terminal illness. The nurse should conduct spiritual assessments on all patients, but this one is the priority.
```

### 908. PFQ-fundamentals-000000525 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 525
- Chapter: Spiritual Health
- JSON path: `$.questions[524].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 909. PFQ-fundamentals-000000525 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 525
- Chapter: Spiritual Health
- JSON path: `$.questions[524].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 910. PFQ-fundamentals-000000526 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 526
- Chapter: Spiritual Health
- JSON path: `$.questions[525].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 911. PFQ-fundamentals-000000526 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 526
- Chapter: Spiritual Health
- JSON path: `$.questions[525].rationale`
- Detail: Known source or extraction contamination detected.

```text
Spiritual care must be multidisciplinary to be most effective. The nurse best addresses patients‘ spiritual needs by discussing them during interdisciplinary rounds. NCLEX Client Needs Category: Psychosocial Integrity
```

### 912. PFQ-fundamentals-000000527 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 527
- Chapter: Spiritual Health
- JSON path: `$.questions[526].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 913. PFQ-fundamentals-000000527 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 527
- Chapter: Spiritual Health
- JSON path: `$.questions[526].rationale`
- Detail: Pattern requires human review against the original source.

```text
Moral distress is cultural conflict between medical treatment and religious beliefs, expressions of concern about rejection by religious community, hesitation in accepting blood transfusion . The other diagnoses are not related. aOnning
```

### 914. PFQ-fundamentals-000000528 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 528
- Chapter: Spiritual Health
- JSON path: `$.questions[527].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 915. PFQ-fundamentals-000000529 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 529
- Chapter: Spiritual Health
- JSON path: `$.questions[528].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 916. PFQ-fundamentals-000000530 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 530
- Chapter: Spiritual Health
- JSON path: `$.questions[529].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 917. PFQ-fundamentals-000000530 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 530
- Chapter: Spiritual Health
- JSON path: `$.questions[529].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 918. PFQ-fundamentals-000000531 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 531
- Chapter: Spiritual Health
- JSON path: `$.questions[530].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 919. PFQ-fundamentals-000000532 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 532
- Chapter: Spiritual Health
- JSON path: `$.questions[531].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 920. PFQ-fundamentals-000000532 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 532
- Chapter: Spiritual Health
- JSON path: `$.questions[531].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Ask if the patient and family want to pray. U S N T
```

### 921. PFQ-fundamentals-000000532 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 532
- Chapter: Spiritual Health
- JSON path: `$.questions[531].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 922. PFQ-fundamentals-000000533 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 533
- Chapter: Spiritual Health
- JSON path: `$.questions[532].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 923. PFQ-fundamentals-000000534 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 534
- Chapter: Spiritual Health
- JSON path: `$.questions[533].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 924. PFQ-fundamentals-000000534 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 534
- Chapter: Spiritual Health
- JSON path: `$.questions[533].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 925. PFQ-fundamentals-000000535 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 535
- Chapter: Spiritual Health
- JSON path: `$.questions[534].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 926. PFQ-fundamentals-000000536 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 536
- Chapter: Spiritual Health
- JSON path: `$.questions[535].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 927. PFQ-fundamentals-000000536 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 536
- Chapter: Spiritual Health
- JSON path: `$.questions[535].rationale`
- Detail: Pattern requires human review against the original source.

```text
Promoting connectedness means recognizing that family and friends are providing at least some of the patient‘s spiritual care. The nurse best assists when offering to call someone for the patient or family. The other options may be appropriate but are not directly related to con…
```

### 928. PFQ-fundamentals-000000536 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 536
- Chapter: Spiritual Health
- JSON path: `$.questions[535].rationale`
- Detail: Pattern requires human review against the original source.

```text
Promoting connectedness means recognizing that family and friends are providing at least some of the patient‘s spiritual care. The nurse best assists when offering to call someone for the patient or family. The other options may be appropriate but are not directly related to con…
```

### 929. PFQ-fundamentals-000000537 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 537
- Chapter: Spiritual Health
- JSON path: `$.questions[536].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 930. PFQ-fundamentals-000000538 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 538
- Chapter: Spiritual Health
- JSON path: `$.questions[537].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 931. PFQ-fundamentals-000000538 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 538
- Chapter: Spiritual Health
- JSON path: `$.questions[537].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 932. PFQ-fundamentals-000000539 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 539
- Chapter: Spiritual Health
- JSON path: `$.questions[538].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 933. PFQ-fundamentals-000000540 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 540
- Chapter: Spiritual Health
- JSON path: `$.questions[539].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 934. PFQ-fundamentals-000000540 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 540
- Chapter: Spiritual Health
- JSON path: `$.questions[539].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 935. PFQ-fundamentals-000000540 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 540
- Chapter: Spiritual Health
- JSON path: `$.questions[539].rationale`
- Detail: Pattern requires human review against the original source.

```text
Spirituality focuses on the meanings of life, death, and existence. Religion is an organiz ed and structured method of practicing or expressing one‘s spirituality, so they are interconnected and not mutually exclusive. Religion provides the structure for expressing spiritua lity…
```

### 936. PFQ-fundamentals-000000541 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 541
- Chapter: Spiritual Health
- JSON path: `$.questions[540].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 937. PFQ-fundamentals-000000541 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 541
- Chapter: Spiritual Health
- JSON path: `$.questions[540].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 938. PFQ-fundamentals-000000542 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 542
- Chapter: Spiritual Health
- JSON path: `$.questions[541].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 939. PFQ-fundamentals-000000542 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 542
- Chapter: Spiritual Health
- JSON path: `$.questions[541].rationale`
- Detail: Pattern requires human review against the original source.

```text
Native American, Hindu, and Buddhist practitioners believe that health and illness are a matter of balance or imbalance in the body. M S C : N C L E X C l i e n t N e e d sC NategRor y:IPsyGchosBoi.caCl InMtegrity
```

### 940. PFQ-fundamentals-000000542 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 542
- Chapter: Spiritual Health
- JSON path: `$.questions[541].rationale`
- Detail: Pattern requires human review against the original source.

```text
Native American, Hindu, and Buddhist practitioners believe that health and illness are a matter of balance or imbalance in the body. M S C : N C L E X C l i e n t N e e d sC NategRor y:IPsyGchosBoi.caCl InMtegrity
```

### 941. PFQ-fundamentals-000000543 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 543
- Chapter: Spiritual Health
- JSON path: `$.questions[542].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 942. PFQ-fundamentals-000000543 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 543
- Chapter: Spiritual Health
- JSON path: `$.questions[542].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 943. PFQ-fundamentals-000000544 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 544
- Chapter: Spiritual Health
- JSON path: `$.questions[543].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 944. PFQ-fundamentals-000000544 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 544
- Chapter: Spiritual Health
- JSON path: `$.questions[543].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 945. PFQ-fundamentals-000000545 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 545
- Chapter: Spiritual Health
- JSON path: `$.questions[544].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 946. PFQ-fundamentals-000000545 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 545
- Chapter: Spiritual Health
- JSON path: `$.questions[544].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 947. PFQ-fundamentals-000000546 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 546
- Chapter: Spiritual Health
- JSON path: `$.questions[545].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 948. PFQ-fundamentals-000000546 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 546
- Chapter: Spiritual Health
- JSON path: `$.questions[545].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 949. PFQ-fundamentals-000000547 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 547
- Chapter: Spiritual Health
- JSON path: `$.questions[546].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 950. PFQ-fundamentals-000000547 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 547
- Chapter: Spiritual Health
- JSON path: `$.questions[546].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 951. PFQ-fundamentals-000000547 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 547
- Chapter: Spiritual Health
- JSON path: `$.questions[546].rationale`
- Detail: Known source or extraction contamination detected.

```text
Native Americans often use shamans; prayers, songs, and dances; storytelling; and herbs in health care. The HOPE framework assesses sources of hope, meaning comfort, strength, peace, love, and connection; organized religion; personal spirituality and practice; and effects on med…
```

### 952. PFQ-fundamentals-000000548 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 548
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[547].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 953. PFQ-fundamentals-000000549 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 549
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[548].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 954. PFQ-fundamentals-000000549 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 549
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[548].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 955. PFQ-fundamentals-000000550 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 550
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[549].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 956. PFQ-fundamentals-000000550 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 550
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[549].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 957. PFQ-fundamentals-000000551 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 551
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[550].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 958. PFQ-fundamentals-000000552 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 552
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[551].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 959. PFQ-fundamentals-000000553 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 553
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[552].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 960. PFQ-fundamentals-000000554 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 554
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[553].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 961. PFQ-fundamentals-000000555 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 555
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[554].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 962. PFQ-fundamentals-000000556 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 556
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[555].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 963. PFQ-fundamentals-000000557 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 557
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[556].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 964. PFQ-fundamentals-000000557 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 557
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[556].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 965. PFQ-fundamentals-000000558 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 558
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[557].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 966. PFQ-fundamentals-000000559 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 559
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[558].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 967. PFQ-fundamentals-000000559 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 559
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[558].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 968. PFQ-fundamentals-000000560 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 560
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[559].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 969. PFQ-fundamentals-000000561 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 561
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[560].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 970. PFQ-fundamentals-000000562 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 562
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[561].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 971. PFQ-fundamentals-000000562 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 562
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[561].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 972. PFQ-fundamentals-000000563 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 563
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[562].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 973. PFQ-fundamentals-000000564 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 564
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[563].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 974. PFQ-fundamentals-000000564 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 564
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[563].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 975. PFQ-fundamentals-000000565 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 565
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[564].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 976. PFQ-fundamentals-000000566 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 566
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[565].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["A", "B", "D", "E", "B", "C"]
```

### 977. PFQ-fundamentals-000000566 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 566
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[565].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 978. PFQ-fundamentals-000000566 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 566
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[565].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 979. PFQ-fundamentals-000000567 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 567
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[566].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 980. PFQ-fundamentals-000000567 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 567
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[566].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 981. PFQ-fundamentals-000000568 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 568
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[567].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 982. PFQ-fundamentals-000000568 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 568
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[567].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 983. PFQ-fundamentals-000000569 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 569
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[568].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 984. PFQ-fundamentals-000000570 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 570
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[569].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 985. PFQ-fundamentals-000000570 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 570
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[569].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 986. PFQ-fundamentals-000000571 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 571
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[570].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 987. PFQ-fundamentals-000000571 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 571
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[570].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 988. PFQ-fundamentals-000000572 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 572
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[571].stem`
- Detail: Pattern requires human review against the original source.

```text
The home health care nurse eNd u cRa tUe sIpSa tGiNe n tBs .o nCw hMi c h goals of hospice care? (Select all thatapply.)
```

### 989. PFQ-fundamentals-000000572 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 572
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[571].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 990. PFQ-fundamentals-000000572 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 572
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[571].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 991. PFQ-fundamentals-000000572 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 572
- Chapter: Public Health, Community-Based, and Home Health Care
- JSON path: `$.questions[571].rationale`
- Detail: Known source or extraction contamination detected.

```text
The goals of hospice care include relief of suffering, supporting the family and patient, and providing grief support after the patient dies. Goals do not include keeping patients out of the hospital or lowering medical costs. 3rd Edition
```

### 992. PFQ-fundamentals-000000573 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 573
- Chapter: Human Sexuality
- JSON path: `$.questions[572].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 993. PFQ-fundamentals-000000573 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 573
- Chapter: Human Sexuality
- JSON path: `$.questions[572].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 994. PFQ-fundamentals-000000574 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 574
- Chapter: Human Sexuality
- JSON path: `$.questions[573].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 995. PFQ-fundamentals-000000575 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 575
- Chapter: Human Sexuality
- JSON path: `$.questions[574].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 996. PFQ-fundamentals-000000576 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 576
- Chapter: Human Sexuality
- JSON path: `$.questions[575].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 997. PFQ-fundamentals-000000577 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 577
- Chapter: Human Sexuality
- JSON path: `$.questions[576].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 998. PFQ-fundamentals-000000578 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 578
- Chapter: Human Sexuality
- JSON path: `$.questions[577].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 999. PFQ-fundamentals-000000578 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 578
- Chapter: Human Sexuality
- JSON path: `$.questions[577].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1000. PFQ-fundamentals-000000579 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 579
- Chapter: Human Sexuality
- JSON path: `$.questions[578].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1001. PFQ-fundamentals-000000579 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 579
- Chapter: Human Sexuality
- JSON path: `$.questions[578].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1002. PFQ-fundamentals-000000580 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 580
- Chapter: Human Sexuality
- JSON path: `$.questions[579].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1003. PFQ-fundamentals-000000581 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 581
- Chapter: Human Sexuality
- JSON path: `$.questions[580].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1004. PFQ-fundamentals-000000582 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 582
- Chapter: Human Sexuality
- JSON path: `$.questions[581].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1005. PFQ-fundamentals-000000582 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 582
- Chapter: Human Sexuality
- JSON path: `$.questions[581].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1006. PFQ-fundamentals-000000583 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 583
- Chapter: Human Sexuality
- JSON path: `$.questions[582].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1007. PFQ-fundamentals-000000583 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 583
- Chapter: Human Sexuality
- JSON path: `$.questions[582].rationale`
- Detail: Known source or extraction contamination detected.

```text
The PLISSIT model is a framework for addressing sexuality. In the SS (specific suggestions) phase, the nurse provides information that allows the patient to proceed with sexual relation s. Informing the patient about sNexUuRalSpIosNitiGoTnsBth.aCt aOr eMl e s s stressful on the …
```

### 1008. PFQ-fundamentals-000000583 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 583
- Chapter: Human Sexuality
- JSON path: `$.questions[582].rationale`
- Detail: Pattern requires human review against the original source.

```text
The PLISSIT model is a framework for addressing sexuality. In the SS (specific suggestions) phase, the nurse provides information that allows the patient to proceed with sexual relation s. Informing the patient about sNexUuRalSpIosNitiGoTnsBth.aCt aOr eMl e s s stressful on the …
```

### 1009. PFQ-fundamentals-000000584 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 584
- Chapter: Human Sexuality
- JSON path: `$.questions[583].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1010. PFQ-fundamentals-000000584 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 584
- Chapter: Human Sexuality
- JSON path: `$.questions[583].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1011. PFQ-fundamentals-000000585 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 585
- Chapter: Human Sexuality
- JSON path: `$.questions[584].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1012. PFQ-fundamentals-000000586 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 586
- Chapter: Human Sexuality
- JSON path: `$.questions[585].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1013. PFQ-fundamentals-000000587 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 587
- Chapter: Human Sexuality
- JSON path: `$.questions[586].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1014. PFQ-fundamentals-000000587 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 587
- Chapter: Human Sexuality
- JSON path: `$.questions[586].rationale`
- Detail: Pattern requires human review against the original source.

```text
Ineffective sexuality patterns refer to a patient who expresses concern about his/her own sexuality. This patient is concerned about the effect of this surgery on his/her attractiveness and desirability. Sexual dysfunction relates more to the physical problems. The patient may h…
```

### 1015. PFQ-fundamentals-000000587 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 587
- Chapter: Human Sexuality
- JSON path: `$.questions[586].rationale`
- Detail: Pattern requires human review against the original source.

```text
Ineffective sexuality patterns refer to a patient who expresses concern about his/her own sexuality. This patient is concerned about the effect of this surgery on his/her attractiveness and desirability. Sexual dysfunction relates more to the physical problems. The patient may h…
```

### 1016. PFQ-fundamentals-000000588 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 588
- Chapter: Human Sexuality
- JSON path: `$.questions[587].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1017. PFQ-fundamentals-000000589 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 589
- Chapter: Human Sexuality
- JSON path: `$.questions[588].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1018. PFQ-fundamentals-000000590 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 590
- Chapter: Human Sexuality
- JSON path: `$.questions[589].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1019. PFQ-fundamentals-000000590 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 590
- Chapter: Human Sexuality
- JSON path: `$.questions[589].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1020. PFQ-fundamentals-000000591 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 591
- Chapter: Human Sexuality
- JSON path: `$.questions[590].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1021. PFQ-fundamentals-000000591 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 591
- Chapter: Human Sexuality
- JSON path: `$.questions[590].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1022. PFQ-fundamentals-000000592 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 592
- Chapter: Human Sexuality
- JSON path: `$.questions[591].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1023. PFQ-fundamentals-000000592 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 592
- Chapter: Human Sexuality
- JSON path: `$.questions[591].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1024. PFQ-fundamentals-000000593 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 593
- Chapter: Human Sexuality
- JSON path: `$.questions[592].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1025. PFQ-fundamentals-000000593 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 593
- Chapter: Human Sexuality
- JSON path: `$.questions[592].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1026. PFQ-fundamentals-000000594 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 594
- Chapter: Human Sexuality
- JSON path: `$.questions[593].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1027. PFQ-fundamentals-000000594 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 594
- Chapter: Human Sexuality
- JSON path: `$.questions[593].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1028. PFQ-fundamentals-000000595 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 595
- Chapter: Human Sexuality
- JSON path: `$.questions[594].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1029. PFQ-fundamentals-000000595 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 595
- Chapter: Human Sexuality
- JSON path: `$.questions[594].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1030. PFQ-fundamentals-000000596 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 596
- Chapter: Human Sexuality
- JSON path: `$.questions[595].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1031. PFQ-fundamentals-000000596 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 596
- Chapter: Human Sexuality
- JSON path: `$.questions[595].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1032. PFQ-fundamentals-000000597 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 597
- Chapter: Human Sexuality
- JSON path: `$.questions[596].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1033. PFQ-fundamentals-000000597 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 597
- Chapter: Human Sexuality
- JSON path: `$.questions[596].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1034. PFQ-fundamentals-000000597 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 597
- Chapter: Human Sexuality
- JSON path: `$.questions[596].rationale`
- Detail: Known source or extraction contamination detected.

```text
Fatigue, medications, pain, and impairments all can have direct effects on sexuality. Lifestyle is another factor, but occupation does not in itself influence sexuality. 3rd Edition
```

### 1035. PFQ-fundamentals-000000598 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 598
- Chapter: Safety
- JSON path: `$.questions[597].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1036. PFQ-fundamentals-000000599 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 599
- Chapter: Safety
- JSON path: `$.questions[598].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1037. PFQ-fundamentals-000000599 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 599
- Chapter: Safety
- JSON path: `$.questions[598].rationale`
- Detail: Known source or extraction contamination detected.

```text
Impairments in the musculoskeletal system can impact mobility through restrictions of range of motion and strength, increasing the chances of falling. Changes to the neurologic system can impair cognitive functioning, changes to the hepatic system can affect mental status, and c…
```

### 1038. PFQ-fundamentals-000000600 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 600
- Chapter: Safety
- JSON path: `$.questions[599].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1039. PFQ-fundamentals-000000600 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 600
- Chapter: Safety
- JSON path: `$.questions[599].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1040. PFQ-fundamentals-000000601 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 601
- Chapter: Safety
- JSON path: `$.questions[600].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1041. PFQ-fundamentals-000000602 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 602
- Chapter: Safety
- JSON path: `$.questions[601].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1042. PFQ-fundamentals-000000602 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 602
- Chapter: Safety
- JSON path: `$.questions[601].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1043. PFQ-fundamentals-000000603 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 603
- Chapter: Safety
- JSON path: `$.questions[602].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1044. PFQ-fundamentals-000000603 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 603
- Chapter: Safety
- JSON path: `$.questions[602].rationale`
- Detail: Pattern requires human review against the original source.

```text
Firearms should be stored in a secure location with trigger locks in place. Ammunition should be stored in a separate location also locked. Proper permits should be obtained a s appropriate. Loaded firearms should never be stored where children can access them.
```

### 1045. PFQ-fundamentals-000000604 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 604
- Chapter: Safety
- JSON path: `$.questions[603].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1046. PFQ-fundamentals-000000605 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 605
- Chapter: Safety
- JSON path: `$.questions[604].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1047. PFQ-fundamentals-000000606 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 606
- Chapter: Safety
- JSON path: `$.questions[605].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1048. PFQ-fundamentals-000000606 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 606
- Chapter: Safety
- JSON path: `$.questions[605].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1049. PFQ-fundamentals-000000607 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 607
- Chapter: Safety
- JSON path: `$.questions[606].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1050. PFQ-fundamentals-000000608 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 608
- Chapter: Safety
- JSON path: `$.questions[607].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1051. PFQ-fundamentals-000000609 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 609
- Chapter: Safety
- JSON path: `$.questions[608].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1052. PFQ-fundamentals-000000609 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 609
- Chapter: Safety
- JSON path: `$.questions[608].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1053. PFQ-fundamentals-000000609 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 609
- Chapter: Safety
- JSON path: `$.questions[608].rationale`
- Detail: Known source or extraction contamination detected.

```text
The Glasgow is a coma scale used to measure level of consciousness, not falls. The rest are scales used to assess the risk for falls in patients. NCLEX Client Needs Category: Safe and Effective Care
```

### 1054. PFQ-fundamentals-000000610 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 610
- Chapter: Safety
- JSON path: `$.questions[609].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1055. PFQ-fundamentals-000000611 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 611
- Chapter: Safety
- JSON path: `$.questions[610].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1056. PFQ-fundamentals-000000612 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 612
- Chapter: Safety
- JSON path: `$.questions[611].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1057. PFQ-fundamentals-000000613 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 613
- Chapter: Safety
- JSON path: `$.questions[612].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1058. PFQ-fundamentals-000000614 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 614
- Chapter: Safety
- JSON path: `$.questions[613].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1059. PFQ-fundamentals-000000615 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 615
- Chapter: Safety
- JSON path: `$.questions[614].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1060. PFQ-fundamentals-000000615 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 615
- Chapter: Safety
- JSON path: `$.questions[614].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1061. PFQ-fundamentals-000000616 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 616
- Chapter: Safety
- JSON path: `$.questions[615].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1062. PFQ-fundamentals-000000616 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 616
- Chapter: Safety
- JSON path: `$.questions[615].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1063. PFQ-fundamentals-000000617 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 617
- Chapter: Safety
- JSON path: `$.questions[616].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a confused, combative patient. Which action would be considered last by the nurse to control behavNior Rof thIe clGi entB? .C M
```

### 1064. PFQ-fundamentals-000000617 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 617
- Chapter: Safety
- JSON path: `$.questions[616].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1065. PFQ-fundamentals-000000617 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 617
- Chapter: Safety
- JSON path: `$.questions[616].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Apply restraints. S N T O
```

### 1066. PFQ-fundamentals-000000618 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 618
- Chapter: Safety
- JSON path: `$.questions[617].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1067. PFQ-fundamentals-000000619 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 619
- Chapter: Safety
- JSON path: `$.questions[618].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1068. PFQ-fundamentals-000000620 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 620
- Chapter: Safety
- JSON path: `$.questions[619].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1069. PFQ-fundamentals-000000621 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 621
- Chapter: Safety
- JSON path: `$.questions[620].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1070. PFQ-fundamentals-000000622 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1071. PFQ-fundamentals-000000622 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1072. PFQ-fundamentals-000000622 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].rationale`
- Detail: Known source or extraction contamination detected.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 1073. PFQ-fundamentals-000000622 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].rationale`
- Detail: Pattern requires human review against the original source.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 1074. PFQ-fundamentals-000000622 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].rationale`
- Detail: Pattern requires human review against the original source.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 1075. PFQ-fundamentals-000000622 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 622
- Chapter: Safety
- JSON path: `$.questions[621].rationale`
- Detail: Pattern requires human review against the original source.

```text
Inadequate lighting presents safety concerns in home, work, community, and health care environments. For an individual to safely and successfully navigate pathways and perform various activities while avoiding potential obstacles and hazards, the environment must be well illumin…
```

### 1076. PFQ-fundamentals-000000623 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 623
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[622].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1077. PFQ-fundamentals-000000623 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 623
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[622].rationale`
- Detail: Known source or extraction contamination detected.

```text
The second line of defense is the inflammatory response. Inflammation is a local response to cellular injury or infection that includes capillary dilation and leukocyte infiltration. Normal flora is the body‘s first line of defense. The immune response is the body‘s attempt to p…
```

### 1078. PFQ-fundamentals-000000624 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 624
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[623].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1079. PFQ-fundamentals-000000624 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 624
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[623].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1080. PFQ-fundamentals-000000624 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 624
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[623].rationale`
- Detail: Known source or extraction contamination detected.

```text
U S N T O Humoral immunity is a defense system that involves antibodies and white blood cells that are produced to fight antigens. Cellular immunity involves defense by white blood cells against any microorganisms that the body does not recognize as its own. The innate (nonspeci…
```

### 1081. PFQ-fundamentals-000000624 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 624
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[623].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O Humoral immunity is a defense system that involves antibodies and white blood cells that are produced to fight antigens. Cellular immunity involves defense by white blood cells against any microorganisms that the body does not recognize as its own. The innate (nonspeci…
```

### 1082. PFQ-fundamentals-000000625 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 625
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[624].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1083. PFQ-fundamentals-000000625 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 625
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[624].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1084. PFQ-fundamentals-000000625 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 625
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[624].rationale`
- Detail: Known source or extraction contamination detected.

```text
Infectious agents include any disease-causing agent and are called pathogens. They include bacteria, fungi, viruses, and parasites. Normal flora is a group of non–disease-causing microorganisms that live in or on the body. Germ is a term used for microorganism. A microorganism i…
```

### 1085. PFQ-fundamentals-000000626 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 626
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[625].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1086. PFQ-fundamentals-000000627 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 627
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[626].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1087. PFQ-fundamentals-000000628 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 628
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[627].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1088. PFQ-fundamentals-000000628 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 628
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[627].rationale`
- Detail: Pattern requires human review against the original source.

```text
The stethoscope would be a means for the pathogen to travel from source t o host. The source is the reservoir or host. The portal of exit is where the pathogen escapes from the reservoir of infection, and the portal of entry is where the microorganism enters the susceptible host.
```

### 1089. PFQ-fundamentals-000000629 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 629
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[628].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1090. PFQ-fundamentals-000000629 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 629
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[628].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1091. PFQ-fundamentals-000000630 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 630
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[629].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1092. PFQ-fundamentals-000000631 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 631
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[630].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1093. PFQ-fundamentals-000000631 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 631
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[630].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1094. PFQ-fundamentals-000000631 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 631
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[630].rationale`
- Detail: Pattern requires human review against the original source.

```text
The 80-year-old male has more risk factors because he is elderly and has increased risk of urinary tract infection related to prostate enlargement, so he has two risk factors. A 24-year-old female runner is likely healthy with no additional risk factors. The 50-year-old obese ma…
```

### 1095. PFQ-fundamentals-000000631 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 631
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[630].rationale`
- Detail: Pattern requires human review against the original source.

```text
The 80-year-old male has more risk factors because he is elderly and has increased risk of urinary tract infection related to prostate enlargement, so he has two risk factors. A 24-year-old female runner is likely healthy with no additional risk factors. The 50-year-old obese ma…
```

### 1096. PFQ-fundamentals-000000632 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 632
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[631].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1097. PFQ-fundamentals-000000633 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 633
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[632].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1098. PFQ-fundamentals-000000634 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 634
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[633].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1099. PFQ-fundamentals-000000635 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 635
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[634].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1100. PFQ-fundamentals-000000635 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 635
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[634].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1101. PFQ-fundamentals-000000636 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 636
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[635].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1102. PFQ-fundamentals-000000636 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 636
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[635].rationale`
- Detail: Pattern requires human review against the original source.

```text
Soap and water must be used to thoroughly clean hands if there is any visible soiling or dirt and with certain infections such as Clostridium difficile and vancomycin-resistant enterococci when preparing for a sterile or surgical procedure, before and after eating, and after usi…
```

### 1103. PFQ-fundamentals-000000637 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 637
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[636].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1104. PFQ-fundamentals-000000638 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 638
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[637].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1105. PFQ-fundamentals-000000639 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 639
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[638].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1106. PFQ-fundamentals-000000639 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 639
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[638].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1107. PFQ-fundamentals-000000639 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 639
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[638].rationale`
- Detail: Pattern requires human review against the original source.

```text
Droplet precautions are used when known or suspected contagious diseases can be transmitted through large droplets suspenNdedRin It h e GaUi r. SBCo.nCtNactMprecaution s are used when a known orsuspected contagious disease may be present and is transmitted through direct contact…
```

### 1108. PFQ-fundamentals-000000640 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 640
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[639].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1109. PFQ-fundamentals-000000640 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 640
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[639].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1110. PFQ-fundamentals-000000641 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 641
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[640].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1111. PFQ-fundamentals-000000642 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 642
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[641].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1112. PFQ-fundamentals-000000642 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 642
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[641].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
Increased sputum produc NtioUnRSINGTB.COM
```

### 1113. PFQ-fundamentals-000000642 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 642
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[641].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1114. PFQ-fundamentals-000000642 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 642
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[641].rationale`
- Detail: Pattern requires human review against the original source.

```text
The elderly are at an increased risk for respiratory infections because of d ecreased cough reflex, decreased elastic recoil of the lungs, decreased activity of the cilia, and abnormal swallowing reflex. They do not generally have increased sputum production.
```

### 1115. PFQ-fundamentals-000000643 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 643
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[642].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1116. PFQ-fundamentals-000000643 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 643
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[642].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1117. PFQ-fundamentals-000000644 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 644
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[643].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1118. PFQ-fundamentals-000000644 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 644
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[643].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1119. PFQ-fundamentals-000000645 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 645
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[644].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1120. PFQ-fundamentals-000000645 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 645
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[644].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1121. PFQ-fundamentals-000000646 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 646
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[645].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1122. PFQ-fundamentals-000000646 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 646
- Chapter: Asepsis and Infection Control
- JSON path: `$.questions[645].rationale`
- Detail: Known source or extraction contamination detected.

```text
Protective precautions may require a positive-pressure room. No live plants, fresh flowers, fresh raw fruit or vegetables, sushi, or blue cheese may be brought into the room because they may harbor bacteria and fungi. The patient cannot eat just any foods because some are restri…
```

### 1123. PFQ-fundamentals-000000647 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 647
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[646].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1124. PFQ-fundamentals-000000647 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 647
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[646].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1125. PFQ-fundamentals-000000648 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 648
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[647].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1126. PFQ-fundamentals-000000649 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 649
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[648].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1127. PFQ-fundamentals-000000650 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 650
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[649].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1128. PFQ-fundamentals-000000650 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 650
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[649].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1129. PFQ-fundamentals-000000651 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 651
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[650].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1130. PFQ-fundamentals-000000652 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 652
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[651].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1131. PFQ-fundamentals-000000653 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 653
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[652].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1132. PFQ-fundamentals-000000653 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 653
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[652].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1133. PFQ-fundamentals-000000654 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 654
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[653].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "B", "C"]
```

### 1134. PFQ-fundamentals-000000654 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 654
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[653].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1135. PFQ-fundamentals-000000655 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 655
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[654].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1136. PFQ-fundamentals-000000656 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 656
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[655].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1137. PFQ-fundamentals-000000657 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 657
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[656].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1138. PFQ-fundamentals-000000658 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 658
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[657].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1139. PFQ-fundamentals-000000659 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 659
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[658].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1140. PFQ-fundamentals-000000659 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 659
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[658].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1141. PFQ-fundamentals-000000660 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 660
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[659].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1142. PFQ-fundamentals-000000660 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 660
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[659].rationale`
- Detail: Pattern requires human review against the original source.

```text
Oral care is important regardless of medication, but a soft-bristled toothbrush should be used related to increased risk of bleeding for any patient on an anticoagulant. An electric toothbrush is too aggressive,NanUdRmSoIutNhwGaTsBh .is Cn oOt Ma dequate.
```

### 1143. PFQ-fundamentals-000000661 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 661
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[660].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1144. PFQ-fundamentals-000000661 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 661
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[660].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1145. PFQ-fundamentals-000000662 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 662
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[661].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1146. PFQ-fundamentals-000000662 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 662
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[661].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1147. PFQ-fundamentals-000000663 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 663
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[662].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1148. PFQ-fundamentals-000000664 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 664
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[663].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1149. PFQ-fundamentals-000000665 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 665
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[664].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1150. PFQ-fundamentals-000000666 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 666
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[665].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1151. PFQ-fundamentals-000000667 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 667
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[666].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1152. PFQ-fundamentals-000000667 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 667
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[666].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1153. PFQ-fundamentals-000000668 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 668
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[667].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1154. PFQ-fundamentals-000000669 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 669
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[668].stem`
- Detail: Pattern requires human review against the original source.

```text
Regarding perineal care, whiNchUnRuSrsiInNg GacTtioBn.s CarOe Mappropriate? ( Select all that apply.)
```

### 1155. PFQ-fundamentals-000000669 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 669
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[668].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1156. PFQ-fundamentals-000000669 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 669
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[668].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1157. PFQ-fundamentals-000000670 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 670
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[669].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1158. PFQ-fundamentals-000000670 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 670
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[669].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Patients with diabetes U S N
```

### 1159. PFQ-fundamentals-000000670 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 670
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[669].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1160. PFQ-fundamentals-000000670 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 670
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[669].rationale`
- Detail: Pattern requires human review against the original source.

```text
Soaking the feet of patients with peripheral vascular disease, cardiovascular disease s uch as strokes and diabetes are contraindicated because it may cause skin breakdown or inf ection. Patient with arthritis or malnourished have no contraindications to having their feet soaked.
```

### 1161. PFQ-fundamentals-000000671 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 671
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[670].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1162. PFQ-fundamentals-000000671 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 671
- Chapter: Hygiene and Personal Care
- JSON path: `$.questions[670].rationale`
- Detail: Known source or extraction contamination detected.

```text
Apply warm water and a conditioner or a detangler, if available, to release tangles and avoid injury to the scalp. Use a comb and/or fingers to work through the tangles individually before shampooing. The nurse avoids cutting the patient‘s hair unless first asking the patient‘s …
```

### 1163. PFQ-fundamentals-000000672 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 672
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[671].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1164. PFQ-fundamentals-000000672 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 672
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[671].rationale`
- Detail: Known source or extraction contamination detected.

```text
Rheumatoid arthritis and osteoarthritis cause inflammation of joints, resulting in pa in and limited joint mobility, not muscle mobility. Genetic disorders such as muscular d ystrophy result in muscle weakness and gradual muscle wasting. Spasticity (increased muscle tone) occurs…
```

### 1165. PFQ-fundamentals-000000673 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 673
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[672].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1166. PFQ-fundamentals-000000673 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 673
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[672].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
The bed is placed in the lNo w Rp o s iIt io nG. B.CM
```

### 1167. PFQ-fundamentals-000000673 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 673
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[672].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
The patient is wearing s oc kUs. SNT O
```

### 1168. PFQ-fundamentals-000000673 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 673
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[672].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
The patient is wearing s oc kUs. SNT O
```

### 1169. PFQ-fundamentals-000000674 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 674
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[673].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1170. PFQ-fundamentals-000000675 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 675
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[674].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1171. PFQ-fundamentals-000000677 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 677
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[676].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1172. PFQ-fundamentals-000000678 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 678
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[677].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1173. PFQ-fundamentals-000000679 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 679
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[678].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1174. PFQ-fundamentals-000000680 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 680
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[679].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1175. PFQ-fundamentals-000000681 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 681
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[680].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1176. PFQ-fundamentals-000000682 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 682
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[681].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1177. PFQ-fundamentals-000000683 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 683
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[682].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1178. PFQ-fundamentals-000000684 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 684
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[683].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1179. PFQ-fundamentals-000000685 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 685
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[684].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1180. PFQ-fundamentals-000000686 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 686
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[685].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1181. PFQ-fundamentals-000000687 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 687
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[686].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1182. PFQ-fundamentals-000000687 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 687
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[686].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
―I wish I could reduce myNrUisRkSbuItNI GcaTn‘Bt .d oCaOn Myt h i n g.‖
```

### 1183. PFQ-fundamentals-000000687 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 687
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[686].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1184. PFQ-fundamentals-000000688 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 688
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[687].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1185. PFQ-fundamentals-000000688 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 688
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[687].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1186. PFQ-fundamentals-000000689 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 689
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[688].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1187. PFQ-fundamentals-000000690 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 690
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[689].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1188. PFQ-fundamentals-000000690 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 690
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[689].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1189. PFQ-fundamentals-000000691 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 691
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[690].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1190. PFQ-fundamentals-000000692 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 692
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[691].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1191. PFQ-fundamentals-000000692 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 692
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[691].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1192. PFQ-fundamentals-000000693 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 693
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[692].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1193. PFQ-fundamentals-000000693 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 693
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[692].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The nurse stands behind tNheUpRaStinIeNt wGhTilBe .a mCbOuMlat ing.
```

### 1194. PFQ-fundamentals-000000693 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 693
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[692].choices[4].text`
- Detail: Pattern requires human review against the original source.

```text
The nurse stands behind tNheUpRaStinIeNt wGhTilBe .a mCbOuMlat ing.
```

### 1195. PFQ-fundamentals-000000694 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 694
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[693].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1196. PFQ-fundamentals-000000695 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 695
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[694].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1197. PFQ-fundamentals-000000695 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 695
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[694].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1198. PFQ-fundamentals-000000696 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 696
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[695].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1199. PFQ-fundamentals-000000696 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 696
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[695].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1200. PFQ-fundamentals-000000696 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 696
- Chapter: Activity, Immobility, and Safe Movement
- JSON path: `$.questions[695].rationale`
- Detail: Known source or extraction contamination detected.

```text
Proper positioning of the SCD sleeve allows proper fit and application, which decreases the risk of constricting the blood flow or diminishing optimal outcomes. Wrap the sleeve around the leg and fasten it with Velcro straps. Verify that two fingers fit between the leg and the s…
```

### 1201. PFQ-fundamentals-000000697 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 697
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[696].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1202. PFQ-fundamentals-000000697 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 697
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[696].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1203. PFQ-fundamentals-000000698 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 698
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[697].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1204. PFQ-fundamentals-000000699 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 699
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[698].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1205. PFQ-fundamentals-000000700 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 700
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[699].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1206. PFQ-fundamentals-000000701 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 701
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[700].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1207. PFQ-fundamentals-000000702 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 702
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[701].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1208. PFQ-fundamentals-000000703 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 703
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[702].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1209. PFQ-fundamentals-000000703 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 703
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[702].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1210. PFQ-fundamentals-000000704 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 704
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[703].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1211. PFQ-fundamentals-000000705 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 705
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[704].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1212. PFQ-fundamentals-000000706 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 706
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[705].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1213. PFQ-fundamentals-000000706 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 706
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[705].rationale`
- Detail: Pattern requires human review against the original source.

```text
Occlusive dressings such as hydrocolloids and transparent films are used for autolytic debridement and are contraindicated in infected wounds. It is the most comfortable form of debridement for the patient. Nty R IGB.CM U S N T O
```

### 1214. PFQ-fundamentals-000000706 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 706
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[705].rationale`
- Detail: Pattern requires human review against the original source.

```text
Occlusive dressings such as hydrocolloids and transparent films are used for autolytic debridement and are contraindicated in infected wounds. It is the most comfortable form of debridement for the patient. Nty R IGB.CM U S N T O
```

### 1215. PFQ-fundamentals-000000707 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 707
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[706].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1216. PFQ-fundamentals-000000708 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 708
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[707].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1217. PFQ-fundamentals-000000709 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 709
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[708].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1218. PFQ-fundamentals-000000710 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 710
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[709].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1219. PFQ-fundamentals-000000711 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 711
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[710].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1220. PFQ-fundamentals-000000712 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 712
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[711].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1221. PFQ-fundamentals-000000713 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 713
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[712].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1222. PFQ-fundamentals-000000714 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 714
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[713].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1223. PFQ-fundamentals-000000714 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 714
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[713].rationale`
- Detail: Known source or extraction contamination detected.

```text
Stage 3 pressure ulcers are full-thickness wounds that extend into the subcutaneous tissue but do not extend through the fascia to muscle, bone, or connective tissue. There may be undermining or tunneling present in the wound. Stage 4 pressure ulcers involve exposure of muscle, …
```

### 1224. PFQ-fundamentals-000000715 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 715
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[714].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1225. PFQ-fundamentals-000000716 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 716
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[715].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1226. PFQ-fundamentals-000000716 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 716
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[715].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1227. PFQ-fundamentals-000000717 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 717
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[716].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1228. PFQ-fundamentals-000000717 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 717
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[716].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1229. PFQ-fundamentals-000000718 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 718
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[717].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1230. PFQ-fundamentals-000000718 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 718
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[717].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1231. PFQ-fundamentals-000000719 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 719
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[718].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1232. PFQ-fundamentals-000000719 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 719
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[718].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1233. PFQ-fundamentals-000000719 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 719
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[718].rationale`
- Detail: Known source or extraction contamination detected.

```text
The Braden scale ranks the patient on the risk categories of sensory perception, moisture, activity, mobility, nutrition, and friction and shear. The scale does not include cognition. NCLEX Client Needs Category: Physiological Integrity: Physiological Adaptation
```

### 1234. PFQ-fundamentals-000000720 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 720
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[719].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1235. PFQ-fundamentals-000000721 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 721
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[720].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1236. PFQ-fundamentals-000000721 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 721
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[720].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1237. PFQ-fundamentals-000000721 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 721
- Chapter: Skin Integrity and Wound Care
- JSON path: `$.questions[720].rationale`
- Detail: Known source or extraction contamination detected.

```text
Cold should not be used if any of the following is present: edema (cold application slows reabsorption of the fluid), circulatory pathophysiology (cold application causes vasoconstriction, further reducing circulation to the area), and shivering (this is a comfort concern). Blee…
```

### 1238. PFQ-fundamentals-000000722 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 722
- Chapter: Nutrition
- JSON path: `$.questions[721].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1239. PFQ-fundamentals-000000723 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 723
- Chapter: Nutrition
- JSON path: `$.questions[722].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1240. PFQ-fundamentals-000000724 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 724
- Chapter: Nutrition
- JSON path: `$.questions[723].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1241. PFQ-fundamentals-000000725 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 725
- Chapter: Nutrition
- JSON path: `$.questions[724].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1242. PFQ-fundamentals-000000726 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 726
- Chapter: Nutrition
- JSON path: `$.questions[725].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1243. PFQ-fundamentals-000000727 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 727
- Chapter: Nutrition
- JSON path: `$.questions[726].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is performing an oral examination on a patient and notices a beefy-red tongue. The nurse identifies this as a characteristic finding for what condition? U S N
```

### 1244. PFQ-fundamentals-000000727 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 727
- Chapter: Nutrition
- JSON path: `$.questions[726].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1245. PFQ-fundamentals-000000727 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 727
- Chapter: Nutrition
- JSON path: `$.questions[726].rationale`
- Detail: Known source or extraction contamination detected.

```text
In conditions such as pernicious anemia, a characteristic finding is a sore, smooth-surfaced, beefy-red tongue, which may interfere with the person‘s ability to chew certain foods. Anorexia nervosa and bulimia are eating disorders. In malnutrition the oral mucosa may be a darker…
```

### 1246. PFQ-fundamentals-000000728 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 728
- Chapter: Nutrition
- JSON path: `$.questions[727].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1247. PFQ-fundamentals-000000728 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 728
- Chapter: Nutrition
- JSON path: `$.questions[727].rationale`
- Detail: Pattern requires human review against the original source.

```text
During feeding, the head of the bed needs to be elevated at 30 to 45 degrees or higher. Liquids are thickened, and patients are encouraged to use slow-eating habits and to alternate between bites of food and sips of fluids to facilitate swallowing. N. 6 RIGTOBP:.ECvalMuation Con…
```

### 1248. PFQ-fundamentals-000000729 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 729
- Chapter: Nutrition
- JSON path: `$.questions[728].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1249. PFQ-fundamentals-000000730 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 730
- Chapter: Nutrition
- JSON path: `$.questions[729].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1250. PFQ-fundamentals-000000730 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 730
- Chapter: Nutrition
- JSON path: `$.questions[729].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
―I can give the patient orange juice.‖ U S N
```

### 1251. PFQ-fundamentals-000000731 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 731
- Chapter: Nutrition
- JSON path: `$.questions[730].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1252. PFQ-fundamentals-000000731 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 731
- Chapter: Nutrition
- JSON path: `$.questions[730].rationale`
- Detail: Pattern requires human review against the original source.

```text
Renal diets restrict potassium, sodium, protein, and phosphorous intake. Fresh fruits (except bananas) and vegetables are excellent dietary choices for individuals on a renal diet. Meats, processed foods, peanut butter, cheese, nuts, caramels, ice cream, and colas are typically …
```

### 1253. PFQ-fundamentals-000000732 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 732
- Chapter: Nutrition
- JSON path: `$.questions[731].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1254. PFQ-fundamentals-000000733 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 733
- Chapter: Nutrition
- JSON path: `$.questions[732].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1255. PFQ-fundamentals-000000733 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 733
- Chapter: Nutrition
- JSON path: `$.questions[732].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Flushes the tube with a small amount of air. U S N
```

### 1256. PFQ-fundamentals-000000734 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 734
- Chapter: Nutrition
- JSON path: `$.questions[733].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1257. PFQ-fundamentals-000000735 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 735
- Chapter: Nutrition
- JSON path: `$.questions[734].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1258. PFQ-fundamentals-000000736 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 736
- Chapter: Nutrition
- JSON path: `$.questions[735].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1259. PFQ-fundamentals-000000737 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 737
- Chapter: Nutrition
- JSON path: `$.questions[736].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1260. PFQ-fundamentals-000000737 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 737
- Chapter: Nutrition
- JSON path: `$.questions[736].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1261. PFQ-fundamentals-000000738 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 738
- Chapter: Nutrition
- JSON path: `$.questions[737].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1262. PFQ-fundamentals-000000738 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 738
- Chapter: Nutrition
- JSON path: `$.questions[737].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1263. PFQ-fundamentals-000000739 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 739
- Chapter: Nutrition
- JSON path: `$.questions[738].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1264. PFQ-fundamentals-000000739 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 739
- Chapter: Nutrition
- JSON path: `$.questions[738].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1265. PFQ-fundamentals-000000740 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 740
- Chapter: Nutrition
- JSON path: `$.questions[739].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1266. PFQ-fundamentals-000000740 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 740
- Chapter: Nutrition
- JSON path: `$.questions[739].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1267. PFQ-fundamentals-000000741 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 741
- Chapter: Nutrition
- JSON path: `$.questions[740].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1268. PFQ-fundamentals-000000741 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 741
- Chapter: Nutrition
- JSON path: `$.questions[740].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1269. PFQ-fundamentals-000000742 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 742
- Chapter: Nutrition
- JSON path: `$.questions[741].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1270. PFQ-fundamentals-000000742 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 742
- Chapter: Nutrition
- JSON path: `$.questions[741].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1271. PFQ-fundamentals-000000742 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 742
- Chapter: Nutrition
- JSON path: `$.questions[741].rationale`
- Detail: Known source or extraction contamination detected.

```text
Deficiencies of vitamin C interfere with normal tissue synthesis and may result in gingivitis, which produces swollen and NblUeeRdiSnIg NguGmTsBw.itCh loMo se ned teeth, and painful, stiff joints. Other problems associated with malabsorption include anemia (a deficiency of red b…
```

### 1272. PFQ-fundamentals-000000743 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 743
- Chapter: Nutrition
- JSON path: `$.questions[742].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1273. PFQ-fundamentals-000000743 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 743
- Chapter: Nutrition
- JSON path: `$.questions[742].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1274. PFQ-fundamentals-000000743 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 743
- Chapter: Nutrition
- JSON path: `$.questions[742].rationale`
- Detail: Pattern requires human review against the original source.

```text
As BMI levels rise, blood pressure and cholesterol levels also rise and the average high- density lipoprotein (HDL), or good, cholesterol levels decrease. Hyperlipidemia (elevation of plasma cholesterol, triglycerides, or both) or low HDL levels contribute to the development of …
```

### 1275. PFQ-fundamentals-000000744 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 744
- Chapter: Nutrition
- JSON path: `$.questions[743].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1276. PFQ-fundamentals-000000744 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 744
- Chapter: Nutrition
- JSON path: `$.questions[743].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1277. PFQ-fundamentals-000000745 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 745
- Chapter: Nutrition
- JSON path: `$.questions[744].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1278. PFQ-fundamentals-000000745 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 745
- Chapter: Nutrition
- JSON path: `$.questions[744].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1279. PFQ-fundamentals-000000746 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 746
- Chapter: Nutrition
- JSON path: `$.questions[745].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1280. PFQ-fundamentals-000000746 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 746
- Chapter: Nutrition
- JSON path: `$.questions[745].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1281. PFQ-fundamentals-000000747 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 747
- Chapter: Nutrition
- JSON path: `$.questions[746].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1282. PFQ-fundamentals-000000747 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 747
- Chapter: Nutrition
- JSON path: `$.questions[746].rationale`
- Detail: Known source or extraction contamination detected.

```text
Administering an enteral feeding may be delegated, at the nurse‘s discretion, to UAP in accordance with state regulations and facility policies and procedures. The nurse should verify tube placement and assess the patient prior to delegating this procedure. The UAP can perform o…
```

### 1283. PFQ-fundamentals-000000747 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 747
- Chapter: Nutrition
- JSON path: `$.questions[746].rationale`
- Detail: Pattern requires human review against the original source.

```text
Administering an enteral feeding may be delegated, at the nurse‘s discretion, to UAP in accordance with state regulations and facility policies and procedures. The nurse should verify tube placement and assess the patient prior to delegating this procedure. The UAP can perform o…
```

### 1284. PFQ-fundamentals-000000748 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 748
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[747].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1285. PFQ-fundamentals-000000749 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 749
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[748].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1286. PFQ-fundamentals-000000749 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 749
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[748].rationale`
- Detail: Known source or extraction contamination detected.

```text
U S N T O The frontal lobes of the cerebrum are the areas of the brain responsible for voluntary motor function, concentration, communication, decision making, and personality. The parietal lobes are responsible for the sense of touch, distinguishing the shape and texture of obj…
```

### 1287. PFQ-fundamentals-000000749 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 749
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[748].rationale`
- Detail: Pattern requires human review against the original source.

```text
U S N T O The frontal lobes of the cerebrum are the areas of the brain responsible for voluntary motor function, concentration, communication, decision making, and personality. The parietal lobes are responsible for the sense of touch, distinguishing the shape and texture of obj…
```

### 1288. PFQ-fundamentals-000000750 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 750
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[749].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1289. PFQ-fundamentals-000000751 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 751
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[750].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1290. PFQ-fundamentals-000000752 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 752
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[751].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1291. PFQ-fundamentals-000000752 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 752
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[751].rationale`
- Detail: Known source or extraction contamination detected.

```text
Tactile disturbances, such as tingling and numbness around the mouth and in the fingers, are signs of hypocalcemia. Mental changes are associated with both hypercalcemia and hypocalcemia. Both hypernatremia and hyponatremia have symptoms of central nervous system disorder. NCLEX…
```

### 1292. PFQ-fundamentals-000000753 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 753
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[752].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1293. PFQ-fundamentals-000000754 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 754
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[753].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1294. PFQ-fundamentals-000000754 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 754
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[753].rationale`
- Detail: Pattern requires human review against the original source.

```text
Hearing ability can be determined by observing the patient‘s conversation and responses and by talking with the patient in a normal conversational tone while standing slightly behind t he patient. If the patient does not respond appropriately, a hearing impairment may exist. Sta…
```

### 1295. PFQ-fundamentals-000000755 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 755
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[754].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1296. PFQ-fundamentals-000000756 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 756
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[755].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1297. PFQ-fundamentals-000000756 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 756
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[755].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1298. PFQ-fundamentals-000000757 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 757
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[756].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1299. PFQ-fundamentals-000000758 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 758
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[757].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1300. PFQ-fundamentals-000000759 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 759
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[758].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1301. PFQ-fundamentals-000000760 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 760
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[759].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1302. PFQ-fundamentals-000000761 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 761
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[760].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1303. PFQ-fundamentals-000000762 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 762
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[761].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1304. PFQ-fundamentals-000000762 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 762
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[761].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1305. PFQ-fundamentals-000000763 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 763
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[762].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is providing education to the family of a patient being discharged with dementia. Which statement by the family indicates an appropriate level of understanding of dementia? (Select all that apply.)
```

### 1306. PFQ-fundamentals-000000763 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 763
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[762].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1307. PFQ-fundamentals-000000764 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 764
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[763].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1308. PFQ-fundamentals-000000765 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 765
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[764].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1309. PFQ-fundamentals-000000765 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 765
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[764].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1310. PFQ-fundamentals-000000766 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 766
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[765].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1311. PFQ-fundamentals-000000766 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 766
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[765].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1312. PFQ-fundamentals-000000766 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 766
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[765].rationale`
- Detail: Pattern requires human review against the original source.

```text
Balance, eyesight, hearing, and sensation are all sensory function. Asking if the patient likes the newspaper does not specifically address vision. M S C : NC L E X C l i e n t Nee d s CNa tegRor y:IP hyGs i o lBo g.i cCa l InMtegrity
```

### 1313. PFQ-fundamentals-000000766 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 766
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[765].rationale`
- Detail: Pattern requires human review against the original source.

```text
Balance, eyesight, hearing, and sensation are all sensory function. Asking if the patient likes the newspaper does not specifically address vision. M S C : NC L E X C l i e n t Nee d s CNa tegRor y:IP hyGs i o lBo g.i cCa l InMtegrity
```

### 1314. PFQ-fundamentals-000000767 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 767
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[766].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1315. PFQ-fundamentals-000000768 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 768
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[767].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1316. PFQ-fundamentals-000000768 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 768
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[767].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1317. PFQ-fundamentals-000000769 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 769
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[768].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1318. PFQ-fundamentals-000000769 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 769
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[768].rationale`
- Detail: Pattern requires human review against the original source.

```text
If a patient has expressive aphasia, he or she understands language but is unable to answer questions, name common obNjeUctsR, SorIstNatGeTsiBm.plCe Oi dMe a s . The patient can answer yes/no questions by shaking the head. The patient might be able to point to pictures to expres…
```

### 1319. PFQ-fundamentals-000000770 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 770
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[769].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1320. PFQ-fundamentals-000000770 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 770
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[769].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1321. PFQ-fundamentals-000000771 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 771
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[770].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1322. PFQ-fundamentals-000000772 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 772
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[771].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1323. PFQ-fundamentals-000000772 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 772
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[771].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1324. PFQ-fundamentals-000000772 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 772
- Chapter: Cognitive and Sensory Alterations
- JSON path: `$.questions[771].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient experiencing dizziness or vertigo exercises caution when changing positions. The patient suffering from motion sickness needs to ride in the front seat of the car and look far ahead through the car windshield. Keeping rooms well-lit and focusing ahead when walking, u…
```

### 1325. PFQ-fundamentals-000000773 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 773
- Chapter: Stress and Coping
- JSON path: `$.questions[772].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1326. PFQ-fundamentals-000000773 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 773
- Chapter: Stress and Coping
- JSON path: `$.questions[772].rationale`
- Detail: Known source or extraction contamination detected.

```text
Sense of coherence (SOC) is a characteristic of personality that references one‘s perception of the world as comprehensible, meaningful, and manageable. Stress appraisal is the automatic, often unconscious assessment of a demand or stressor. Allostasis is an alternative term for…
```

### 1327. PFQ-fundamentals-000000774 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 774
- Chapter: Stress and Coping
- JSON path: `$.questions[773].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1328. PFQ-fundamentals-000000774 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 774
- Chapter: Stress and Coping
- JSON path: `$.questions[773].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
―I will join a support groupU.‖ SNT O
```

### 1329. PFQ-fundamentals-000000775 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 775
- Chapter: Stress and Coping
- JSON path: `$.questions[774].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1330. PFQ-fundamentals-000000776 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 776
- Chapter: Stress and Coping
- JSON path: `$.questions[775].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1331. PFQ-fundamentals-000000776 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 776
- Chapter: Stress and Coping
- JSON path: `$.questions[775].rationale`
- Detail: Pattern requires human review against the original source.

```text
The endocrine system responds to stress on the body such as what happens during an acute MI. Corticosteroids are important in the stress response because they increase serum glucose levels and inhibit the inflammatory response. Although MIs can be seen in diabetics, there is not…
```

### 1332. PFQ-fundamentals-000000776 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 776
- Chapter: Stress and Coping
- JSON path: `$.questions[775].rationale`
- Detail: Pattern requires human review against the original source.

```text
The endocrine system responds to stress on the body such as what happens during an acute MI. Corticosteroids are important in the stress response because they increase serum glucose levels and inhibit the inflammatory response. Although MIs can be seen in diabetics, there is not…
```

### 1333. PFQ-fundamentals-000000777 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 777
- Chapter: Stress and Coping
- JSON path: `$.questions[776].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1334. PFQ-fundamentals-000000778 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 778
- Chapter: Stress and Coping
- JSON path: `$.questions[777].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1335. PFQ-fundamentals-000000778 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 778
- Chapter: Stress and Coping
- JSON path: `$.questions[777].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Eat a diet with lots of fiber. U S N T O
```

### 1336. PFQ-fundamentals-000000778 — detached taxonomy word

- Severity: **medium**
- Category: Text
- Question index: 778
- Chapter: Stress and Coping
- JSON path: `$.questions[777].rationale`
- Detail: Pattern requires human review against the original source.

```text
High stress levels are known to exacerbate multiple sclerosis and other autoimmune diseases. Exercise helps keep muscles loose and helps with balance. Assessing skin for pressure sores and eating a diet with high fiber prevents complications from multiple sclerosis. Analyzing
```

### 1337. PFQ-fundamentals-000000778 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 778
- Chapter: Stress and Coping
- JSON path: `$.questions[777].rationale`
- Detail: Pattern requires human review against the original source.

```text
High stress levels are known to exacerbate multiple sclerosis and other autoimmune diseases. Exercise helps keep muscles loose and helps with balance. Assessing skin for pressure sores and eating a diet with high fiber prevents complications from multiple sclerosis. Analyzing
```

### 1338. PFQ-fundamentals-000000779 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 779
- Chapter: Stress and Coping
- JSON path: `$.questions[778].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1339. PFQ-fundamentals-000000780 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 780
- Chapter: Stress and Coping
- JSON path: `$.questions[779].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1340. PFQ-fundamentals-000000780 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 780
- Chapter: Stress and Coping
- JSON path: `$.questions[779].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Blood pressure of 120/84N R I G B.C M
```

### 1341. PFQ-fundamentals-000000781 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 781
- Chapter: Stress and Coping
- JSON path: `$.questions[780].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1342. PFQ-fundamentals-000000782 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 782
- Chapter: Stress and Coping
- JSON path: `$.questions[781].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1343. PFQ-fundamentals-000000783 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 783
- Chapter: Stress and Coping
- JSON path: `$.questions[782].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1344. PFQ-fundamentals-000000784 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 784
- Chapter: Stress and Coping
- JSON path: `$.questions[783].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1345. PFQ-fundamentals-000000785 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 785
- Chapter: Stress and Coping
- JSON path: `$.questions[784].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1346. PFQ-fundamentals-000000786 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 786
- Chapter: Stress and Coping
- JSON path: `$.questions[785].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1347. PFQ-fundamentals-000000787 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 787
- Chapter: Stress and Coping
- JSON path: `$.questions[786].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1348. PFQ-fundamentals-000000788 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 788
- Chapter: Stress and Coping
- JSON path: `$.questions[787].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1349. PFQ-fundamentals-000000789 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 789
- Chapter: Stress and Coping
- JSON path: `$.questions[788].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1350. PFQ-fundamentals-000000790 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 790
- Chapter: Stress and Coping
- JSON path: `$.questions[789].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1351. PFQ-fundamentals-000000791 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 791
- Chapter: Stress and Coping
- JSON path: `$.questions[790].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1352. PFQ-fundamentals-000000791 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 791
- Chapter: Stress and Coping
- JSON path: `$.questions[790].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1353. PFQ-fundamentals-000000792 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 792
- Chapter: Stress and Coping
- JSON path: `$.questions[791].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1354. PFQ-fundamentals-000000792 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 792
- Chapter: Stress and Coping
- JSON path: `$.questions[791].rationale`
- Detail: Known source or extraction contamination detected.

```text
The release of hormones increases the heart rate, resulting in increased cardiac output, and elevated blood pressure. TheNre isRanIi n c rGeUa s eBSi.n Ct h e Mf low of blood to muscles at the expense ofthe digestive and other systems not immediately needed in the fight-or-fligh…
```

### 1355. PFQ-fundamentals-000000792 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 792
- Chapter: Stress and Coping
- JSON path: `$.questions[791].rationale`
- Detail: Pattern requires human review against the original source.

```text
The release of hormones increases the heart rate, resulting in increased cardiac output, and elevated blood pressure. TheNre isRanIi n c rGeUa s eBSi.n Ct h e Mf low of blood to muscles at the expense ofthe digestive and other systems not immediately needed in the fight-or-fligh…
```

### 1356. PFQ-fundamentals-000000793 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 793
- Chapter: Stress and Coping
- JSON path: `$.questions[792].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1357. PFQ-fundamentals-000000793 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 793
- Chapter: Stress and Coping
- JSON path: `$.questions[792].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1358. PFQ-fundamentals-000000793 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 793
- Chapter: Stress and Coping
- JSON path: `$.questions[792].rationale`
- Detail: Pattern requires human review against the original source.

```text
Personality factors such as resilience, hardiness, and sense of coherence can buffer t he impact of stress, reducing the negative consequences. Gender is not a personality factor . Coping style refers to a pattern of measures taken to relieve stress but is not a personality fact…
```

### 1359. PFQ-fundamentals-000000794 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 794
- Chapter: Stress and Coping
- JSON path: `$.questions[793].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1360. PFQ-fundamentals-000000794 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 794
- Chapter: Stress and Coping
- JSON path: `$.questions[793].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1361. PFQ-fundamentals-000000794 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 794
- Chapter: Stress and Coping
- JSON path: `$.questions[793].rationale`
- Detail: Known source or extraction contamination detected.

```text
Childhood stress related to the school experience centers on competition, goal achievement, and test anxiety. Family dissolution and life changes are not related to the school experience. NCLEX Client Needs Category: Psychosocial Integrity
```

### 1362. PFQ-fundamentals-000000795 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 795
- Chapter: Stress and Coping
- JSON path: `$.questions[794].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "C", "E", "B", "C"]
```

### 1363. PFQ-fundamentals-000000795 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 795
- Chapter: Stress and Coping
- JSON path: `$.questions[794].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1364. PFQ-fundamentals-000000796 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 796
- Chapter: Stress and Coping
- JSON path: `$.questions[795].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1365. PFQ-fundamentals-000000796 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 796
- Chapter: Stress and Coping
- JSON path: `$.questions[795].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1366. PFQ-fundamentals-000000797 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 797
- Chapter: Stress and Coping
- JSON path: `$.questions[796].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1367. PFQ-fundamentals-000000797 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 797
- Chapter: Stress and Coping
- JSON path: `$.questions[796].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1368. PFQ-fundamentals-000000797 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 797
- Chapter: Stress and Coping
- JSON path: `$.questions[796].rationale`
- Detail: Known source or extraction contamination detected.

```text
To care most effectively for others, nurses must first take time to care for themselves. Many of the stress reduction interventions incorporated into patient care plans can be effective in addressing the stressors faced by nurses. Exercise, balanced nutrition, and mindfulness th…
```

### 1369. PFQ-fundamentals-000000798 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 798
- Chapter: Sleep
- JSON path: `$.questions[797].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1370. PFQ-fundamentals-000000799 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 799
- Chapter: Sleep
- JSON path: `$.questions[798].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1371. PFQ-fundamentals-000000800 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 800
- Chapter: Sleep
- JSON path: `$.questions[799].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1372. PFQ-fundamentals-000000801 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 801
- Chapter: Sleep
- JSON path: `$.questions[800].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1373. PFQ-fundamentals-000000801 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 801
- Chapter: Sleep
- JSON path: `$.questions[800].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1374. PFQ-fundamentals-000000802 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 802
- Chapter: Sleep
- JSON path: `$.questions[801].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1375. PFQ-fundamentals-000000803 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 803
- Chapter: Sleep
- JSON path: `$.questions[802].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1376. PFQ-fundamentals-000000804 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 804
- Chapter: Sleep
- JSON path: `$.questions[803].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1377. PFQ-fundamentals-000000805 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 805
- Chapter: Sleep
- JSON path: `$.questions[804].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1378. PFQ-fundamentals-000000806 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 806
- Chapter: Sleep
- JSON path: `$.questions[805].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1379. PFQ-fundamentals-000000807 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 807
- Chapter: Sleep
- JSON path: `$.questions[806].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1380. PFQ-fundamentals-000000807 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 807
- Chapter: Sleep
- JSON path: `$.questions[806].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1381. PFQ-fundamentals-000000808 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 808
- Chapter: Sleep
- JSON path: `$.questions[807].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1382. PFQ-fundamentals-000000809 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 809
- Chapter: Sleep
- JSON path: `$.questions[808].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1383. PFQ-fundamentals-000000810 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 810
- Chapter: Sleep
- JSON path: `$.questions[809].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1384. PFQ-fundamentals-000000811 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 811
- Chapter: Sleep
- JSON path: `$.questions[810].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1385. PFQ-fundamentals-000000811 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 811
- Chapter: Sleep
- JSON path: `$.questions[810].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1386. PFQ-fundamentals-000000812 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 812
- Chapter: Sleep
- JSON path: `$.questions[811].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1387. PFQ-fundamentals-000000813 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 813
- Chapter: Sleep
- JSON path: `$.questions[812].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1388. PFQ-fundamentals-000000814 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 814
- Chapter: Sleep
- JSON path: `$.questions[813].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1389. PFQ-fundamentals-000000814 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 814
- Chapter: Sleep
- JSON path: `$.questions[813].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1390. PFQ-fundamentals-000000815 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 815
- Chapter: Sleep
- JSON path: `$.questions[814].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1391. PFQ-fundamentals-000000815 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 815
- Chapter: Sleep
- JSON path: `$.questions[814].choices[1].text`
- Detail: Pattern requires human review against the original source.

```text
Slow rhythmic scanning eye movements U S N
```

### 1392. PFQ-fundamentals-000000815 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 815
- Chapter: Sleep
- JSON path: `$.questions[814].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1393. PFQ-fundamentals-000000815 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 815
- Chapter: Sleep
- JSON path: `$.questions[814].rationale`
- Detail: Pattern requires human review against the original source.

```text
During non –rapid eye movement (NREM) sleep, in which REM does not occur, physiological activity is reduced, brain waves, breathing and heart rate slow, and blood p ressure drops. Slow scanning eye movements do not occur in either REM or NREM. Dreaming occurs in REM.
```

### 1394. PFQ-fundamentals-000000816 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 816
- Chapter: Sleep
- JSON path: `$.questions[815].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1395. PFQ-fundamentals-000000817 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 817
- Chapter: Sleep
- JSON path: `$.questions[816].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1396. PFQ-fundamentals-000000818 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 818
- Chapter: Sleep
- JSON path: `$.questions[817].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1397. PFQ-fundamentals-000000818 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 818
- Chapter: Sleep
- JSON path: `$.questions[817].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1398. PFQ-fundamentals-000000819 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 819
- Chapter: Sleep
- JSON path: `$.questions[818].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1399. PFQ-fundamentals-000000819 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 819
- Chapter: Sleep
- JSON path: `$.questions[818].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1400. PFQ-fundamentals-000000820 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 820
- Chapter: Sleep
- JSON path: `$.questions[819].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1401. PFQ-fundamentals-000000820 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 820
- Chapter: Sleep
- JSON path: `$.questions[819].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1402. PFQ-fundamentals-000000821 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 821
- Chapter: Sleep
- JSON path: `$.questions[820].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1403. PFQ-fundamentals-000000821 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 821
- Chapter: Sleep
- JSON path: `$.questions[820].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1404. PFQ-fundamentals-000000822 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 822
- Chapter: Sleep
- JSON path: `$.questions[821].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1405. PFQ-fundamentals-000000822 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 822
- Chapter: Sleep
- JSON path: `$.questions[821].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1406. PFQ-fundamentals-000000822 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 822
- Chapter: Sleep
- JSON path: `$.questions[821].rationale`
- Detail: Known source or extraction contamination detected.

```text
Medications would be used cNarUeRf ulSlyIaNnGd dToBn.otCalwMays improve sleep. Addressing the sleep environment, maintaining sleep routines, providing light snacks if allowed, and instituting relaxation measures will all improve sleep. 3rd Edition
```

### 1407. PFQ-fundamentals-000000823 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 823
- Chapter: Diagnostic Testing
- JSON path: `$.questions[822].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1408. PFQ-fundamentals-000000823 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 823
- Chapter: Diagnostic Testing
- JSON path: `$.questions[822].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1409. PFQ-fundamentals-000000824 — repeated word

- Severity: **medium**
- Category: Text
- Question index: 824
- Chapter: Diagnostic Testing
- JSON path: `$.questions[823].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for an elderly patient with dementia. Which laboratory finding indicates to the nurse that that patient is often forgetting to eat meals?
```

### 1410. PFQ-fundamentals-000000824 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 824
- Chapter: Diagnostic Testing
- JSON path: `$.questions[823].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1411. PFQ-fundamentals-000000825 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 825
- Chapter: Diagnostic Testing
- JSON path: `$.questions[824].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1412. PFQ-fundamentals-000000825 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 825
- Chapter: Diagnostic Testing
- JSON path: `$.questions[824].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
Prothrombin time (PT) 11.5 sec U S N
```

### 1413. PFQ-fundamentals-000000825 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 825
- Chapter: Diagnostic Testing
- JSON path: `$.questions[824].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1414. PFQ-fundamentals-000000826 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 826
- Chapter: Diagnostic Testing
- JSON path: `$.questions[825].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1415. PFQ-fundamentals-000000826 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 826
- Chapter: Diagnostic Testing
- JSON path: `$.questions[825].rationale`
- Detail: Known source or extraction contamination detected.

```text
Bleeding anywhere along the GI tract results in blood in the stool. Bleeding that occurs in the upper GI tract produces stools that are black and tarry in appearance. Bleeding within the lower GI tract presents with soft stools that have bright red streaks. Watery stool with par…
```

### 1416. PFQ-fundamentals-000000827 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 827
- Chapter: Diagnostic Testing
- JSON path: `$.questions[826].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1417. PFQ-fundamentals-000000827 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 827
- Chapter: Diagnostic Testing
- JSON path: `$.questions[826].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1418. PFQ-fundamentals-000000828 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 828
- Chapter: Diagnostic Testing
- JSON path: `$.questions[827].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1419. PFQ-fundamentals-000000828 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 828
- Chapter: Diagnostic Testing
- JSON path: `$.questions[827].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1420. PFQ-fundamentals-000000829 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 829
- Chapter: Diagnostic Testing
- JSON path: `$.questions[828].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1421. PFQ-fundamentals-000000829 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 829
- Chapter: Diagnostic Testing
- JSON path: `$.questions[828].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1422. PFQ-fundamentals-000000830 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 830
- Chapter: Diagnostic Testing
- JSON path: `$.questions[829].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1423. PFQ-fundamentals-000000830 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 830
- Chapter: Diagnostic Testing
- JSON path: `$.questions[829].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1424. PFQ-fundamentals-000000831 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 831
- Chapter: Diagnostic Testing
- JSON path: `$.questions[830].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1425. PFQ-fundamentals-000000831 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 831
- Chapter: Diagnostic Testing
- JSON path: `$.questions[830].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1426. PFQ-fundamentals-000000832 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 832
- Chapter: Diagnostic Testing
- JSON path: `$.questions[831].choices[2].text`
- Detail: Pattern requires human review against the original source.

```text
Shrimp and scallops U S N T O
```

### 1427. PFQ-fundamentals-000000833 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 833
- Chapter: Diagnostic Testing
- JSON path: `$.questions[832].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1428. PFQ-fundamentals-000000833 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 833
- Chapter: Diagnostic Testing
- JSON path: `$.questions[832].rationale`
- Detail: Known source or extraction contamination detected.

```text
Numbing medication is applied to the back of the throat just before bronchoscopy. This may lead to swallowing difficulty and risk for aspiration until the gag reflex returns. The nurse should keep patient NPO until swallow, gag, and cough reflexes have returned. The nurse does n…
```

### 1429. PFQ-fundamentals-000000834 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 834
- Chapter: Diagnostic Testing
- JSON path: `$.questions[833].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1430. PFQ-fundamentals-000000834 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 834
- Chapter: Diagnostic Testing
- JSON path: `$.questions[833].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1431. PFQ-fundamentals-000000834 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 834
- Chapter: Diagnostic Testing
- JSON path: `$.questions[833].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient will be positioned in the prone or lateral position for the test, so the patient will not be able to count ceiling tiles as a distraction during the numbing step of the test. The patient may take acetaminophen as needed for discomfort afterward. The biopsy site must …
```

### 1432. PFQ-fundamentals-000000835 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 835
- Chapter: Diagnostic Testing
- JSON path: `$.questions[834].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1433. PFQ-fundamentals-000000835 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 835
- Chapter: Diagnostic Testing
- JSON path: `$.questions[834].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Provide a quiet, dark envNiroUnRmSenIt NsoGtThaBt .thCe Op aMt i e n t can rest comfortably.
```

### 1434. PFQ-fundamentals-000000836 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 836
- Chapter: Diagnostic Testing
- JSON path: `$.questions[835].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1435. PFQ-fundamentals-000000837 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 837
- Chapter: Diagnostic Testing
- JSON path: `$.questions[836].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1436. PFQ-fundamentals-000000837 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 837
- Chapter: Diagnostic Testing
- JSON path: `$.questions[836].rationale`
- Detail: Known source or extraction contamination detected.

```text
Drinking extra fluids so that the lab will have an extra-large specimen to test is not done as part of 24-hour urine collection, and it may skew the test results. The specimen should be kept chilled on ice or in a refrigerator until it is brought to the lab. If the patient accid…
```

### 1437. PFQ-fundamentals-000000838 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 838
- Chapter: Diagnostic Testing
- JSON path: `$.questions[837].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1438. PFQ-fundamentals-000000838 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 838
- Chapter: Diagnostic Testing
- JSON path: `$.questions[837].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1439. PFQ-fundamentals-000000839 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 839
- Chapter: Diagnostic Testing
- JSON path: `$.questions[838].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1440. PFQ-fundamentals-000000840 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 840
- Chapter: Diagnostic Testing
- JSON path: `$.questions[839].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1441. PFQ-fundamentals-000000841 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 841
- Chapter: Diagnostic Testing
- JSON path: `$.questions[840].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1442. PFQ-fundamentals-000000842 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 842
- Chapter: Diagnostic Testing
- JSON path: `$.questions[841].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1443. PFQ-fundamentals-000000843 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 843
- Chapter: Diagnostic Testing
- JSON path: `$.questions[842].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1444. PFQ-fundamentals-000000843 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 843
- Chapter: Diagnostic Testing
- JSON path: `$.questions[842].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
White blood cell count (WNBCR) 4I5U0 0G/Sm mNB3.CT M O
```

### 1445. PFQ-fundamentals-000000843 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 843
- Chapter: Diagnostic Testing
- JSON path: `$.questions[842].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1446. PFQ-fundamentals-000000843 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 843
- Chapter: Diagnostic Testing
- JSON path: `$.questions[842].rationale`
- Detail: Pattern requires human review against the original source.

```text
Red blood cell count of 5.8 million and hemoglobin value of 14 g/dL are both norm al. Hematocrit level of 25% is very low and indicative of ongoing anemia. White blood cell and platelet counts are not checked for anemia.
```

### 1447. PFQ-fundamentals-000000844 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 844
- Chapter: Diagnostic Testing
- JSON path: `$.questions[843].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1448. PFQ-fundamentals-000000844 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 844
- Chapter: Diagnostic Testing
- JSON path: `$.questions[843].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1449. PFQ-fundamentals-000000845 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 845
- Chapter: Diagnostic Testing
- JSON path: `$.questions[844].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1450. PFQ-fundamentals-000000845 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 845
- Chapter: Diagnostic Testing
- JSON path: `$.questions[844].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1451. PFQ-fundamentals-000000845 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 845
- Chapter: Diagnostic Testing
- JSON path: `$.questions[844].rationale`
- Detail: Pattern requires human review against the original source.

```text
Interventions for the Nursing diagnosis of risk for infection involve monitoring for signs and symptoms of infection, preventing contamination of supplies by maintaining a sterile field during the procedure, and teaching the patient how to care for the site afterward. Providing …
```

### 1452. PFQ-fundamentals-000000846 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 846
- Chapter: Diagnostic Testing
- JSON path: `$.questions[845].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1453. PFQ-fundamentals-000000846 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 846
- Chapter: Diagnostic Testing
- JSON path: `$.questions[845].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1454. PFQ-fundamentals-000000847 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 847
- Chapter: Diagnostic Testing
- JSON path: `$.questions[846].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1455. PFQ-fundamentals-000000847 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 847
- Chapter: Diagnostic Testing
- JSON path: `$.questions[846].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1456. PFQ-fundamentals-000000847 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 847
- Chapter: Diagnostic Testing
- JSON path: `$.questions[846].rationale`
- Detail: Known source or extraction contamination detected.

```text
Alanine aminotransferase (ALT) and alkaline phosphatase (ALP) are indicators of liver function, and increased levels indicate liver damage from a variety of causes. BUN, ANA, ESR, and FDP are not indicators of liver function. NCLEX Client Needs Category: Reduction of Risk Potent…
```

### 1457. PFQ-fundamentals-000000847 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 847
- Chapter: Diagnostic Testing
- JSON path: `$.questions[846].rationale`
- Detail: Known source or extraction contamination detected.

```text
Alanine aminotransferase (ALT) and alkaline phosphatase (ALP) are indicators of liver function, and increased levels indicate liver damage from a variety of causes. BUN, ANA, ESR, and FDP are not indicators of liver function. NCLEX Client Needs Category: Reduction of Risk Potent…
```

### 1458. PFQ-fundamentals-000000848 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 848
- Chapter: Medication Administration
- JSON path: `$.questions[847].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1459. PFQ-fundamentals-000000848 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 848
- Chapter: Medication Administration
- JSON path: `$.questions[847].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1460. PFQ-fundamentals-000000849 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 849
- Chapter: Medication Administration
- JSON path: `$.questions[848].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1461. PFQ-fundamentals-000000850 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 850
- Chapter: Medication Administration
- JSON path: `$.questions[849].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who is in agonizing pain. All the following options are listed on the patient‘s medication order sheet to relive pain. The nurse knows which option that will provide the most rapid pain relief for the patient?
```

### 1462. PFQ-fundamentals-000000850 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 850
- Chapter: Medication Administration
- JSON path: `$.questions[849].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1463. PFQ-fundamentals-000000850 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 850
- Chapter: Medication Administration
- JSON path: `$.questions[849].rationale`
- Detail: Known source or extraction contamination detected.

```text
IV administration has the most rapid onset of action and will provide the patient with the quickest pain relief. NCLEX Client Needs Category: Physiological Integrity: Pharmacological and Parenteral Therapies
```

### 1464. PFQ-fundamentals-000000851 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 851
- Chapter: Medication Administration
- JSON path: `$.questions[850].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1465. PFQ-fundamentals-000000852 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 852
- Chapter: Medication Administration
- JSON path: `$.questions[851].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1466. PFQ-fundamentals-000000852 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 852
- Chapter: Medication Administration
- JSON path: `$.questions[851].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1467. PFQ-fundamentals-000000853 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 853
- Chapter: Medication Administration
- JSON path: `$.questions[852].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1468. PFQ-fundamentals-000000854 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 854
- Chapter: Medication Administration
- JSON path: `$.questions[853].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1469. PFQ-fundamentals-000000855 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 855
- Chapter: Medication Administration
- JSON path: `$.questions[854].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1470. PFQ-fundamentals-000000855 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 855
- Chapter: Medication Administration
- JSON path: `$.questions[854].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1471. PFQ-fundamentals-000000855 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 855
- Chapter: Medication Administration
- JSON path: `$.questions[854].rationale`
- Detail: Known source or extraction contamination detected.

```text
Extended release medications must always be swallowed whole without crushing or dissolving the tablet. They are not given sublingually or allowed to dissolve in the mouth. MS Contin Morphine sulfate Extended release tablets, USP 15 mg CII only NCLEX Client Needs Category: Physio…
```

### 1472. PFQ-fundamentals-000000856 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 856
- Chapter: Medication Administration
- JSON path: `$.questions[855].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1473. PFQ-fundamentals-000000857 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 857
- Chapter: Medication Administration
- JSON path: `$.questions[856].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1474. PFQ-fundamentals-000000858 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 858
- Chapter: Medication Administration
- JSON path: `$.questions[857].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1475. PFQ-fundamentals-000000859 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 859
- Chapter: Medication Administration
- JSON path: `$.questions[858].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1476. PFQ-fundamentals-000000860 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 860
- Chapter: Medication Administration
- JSON path: `$.questions[859].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1477. PFQ-fundamentals-000000861 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 861
- Chapter: Medication Administration
- JSON path: `$.questions[860].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1478. PFQ-fundamentals-000000861 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 861
- Chapter: Medication Administration
- JSON path: `$.questions[860].rationale`
- Detail: Pattern requires human review against the original source.

```text
Asking if the patient has been taking extra doses of the medication will allow the nurse to determine if the patient has been taking too much of the drug or more than was prescribed. Toxicity occurs when the patient receives/takes excessive amounts of the drug. Therapies
```

### 1479. PFQ-fundamentals-000000862 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 862
- Chapter: Medication Administration
- JSON path: `$.questions[861].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1480. PFQ-fundamentals-000000863 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 863
- Chapter: Medication Administration
- JSON path: `$.questions[862].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1481. PFQ-fundamentals-000000863 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 863
- Chapter: Medication Administration
- JSON path: `$.questions[862].rationale`
- Detail: Known source or extraction contamination detected.

```text
When medications combine t No foRrm Ic r y sGt a l sBo.r Ca d v Me r s e chemical reactions, the result is a drug incompatibility. Compatibility must be assessed prior to medication preparation and administration. NCLEX Client Needs Category: Physiological Integrity: Pharmacolog…
```

### 1482. PFQ-fundamentals-000000864 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 864
- Chapter: Medication Administration
- JSON path: `$.questions[863].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1483. PFQ-fundamentals-000000865 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 865
- Chapter: Medication Administration
- JSON path: `$.questions[864].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1484. PFQ-fundamentals-000000866 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 866
- Chapter: Medication Administration
- JSON path: `$.questions[865].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1485. PFQ-fundamentals-000000866 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 866
- Chapter: Medication Administration
- JSON path: `$.questions[865].rationale`
- Detail: Known source or extraction contamination detected.

```text
Intramuscular injections for adults are usually administered with a 3 mL syringe and a 1 to 3 inch, 19 to 25 gauge needle. Tuberculin syringes are typically used for subcutaneous injections. The inch needles aNre tRo o Is horGt f o Br i.n tCraUmMuSs cular injections into adults.…
```

### 1486. PFQ-fundamentals-000000867 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 867
- Chapter: Medication Administration
- JSON path: `$.questions[866].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1487. PFQ-fundamentals-000000868 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 868
- Chapter: Medication Administration
- JSON path: `$.questions[867].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient with multiple chronic illnesses who is having difficulty remembering to take multiple medications at the correct times. Which is the appropriat e Nursing diagnosis for this patient?
```

### 1488. PFQ-fundamentals-000000868 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 868
- Chapter: Medication Administration
- JSON path: `$.questions[867].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1489. PFQ-fundamentals-000000869 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 869
- Chapter: Medication Administration
- JSON path: `$.questions[868].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1490. PFQ-fundamentals-000000870 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 870
- Chapter: Medication Administration
- JSON path: `$.questions[869].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1491. PFQ-fundamentals-000000871 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 871
- Chapter: Medication Administration
- JSON path: `$.questions[870].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "E", "F", "B", "C"]
```

### 1492. PFQ-fundamentals-000000871 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 871
- Chapter: Medication Administration
- JSON path: `$.questions[870].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1493. PFQ-fundamentals-000000872 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 872
- Chapter: Medication Administration
- JSON path: `$.questions[871].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1494. PFQ-fundamentals-000000872 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 872
- Chapter: Medication Administration
- JSON path: `$.questions[871].rationale`
- Detail: Known source or extraction contamination detected.

```text
Parenteral medications are administered by injection into tissue, muscle, or a vein rather than through the gastrointestinal or respiratory route. Therapies 3rd Edition
```

### 1495. PFQ-fundamentals-000000873 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 873
- Chapter: Pain Management
- JSON path: `$.questions[872].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1496. PFQ-fundamentals-000000874 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 874
- Chapter: Pain Management
- JSON path: `$.questions[873].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1497. PFQ-fundamentals-000000875 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 875
- Chapter: Pain Management
- JSON path: `$.questions[874].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1498. PFQ-fundamentals-000000875 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 875
- Chapter: Pain Management
- JSON path: `$.questions[874].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1499. PFQ-fundamentals-000000875 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 875
- Chapter: Pain Management
- JSON path: `$.questions[874].rationale`
- Detail: Known source or extraction contamination detected.

```text
Visceral pain arises from the organs of the body and occurs when inflammation and tissue damage occur, such as with cholecystitis. Somatic pain occurs when there is tissue damage to skin, muscle, joints, and bones. Referred pain occurs when the discomfort is felt at a location o…
```

### 1500. PFQ-fundamentals-000000876 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 876
- Chapter: Pain Management
- JSON path: `$.questions[875].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1501. PFQ-fundamentals-000000876 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 876
- Chapter: Pain Management
- JSON path: `$.questions[875].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1502. PFQ-fundamentals-000000877 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 877
- Chapter: Pain Management
- JSON path: `$.questions[876].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1503. PFQ-fundamentals-000000878 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 878
- Chapter: Pain Management
- JSON path: `$.questions[877].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1504. PFQ-fundamentals-000000878 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 878
- Chapter: Pain Management
- JSON path: `$.questions[877].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1505. PFQ-fundamentals-000000879 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 879
- Chapter: Pain Management
- JSON path: `$.questions[878].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1506. PFQ-fundamentals-000000879 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 879
- Chapter: Pain Management
- JSON path: `$.questions[878].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1507. PFQ-fundamentals-000000879 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 879
- Chapter: Pain Management
- JSON path: `$.questions[878].rationale`
- Detail: Known source or extraction contamination detected.

```text
Referred pain is pain that occurs when discomfort is felt in a different area than the source of the pain. Phantom pain occurs in amputees when pain is felt in the missing limb. Neuropathic pain occurs in the nervous system and often feels like burning or tingling. Psychogenic p…
```

### 1508. PFQ-fundamentals-000000879 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 879
- Chapter: Pain Management
- JSON path: `$.questions[878].rationale`
- Detail: Pattern requires human review against the original source.

```text
Referred pain is pain that occurs when discomfort is felt in a different area than the source of the pain. Phantom pain occurs in amputees when pain is felt in the missing limb. Neuropathic pain occurs in the nervous system and often feels like burning or tingling. Psychogenic p…
```

### 1509. PFQ-fundamentals-000000880 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 880
- Chapter: Pain Management
- JSON path: `$.questions[879].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1510. PFQ-fundamentals-000000880 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 880
- Chapter: Pain Management
- JSON path: `$.questions[879].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1511. PFQ-fundamentals-000000881 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 881
- Chapter: Pain Management
- JSON path: `$.questions[880].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1512. PFQ-fundamentals-000000882 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 882
- Chapter: Pain Management
- JSON path: `$.questions[881].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1513. PFQ-fundamentals-000000883 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 883
- Chapter: Pain Management
- JSON path: `$.questions[882].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1514. PFQ-fundamentals-000000883 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 883
- Chapter: Pain Management
- JSON path: `$.questions[882].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1515. PFQ-fundamentals-000000884 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 884
- Chapter: Pain Management
- JSON path: `$.questions[883].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1516. PFQ-fundamentals-000000885 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 885
- Chapter: Pain Management
- JSON path: `$.questions[884].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1517. PFQ-fundamentals-000000885 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 885
- Chapter: Pain Management
- JSON path: `$.questions[884].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1518. PFQ-fundamentals-000000886 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 886
- Chapter: Pain Management
- JSON path: `$.questions[885].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1519. PFQ-fundamentals-000000887 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 887
- Chapter: Pain Management
- JSON path: `$.questions[886].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1520. PFQ-fundamentals-000000887 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 887
- Chapter: Pain Management
- JSON path: `$.questions[886].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1521. PFQ-fundamentals-000000888 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 888
- Chapter: Pain Management
- JSON path: `$.questions[887].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1522. PFQ-fundamentals-000000889 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 889
- Chapter: Pain Management
- JSON path: `$.questions[888].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who has a PCA pump following total hyster ectomy surgery. The nurse sees the visitor push the PCA button while the patient is sleeping quietly. What is the best response of the nurse?
```

### 1523. PFQ-fundamentals-000000889 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 889
- Chapter: Pain Management
- JSON path: `$.questions[888].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1524. PFQ-fundamentals-000000889 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 889
- Chapter: Pain Management
- JSON path: `$.questions[888].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
―PCA pumps are great because she doesn‘t have to wait for me to administer her pain medication.‖
```

### 1525. PFQ-fundamentals-000000890 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 890
- Chapter: Pain Management
- JSON path: `$.questions[889].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1526. PFQ-fundamentals-000000890 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 890
- Chapter: Pain Management
- JSON path: `$.questions[889].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1527. PFQ-fundamentals-000000890 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 890
- Chapter: Pain Management
- JSON path: `$.questions[889].rationale`
- Detail: Pattern requires human review against the original source.

```text
Pain character should be assessed using questions to learn more about what the pain feels like. Examples like stabbing, aching, burning may be used so that patients can under stand what the nurse is requesting. Onset is determined by asking when the pain started. Exacerbating/re…
```

### 1528. PFQ-fundamentals-000000891 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 891
- Chapter: Pain Management
- JSON path: `$.questions[890].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1529. PFQ-fundamentals-000000891 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 891
- Chapter: Pain Management
- JSON path: `$.questions[890].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1530. PFQ-fundamentals-000000892 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 892
- Chapter: Pain Management
- JSON path: `$.questions[891].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1531. PFQ-fundamentals-000000892 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 892
- Chapter: Pain Management
- JSON path: `$.questions[891].rationale`
- Detail: Pattern requires human review against the original source.

```text
Goals must be measurable and objective so that nursing staff can determine when each of the goals has been met. Having the patient describe meditation techniques is measurable because the nursing staff can determine whether he can actually describe them. Goals are achieved by th…
```

### 1532. PFQ-fundamentals-000000893 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 893
- Chapter: Pain Management
- JSON path: `$.questions[892].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1533. PFQ-fundamentals-000000893 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 893
- Chapter: Pain Management
- JSON path: `$.questions[892].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1534. PFQ-fundamentals-000000894 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 894
- Chapter: Pain Management
- JSON path: `$.questions[893].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1535. PFQ-fundamentals-000000894 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 894
- Chapter: Pain Management
- JSON path: `$.questions[893].rationale`
- Detail: Known source or extraction contamination detected.

```text
Tricyclic antidepressants like amitriptyline and anticonvulsants like gabapentin are often used to treat neuropathic pain because they work directly on the nervous system. They may be given along with narcotic pain medication to make the patient comfortable. Senna will relieve c…
```

### 1536. PFQ-fundamentals-000000895 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 895
- Chapter: Pain Management
- JSON path: `$.questions[894].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1537. PFQ-fundamentals-000000895 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 895
- Chapter: Pain Management
- JSON path: `$.questions[894].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1538. PFQ-fundamentals-000000895 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 895
- Chapter: Pain Management
- JSON path: `$.questions[894].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient‘s history of rheumatoid arthritis, previous knee replacement surgery, and marathon running indicate that the patient has had significant experience dealing with pain, which will affect how he or she experiences pain after this surgery. The other factors will not affe…
```

### 1539. PFQ-fundamentals-000000895 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 895
- Chapter: Pain Management
- JSON path: `$.questions[894].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient‘s history of rheumatoid arthritis, previous knee replacement surgery, and marathon running indicate that the patient has had significant experience dealing with pain, which will affect how he or she experiences pain after this surgery. The other factors will not affe…
```

### 1540. PFQ-fundamentals-000000896 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 896
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[895].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1541. PFQ-fundamentals-000000897 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 897
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[896].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1542. PFQ-fundamentals-000000897 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 897
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[896].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1543. PFQ-fundamentals-000000898 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 898
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[897].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1544. PFQ-fundamentals-000000898 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 898
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[897].rationale`
- Detail: Pattern requires human review against the original source.

```text
Airway maintenance and protection is the highest priority for this patient, so the nurse should assess the endotracheal tube first to ensure that it is patent and positioned correctl y. The other tubes may be assessed afterward.
```

### 1545. PFQ-fundamentals-000000899 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 899
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[898].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1546. PFQ-fundamentals-000000900 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 900
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[899].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1547. PFQ-fundamentals-000000901 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 901
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[900].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1548. PFQ-fundamentals-000000902 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 902
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[901].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1549. PFQ-fundamentals-000000902 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 902
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[901].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1550. PFQ-fundamentals-000000903 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 903
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[902].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1551. PFQ-fundamentals-000000903 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 903
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[902].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1552. PFQ-fundamentals-000000904 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 904
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[903].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1553. PFQ-fundamentals-000000904 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 904
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[903].rationale`
- Detail: Pattern requires human review against the original source.

```text
The large red blood stain over the incision and feeling of ripping open most likely indicates that the patient‘s wound has dehisced or eviscerated. The nurse should immediately lower the patient to the floor to reduce tension on the wound. Patient modesty and privacy should be m…
```

### 1554. PFQ-fundamentals-000000905 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 905
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[904].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1555. PFQ-fundamentals-000000905 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 905
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[904].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1556. PFQ-fundamentals-000000906 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 906
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[905].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1557. PFQ-fundamentals-000000906 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 906
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[905].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1558. PFQ-fundamentals-000000907 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 907
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[906].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1559. PFQ-fundamentals-000000908 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 908
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[907].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1560. PFQ-fundamentals-000000909 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 909
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[908].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1561. PFQ-fundamentals-000000910 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 910
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[909].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1562. PFQ-fundamentals-000000910 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 910
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[909].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1563. PFQ-fundamentals-000000910 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 910
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[909].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient must take in a deep breath while holding the spirometer to the mouth s o that the device can indicate how much air is being inhaled into the lungs. The remaining responses are correct components of the procedure.
```

### 1564. PFQ-fundamentals-000000911 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 911
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[910].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1565. PFQ-fundamentals-000000911 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 911
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[910].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1566. PFQ-fundamentals-000000912 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 912
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[911].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1567. PFQ-fundamentals-000000913 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 913
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[912].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1568. PFQ-fundamentals-000000913 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 913
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[912].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1569. PFQ-fundamentals-000000914 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 914
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[913].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1570. PFQ-fundamentals-000000915 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 915
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[914].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is obtaining preoperative information for a patient who will be having emergency surgery shortly for a ruptured appendix. Which information is crucial for the nurse to assess? (Select all that apply.)
```

### 1571. PFQ-fundamentals-000000915 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 915
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[914].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1572. PFQ-fundamentals-000000915 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 915
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[914].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1573. PFQ-fundamentals-000000915 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 915
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[914].rationale`
- Detail: Pattern requires human review against the original source.

```text
Priority assessment must be completed prior to emergency surgery, including use of medications, alcohol, tobacco, or recreational drugs because these may interact with anesthesia medications. Allergies must be identified to prevent reactions in the operating room. Special precau…
```

### 1574. PFQ-fundamentals-000000916 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 916
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[915].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1575. PFQ-fundamentals-000000917 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 917
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[916].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1576. PFQ-fundamentals-000000917 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 917
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[916].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1577. PFQ-fundamentals-000000917 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 917
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[916].rationale`
- Detail: Known source or extraction contamination detected.

```text
Postoperative splinting is done by supporting the abdominal and chest muscles to minimize the pain of coughing and deep breathing after surgery. Patients who have just had heart or abdominal surgery will benefit from splinting. The other surgical procedures do not affect the che…
```

### 1578. PFQ-fundamentals-000000918 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 918
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[917].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1579. PFQ-fundamentals-000000918 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 918
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[917].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1580. PFQ-fundamentals-000000919 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 919
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[918].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1581. PFQ-fundamentals-000000919 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 919
- Chapter: Perioperative Nursing Care
- JSON path: `$.questions[918].rationale`
- Detail: Known source or extraction contamination detected.

```text
Signs of internal bleeding include tachycardia, increased abdominal pain and a drop in hematocrit/hemoglobin. Urinary output would decrease with internal bleeding because the kidneys work to conserve fluids. Itching and constipation are not signs of internal bleeding. 3rd Edition
```

### 1582. PFQ-fundamentals-000000920 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 920
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[919].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1583. PFQ-fundamentals-000000921 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 921
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[920].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1584. PFQ-fundamentals-000000921 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 921
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[920].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1585. PFQ-fundamentals-000000922 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 922
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[921].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1586. PFQ-fundamentals-000000922 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 922
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[921].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1587. PFQ-fundamentals-000000923 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 923
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[922].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1588. PFQ-fundamentals-000000923 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 923
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[922].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1589. PFQ-fundamentals-000000924 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 924
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[923].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1590. PFQ-fundamentals-000000924 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 924
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[923].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1591. PFQ-fundamentals-000000925 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 925
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[924].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1592. PFQ-fundamentals-000000926 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 926
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[925].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1593. PFQ-fundamentals-000000926 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 926
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[925].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1594. PFQ-fundamentals-000000927 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 927
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[926].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1595. PFQ-fundamentals-000000927 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 927
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[926].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1596. PFQ-fundamentals-000000928 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 928
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[927].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1597. PFQ-fundamentals-000000928 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 928
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[927].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1598. PFQ-fundamentals-000000929 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 929
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[928].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1599. PFQ-fundamentals-000000930 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 930
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[929].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1600. PFQ-fundamentals-000000931 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 931
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[930].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1601. PFQ-fundamentals-000000931 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 931
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[930].rationale`
- Detail: Known source or extraction contamination detected.

```text
Postural drainage is used for patients who have difficulty removing thick secretions from the airway. A patient with chronic bronchitis and a congested, productive cough would benefit from postural drainage because it would help clear the airway. NCLEX Client Needs Category: Phy…
```

### 1602. PFQ-fundamentals-000000932 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 932
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[931].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1603. PFQ-fundamentals-000000932 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 932
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[931].rationale`
- Detail: Pattern requires human review against the original source.

```text
Hemodilution is a common finding when patients are in fluid overload caused by congestive heart failure. A normal hematocrit result is 42% to 52% for a male and 37% to 47% for a female, so the patient‘s 32% Nhe mRat oIcrit Gl eveBl .isCm arMked ly low. The other laboratory resul…
```

### 1604. PFQ-fundamentals-000000932 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 932
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[931].rationale`
- Detail: Pattern requires human review against the original source.

```text
Hemodilution is a common finding when patients are in fluid overload caused by congestive heart failure. A normal hematocrit result is 42% to 52% for a male and 37% to 47% for a female, so the patient‘s 32% Nhe mRat oIcrit Gl eveBl .isCm arMked ly low. The other laboratory resul…
```

### 1605. PFQ-fundamentals-000000933 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 933
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[932].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1606. PFQ-fundamentals-000000934 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 934
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[933].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1607. PFQ-fundamentals-000000934 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 934
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[933].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1608. PFQ-fundamentals-000000934 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 934
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[933].rationale`
- Detail: Known source or extraction contamination detected.

```text
Cardiac catheterization includes the use of contrast dye to visualize the coronary arteries and determine blood flow to cardiac muscle. The other tests will not allow the physician to determine which (if any) coronary arteries are occluded. NCLEX Client Needs Category: Physiolog…
```

### 1609. PFQ-fundamentals-000000935 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 935
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[934].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1610. PFQ-fundamentals-000000935 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 935
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[934].rationale`
- Detail: Known source or extraction contamination detected.

```text
Echocardiograms allow for ultrasound visualization of the structures of the heart along with function of the heart valves aNndUcRaSrdIiaNc GmTusBcu.laCtuOreM. NCLEX Client Needs Category: Physiological Integrity: Reduction of Risk Potential
```

### 1611. PFQ-fundamentals-000000936 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 936
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[935].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1612. PFQ-fundamentals-000000936 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 936
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[935].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1613. PFQ-fundamentals-000000937 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 937
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[936].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1614. PFQ-fundamentals-000000937 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 937
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[936].choices[4].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1615. PFQ-fundamentals-000000937 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 937
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[936].rationale`
- Detail: Pattern requires human review against the original source.

```text
The goal of long-term therapy for the patient with COPD is usually to have an oxygen saturation level of more than 90%, which represents adequate delivery of oxygen to the tissues. Oxygen saturation may decrease during exercise, sleep, or deterioration of the respiratory status.…
```

### 1616. PFQ-fundamentals-000000938 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 938
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[937].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1617. PFQ-fundamentals-000000938 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 938
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[937].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1618. PFQ-fundamentals-000000939 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 939
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[938].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1619. PFQ-fundamentals-000000939 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 939
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[938].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1620. PFQ-fundamentals-000000940 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 940
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[939].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1621. PFQ-fundamentals-000000940 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 940
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[939].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1622. PFQ-fundamentals-000000941 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 941
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[940].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1623. PFQ-fundamentals-000000941 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 941
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[940].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1624. PFQ-fundamentals-000000941 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 941
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[940].rationale`
- Detail: Pattern requires human review against the original source.

```text
Only the inner cannula of the tracheostomy is removed for cleaning. The outer cannul a stays in the trachea to maintain airway patency. Clean gloves are applied before the soiled dress ing is removed. Normal sterile saline is used to remove secretions that have built u p on the …
```

### 1625. PFQ-fundamentals-000000942 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 942
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[941].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1626. PFQ-fundamentals-000000942 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 942
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[941].rationale`
- Detail: Known source or extraction contamination detected.

```text
The head of the patient‘s bed should be elevated prior to suctioning to facilitate coughing out secretions. Suction is always applied intermittently as the catheter is withdrawn. Water-soluble lubricant is used when suctioning the naris but not a tracheostomy because the secreti…
```

### 1627. PFQ-fundamentals-000000942 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 942
- Chapter: Oxygenation and Tissue Perfusion
- JSON path: `$.questions[941].rationale`
- Detail: Pattern requires human review against the original source.

```text
The head of the patient‘s bed should be elevated prior to suctioning to facilitate coughing out secretions. Suction is always applied intermittently as the catheter is withdrawn. Water-soluble lubricant is used when suctioning the naris but not a tracheostomy because the secreti…
```

### 1628. PFQ-fundamentals-000000943 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 943
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[942].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1629. PFQ-fundamentals-000000943 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 943
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[942].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1630. PFQ-fundamentals-000000943 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 943
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[942].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient‘s low albumin level will lead to generalized pitting edema because there isn‘t enough protein in the blood to keep water within the bloodstream. Lack of oncotic pressure from low serum albumin leads to edema. The other findings are not related to malnutrition. NCLEX …
```

### 1631. PFQ-fundamentals-000000944 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 944
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[943].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the patient‘s laboratory results. Which result must be communicated to t hephysician immediately? a . Serumchloride level 85 m E qN/ L R I GB.CM
```

### 1632. PFQ-fundamentals-000000944 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 944
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[943].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the patient‘s laboratory results. Which result must be communicated to t hephysician immediately? a . Serumchloride level 85 m E qN/ L R I GB.CM
```

### 1633. PFQ-fundamentals-000000944 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 944
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[943].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is reviewing the patient‘s laboratory results. Which result must be communicated to t hephysician immediately? a . Serumchloride level 85 m E qN/ L R I GB.CM
```

### 1634. PFQ-fundamentals-000000944 — possible broken web text

- Severity: **high**
- Category: Text
- Question index: 944
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[943].choices[0].text`
- Detail: Pattern requires human review against the original source.

```text
Serum sodium level 134 m UE q / LS NT O
```

### 1635. PFQ-fundamentals-000000945 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 945
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[944].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1636. PFQ-fundamentals-000000946 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 946
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[945].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1637. PFQ-fundamentals-000000946 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 946
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[945].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1638. PFQ-fundamentals-000000947 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 947
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[946].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1639. PFQ-fundamentals-000000948 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 948
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[947].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1640. PFQ-fundamentals-000000949 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 949
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[948].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1641. PFQ-fundamentals-000000949 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 949
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[948].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1642. PFQ-fundamentals-000000949 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 949
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[948].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient with dehydration is at risk for orthostatic hypotension or falling of the blood pressure when the patient rises to a standing position. When the blood pressure falls sufficiently, fainting may occur. The patient should be assisted to rise slowly from a supine to a si…
```

### 1643. PFQ-fundamentals-000000950 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 950
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[949].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1644. PFQ-fundamentals-000000950 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 950
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[949].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1645. PFQ-fundamentals-000000951 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 951
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[950].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1646. PFQ-fundamentals-000000952 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 952
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[951].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1647. PFQ-fundamentals-000000952 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 952
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[951].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1648. PFQ-fundamentals-000000953 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 953
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[952].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1649. PFQ-fundamentals-000000954 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 954
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[953].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1650. PFQ-fundamentals-000000954 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 954
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[953].rationale`
- Detail: Known source or extraction contamination detected.

```text
Intermittent doses of IV diuretics are best administered via an over-the-needle angiocatheter that is connected to a saline lock. The other IV catheter options are used when the patient requires a vesicant drug that could cause significant damage to tissues or when the patient r…
```

### 1651. PFQ-fundamentals-000000955 — duplicate correct answers

- Severity: **high**
- Category: Structure
- Question index: 955
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[954].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "B", "C"]
```

### 1652. PFQ-fundamentals-000000955 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 955
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[954].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1653. PFQ-fundamentals-000000956 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 956
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[955].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1654. PFQ-fundamentals-000000956 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 956
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[955].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1655. PFQ-fundamentals-000000956 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 956
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[955].rationale`
- Detail: Known source or extraction contamination detected.

```text
An IV site that is puffy and painful should be discontinued promptly because the fluid has infiltrated outside the vein and is causing localized irritation. The IV should be restarted in the other arm if possible. The other actions are inappropriate. NCLEX Client Needs Category:…
```

### 1656. PFQ-fundamentals-000000957 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 957
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[956].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1657. PFQ-fundamentals-000000957 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 957
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[956].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1658. PFQ-fundamentals-000000958 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 958
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[957].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1659. PFQ-fundamentals-000000959 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 959
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[958].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1660. PFQ-fundamentals-000000960 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 960
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[959].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1661. PFQ-fundamentals-000000960 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 960
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[959].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1662. PFQ-fundamentals-000000961 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 961
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[960].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1663. PFQ-fundamentals-000000961 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 961
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[960].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1664. PFQ-fundamentals-000000961 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 961
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[960].rationale`
- Detail: Pattern requires human review against the original source.

```text
A serum sodium level of 124 mEq/L is dangerously low and may cause neurol ogic problems including seizures, confusion, and weakness. Regular neurologic checks should be performed and the patient should be placed on seizure precautions until the sodium level is corrected. Encoura…
```

### 1665. PFQ-fundamentals-000000962 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 962
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[961].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1666. PFQ-fundamentals-000000962 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 962
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[961].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient should be instructed to take the diuretic early in the morning so that the effects will wear off before the patient goes to bed at night. Decreasing the dose could lead to fluid overload and pulmonary edema. Therapies
```

### 1667. PFQ-fundamentals-000000963 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 963
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[962].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1668. PFQ-fundamentals-000000963 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 963
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[962].choices[3].text`
- Detail: Pattern requires human review against the original source.

```text
―These medications will iNn c rRea s eIyo Gu r uBr i n.eCo u tMp u t until your kidneys recover.‖
```

### 1669. PFQ-fundamentals-000000964 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 964
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[963].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1670. PFQ-fundamentals-000000964 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 964
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[963].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1671. PFQ-fundamentals-000000965 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 965
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[964].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1672. PFQ-fundamentals-000000966 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 966
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[965].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1673. PFQ-fundamentals-000000966 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 966
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[965].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1674. PFQ-fundamentals-000000967 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 967
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[966].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1675. PFQ-fundamentals-000000967 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 967
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[966].rationale`
- Detail: Known source or extraction contamination detected.

```text
If a person produces the B antigen, the blood type is classified as B. Type O blood is classified as universal donors because their blood cells contain no antigens. Rh positive (Rh+) blood which means the person has the Rh factor on the surface of the red blood cells. Those who …
```

### 1676. PFQ-fundamentals-000000967 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 967
- Chapter: Fluid, Electrolytes, and Acid-Base Balance
- JSON path: `$.questions[966].rationale`
- Detail: Known source or extraction contamination detected.

```text
If a person produces the B antigen, the blood type is classified as B. Type O blood is classified as universal donors because their blood cells contain no antigens. Rh positive (Rh+) blood which means the person has the Rh factor on the surface of the red blood cells. Those who …
```

### 1677. PFQ-fundamentals-000000968 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 968
- Chapter: Bowel Elimination
- JSON path: `$.questions[967].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who periodically has small streaks of fresh red blood in the stool. The patient denies abdominal pain or loss of appetite. The nurse identifies wh at to be the most likely cause of this patient‘s bleeding?
```

### 1678. PFQ-fundamentals-000000968 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 968
- Chapter: Bowel Elimination
- JSON path: `$.questions[967].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1679. PFQ-fundamentals-000000968 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 968
- Chapter: Bowel Elimination
- JSON path: `$.questions[967].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1680. PFQ-fundamentals-000000968 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 968
- Chapter: Bowel Elimination
- JSON path: `$.questions[967].rationale`
- Detail: Known source or extraction contamination detected.

```text
Bleeding hemorrhoids can lead to small streaks of fresh red blood in the stool. Bleeding gastric ulcer would lead to black, tarry stools as the blood is digested. Colon polyps do not cause bleeding. NCLEX Client Needs Category: Physiological Integrity: Physiological Adaptation
```

### 1681. PFQ-fundamentals-000000970 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 970
- Chapter: Bowel Elimination
- JSON path: `$.questions[969].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1682. PFQ-fundamentals-000000971 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 971
- Chapter: Bowel Elimination
- JSON path: `$.questions[970].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1683. PFQ-fundamentals-000000972 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 972
- Chapter: Bowel Elimination
- JSON path: `$.questions[971].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1684. PFQ-fundamentals-000000972 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 972
- Chapter: Bowel Elimination
- JSON path: `$.questions[971].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1685. PFQ-fundamentals-000000973 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 973
- Chapter: Bowel Elimination
- JSON path: `$.questions[972].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1686. PFQ-fundamentals-000000973 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 973
- Chapter: Bowel Elimination
- JSON path: `$.questions[972].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1687. PFQ-fundamentals-000000974 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 974
- Chapter: Bowel Elimination
- JSON path: `$.questions[973].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1688. PFQ-fundamentals-000000974 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 974
- Chapter: Bowel Elimination
- JSON path: `$.questions[973].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1689. PFQ-fundamentals-000000975 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 975
- Chapter: Bowel Elimination
- JSON path: `$.questions[974].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1690. PFQ-fundamentals-000000976 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 976
- Chapter: Bowel Elimination
- JSON path: `$.questions[975].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1691. PFQ-fundamentals-000000977 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 977
- Chapter: Bowel Elimination
- JSON path: `$.questions[976].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1692. PFQ-fundamentals-000000977 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 977
- Chapter: Bowel Elimination
- JSON path: `$.questions[976].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1693. PFQ-fundamentals-000000978 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 978
- Chapter: Bowel Elimination
- JSON path: `$.questions[977].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1694. PFQ-fundamentals-000000979 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 979
- Chapter: Bowel Elimination
- JSON path: `$.questions[978].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1695. PFQ-fundamentals-000000979 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 979
- Chapter: Bowel Elimination
- JSON path: `$.questions[978].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1696. PFQ-fundamentals-000000979 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 979
- Chapter: Bowel Elimination
- JSON path: `$.questions[978].rationale`
- Detail: Pattern requires human review against the original source.

```text
Patients with a traumatic brain injury often have increased intracranial pressure, w hich can be worsened with enema administration, thus putting the patient at risk for additional neurologic damage. The provider should be contacted and the order should be questioned. Constipati…
```

### 1697. PFQ-fundamentals-000000980 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 980
- Chapter: Bowel Elimination
- JSON path: `$.questions[979].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1698. PFQ-fundamentals-000000980 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 980
- Chapter: Bowel Elimination
- JSON path: `$.questions[979].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1699. PFQ-fundamentals-000000981 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 981
- Chapter: Bowel Elimination
- JSON path: `$.questions[980].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1700. PFQ-fundamentals-000000982 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 982
- Chapter: Bowel Elimination
- JSON path: `$.questions[981].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1701. PFQ-fundamentals-000000982 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 982
- Chapter: Bowel Elimination
- JSON path: `$.questions[981].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1702. PFQ-fundamentals-000000982 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 982
- Chapter: Bowel Elimination
- JSON path: `$.questions[981].rationale`
- Detail: Known source or extraction contamination detected.

```text
Diarrhea, abdominal pain, and low-grade temperature after completing IV antibiotics are often caused by C. difficile infection. NCLEX Client Needs Category: Physiological Integrity: Physiological Adaptation
```

### 1703. PFQ-fundamentals-000000983 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 983
- Chapter: Bowel Elimination
- JSON path: `$.questions[982].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1704. PFQ-fundamentals-000000983 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 983
- Chapter: Bowel Elimination
- JSON path: `$.questions[982].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1705. PFQ-fundamentals-000000984 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 984
- Chapter: Bowel Elimination
- JSON path: `$.questions[983].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1706. PFQ-fundamentals-000000985 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 985
- Chapter: Bowel Elimination
- JSON path: `$.questions[984].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1707. PFQ-fundamentals-000000985 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 985
- Chapter: Bowel Elimination
- JSON path: `$.questions[984].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1708. PFQ-fundamentals-000000986 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 986
- Chapter: Bowel Elimination
- JSON path: `$.questions[985].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1709. PFQ-fundamentals-000000987 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 987
- Chapter: Bowel Elimination
- JSON path: `$.questions[986].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1710. PFQ-fundamentals-000000987 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 987
- Chapter: Bowel Elimination
- JSON path: `$.questions[986].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1711. PFQ-fundamentals-000000988 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 988
- Chapter: Bowel Elimination
- JSON path: `$.questions[987].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1712. PFQ-fundamentals-000000989 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 989
- Chapter: Bowel Elimination
- JSON path: `$.questions[988].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a postoperative patient who had a colostomy placed 2 days ago. The appliance needs to be changed for the first time. Which ostomy care actions can the nurse delegate to the nursing assistant? (Select all that apply.)
```

### 1713. PFQ-fundamentals-000000989 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 989
- Chapter: Bowel Elimination
- JSON path: `$.questions[988].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1714. PFQ-fundamentals-000000989 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 989
- Chapter: Bowel Elimination
- JSON path: `$.questions[988].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1715. PFQ-fundamentals-000000990 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 990
- Chapter: Bowel Elimination
- JSON path: `$.questions[989].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who will be having a colonoscopy the following morning. Which items must be removed from the patient‘s dinner tray since they are not allowed prior to the test? (Select all that apply.)
```

### 1716. PFQ-fundamentals-000000990 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 990
- Chapter: Bowel Elimination
- JSON path: `$.questions[989].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1717. PFQ-fundamentals-000000990 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 990
- Chapter: Bowel Elimination
- JSON path: `$.questions[989].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1718. PFQ-fundamentals-000000990 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 990
- Chapter: Bowel Elimination
- JSON path: `$.questions[989].rationale`
- Detail: Known source or extraction contamination detected.

```text
Patients who will undergo colonoscopy testing should have a clear liquid diet the day before the exam, so cream of chicken soup and coffee creamer should not be consumed. Foods with red food coloring should also be avoided prior to colonoscopy. 3rd Edition
```

### 1719. PFQ-fundamentals-000000990 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 990
- Chapter: Bowel Elimination
- JSON path: `$.questions[989].rationale`
- Detail: Pattern requires human review against the original source.

```text
Patients who will undergo colonoscopy testing should have a clear liquid diet the day before the exam, so cream of chicken soup and coffee creamer should not be consumed. Foods with red food coloring should also be avoided prior to colonoscopy. 3rd Edition
```

### 1720. PFQ-fundamentals-000000991 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 991
- Chapter: Urinary Elimination
- JSON path: `$.questions[990].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1721. PFQ-fundamentals-000000991 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 991
- Chapter: Urinary Elimination
- JSON path: `$.questions[990].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1722. PFQ-fundamentals-000000992 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 992
- Chapter: Urinary Elimination
- JSON path: `$.questions[991].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1723. PFQ-fundamentals-000000993 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 993
- Chapter: Urinary Elimination
- JSON path: `$.questions[992].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1724. PFQ-fundamentals-000000993 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 993
- Chapter: Urinary Elimination
- JSON path: `$.questions[992].rationale`
- Detail: Known source or extraction contamination detected.

```text
The patient with stress incontinence experiences loss of urine when coughing, sneezing, laughing, or exercising. The highest priority goal for this patient is to not experience incontinence at all and remain continent through all daily activities. If the patient remains continen…
```

### 1725. PFQ-fundamentals-000000994 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 994
- Chapter: Urinary Elimination
- JSON path: `$.questions[993].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1726. PFQ-fundamentals-000000995 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 995
- Chapter: Urinary Elimination
- JSON path: `$.questions[994].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1727. PFQ-fundamentals-000000996 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 996
- Chapter: Urinary Elimination
- JSON path: `$.questions[995].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1728. PFQ-fundamentals-000000996 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 996
- Chapter: Urinary Elimination
- JSON path: `$.questions[995].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1729. PFQ-fundamentals-000000997 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 997
- Chapter: Urinary Elimination
- JSON path: `$.questions[996].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a seriously ill patient whose laboratory results show a serum creatinine level of 3.5 mg/dL and a serum BUN of 35 mg/dL. Which conclusion can the nurse draw from these test results?
```

### 1730. PFQ-fundamentals-000000997 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 997
- Chapter: Urinary Elimination
- JSON path: `$.questions[996].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1731. PFQ-fundamentals-000000998 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 998
- Chapter: Urinary Elimination
- JSON path: `$.questions[997].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1732. PFQ-fundamentals-000000998 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 998
- Chapter: Urinary Elimination
- JSON path: `$.questions[997].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1733. PFQ-fundamentals-000000998 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 998
- Chapter: Urinary Elimination
- JSON path: `$.questions[997].rationale`
- Detail: Known source or extraction contamination detected.

```text
Patients in renal failure often require dialysis to reduce serum potassium levels to less than 5.5 mmol/L . Critically high serum potassium levels can lead to lethal arrhythmias and must be corrected promptly. Patients with advanced renal failure may require emergency hemodialys…
```

### 1734. PFQ-fundamentals-000000998 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 998
- Chapter: Urinary Elimination
- JSON path: `$.questions[997].rationale`
- Detail: Pattern requires human review against the original source.

```text
Patients in renal failure often require dialysis to reduce serum potassium levels to less than 5.5 mmol/L . Critically high serum potassium levels can lead to lethal arrhythmias and must be corrected promptly. Patients with advanced renal failure may require emergency hemodialys…
```

### 1735. PFQ-fundamentals-000000999 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 999
- Chapter: Urinary Elimination
- JSON path: `$.questions[998].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1736. PFQ-fundamentals-000001000 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1000
- Chapter: Urinary Elimination
- JSON path: `$.questions[999].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1737. PFQ-fundamentals-000001000 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1000
- Chapter: Urinary Elimination
- JSON path: `$.questions[999].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1738. PFQ-fundamentals-000001001 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1001
- Chapter: Urinary Elimination
- JSON path: `$.questions[1000].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1739. PFQ-fundamentals-000001002 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1002
- Chapter: Urinary Elimination
- JSON path: `$.questions[1001].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1740. PFQ-fundamentals-000001003 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1003
- Chapter: Urinary Elimination
- JSON path: `$.questions[1002].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1741. PFQ-fundamentals-000001003 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1003
- Chapter: Urinary Elimination
- JSON path: `$.questions[1002].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1742. PFQ-fundamentals-000001004 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1004
- Chapter: Urinary Elimination
- JSON path: `$.questions[1003].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1743. PFQ-fundamentals-000001004 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 1004
- Chapter: Urinary Elimination
- JSON path: `$.questions[1003].rationale`
- Detail: Pattern requires human review against the original source.

```text
The patient has acute urinary retention with overflow as evidenced by 1100 mL of urine in the bladder and frequent passage of small amounts of urine. The priority nursing diagnosi s is thus Impaired urination r/t obstruction of urinary bladder outlet. Urinary retention is the ca…
```

### 1744. PFQ-fundamentals-000001006 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1006
- Chapter: Urinary Elimination
- JSON path: `$.questions[1005].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1745. PFQ-fundamentals-000001006 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1006
- Chapter: Urinary Elimination
- JSON path: `$.questions[1005].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1746. PFQ-fundamentals-000001007 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1007
- Chapter: Urinary Elimination
- JSON path: `$.questions[1006].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1747. PFQ-fundamentals-000001007 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1007
- Chapter: Urinary Elimination
- JSON path: `$.questions[1006].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1748. PFQ-fundamentals-000001008 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 1008
- Chapter: Urinary Elimination
- JSON path: `$.questions[1007].stem`
- Detail: Pattern requires human review against the original source.

```text
The preceptor is watching a nursing student care for a male patient who requires a condom catheter. Which action by theNnUuRrsiSnIg NstuGdTenBt .inCdiOcaMtes that the procedure is performed correctly?
```

### 1749. PFQ-fundamentals-000001008 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1008
- Chapter: Urinary Elimination
- JSON path: `$.questions[1007].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1750. PFQ-fundamentals-000001009 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1009
- Chapter: Urinary Elimination
- JSON path: `$.questions[1008].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1751. PFQ-fundamentals-000001009 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1009
- Chapter: Urinary Elimination
- JSON path: `$.questions[1008].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1752. PFQ-fundamentals-000001010 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1010
- Chapter: Urinary Elimination
- JSON path: `$.questions[1009].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1753. PFQ-fundamentals-000001010 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 1010
- Chapter: Urinary Elimination
- JSON path: `$.questions[1009].rationale`
- Detail: Known source or extraction contamination detected.

```text
CT requires exposure to radiation similar to an x-ray, so the patient‘s provider and radiologist should be notified promptly of the possibility of pregnancy. The other conditions do not preclude CT scan examination for the patient. NCLEX Client Needs Category: Physiological Inte…
```

### 1754. PFQ-fundamentals-000001011 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1011
- Chapter: Urinary Elimination
- JSON path: `$.questions[1010].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1755. PFQ-fundamentals-000001012 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1012
- Chapter: Urinary Elimination
- JSON path: `$.questions[1011].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1756. PFQ-fundamentals-000001012 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1012
- Chapter: Urinary Elimination
- JSON path: `$.questions[1011].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1757. PFQ-fundamentals-000001012 — test-bank metadata

- Severity: **high**
- Category: Contamination
- Question index: 1012
- Chapter: Urinary Elimination
- JSON path: `$.questions[1011].rationale`
- Detail: Known source or extraction contamination detected.

```text
Concentrated dark urine indicates dehydration rather than infection of the urinary tract. Urine that smells of sweet fruit contains ketones from high blood sugar . Urine that is cloudy with a foul odor and positive for nitrites is most likely due to urinary tract infection. Freq…
```

### 1758. PFQ-fundamentals-000001012 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 1012
- Chapter: Urinary Elimination
- JSON path: `$.questions[1011].rationale`
- Detail: Pattern requires human review against the original source.

```text
Concentrated dark urine indicates dehydration rather than infection of the urinary tract. Urine that smells of sweet fruit contains ketones from high blood sugar . Urine that is cloudy with a foul odor and positive for nitrites is most likely due to urinary tract infection. Freq…
```

### 1759. PFQ-fundamentals-000001012 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1012
- Chapter: Urinary Elimination
- JSON path: `$.questions[1011].rationale`
- Detail: Pattern requires human review against the original source.

```text
Concentrated dark urine indicates dehydration rather than infection of the urinary tract. Urine that smells of sweet fruit contains ketones from high blood sugar . Urine that is cloudy with a foul odor and positive for nitrites is most likely due to urinary tract infection. Freq…
```

### 1760. PFQ-fundamentals-000001013 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1013
- Chapter: Urinary Elimination
- JSON path: `$.questions[1012].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1761. PFQ-fundamentals-000001013 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1013
- Chapter: Urinary Elimination
- JSON path: `$.questions[1012].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1762. PFQ-fundamentals-000001014 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1014
- Chapter: Urinary Elimination
- JSON path: `$.questions[1013].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1763. PFQ-fundamentals-000001014 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1014
- Chapter: Urinary Elimination
- JSON path: `$.questions[1013].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1764. PFQ-fundamentals-000001015 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1015
- Chapter: Urinary Elimination
- JSON path: `$.questions[1014].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1765. PFQ-fundamentals-000001015 — edition metadata

- Severity: **high**
- Category: Contamination
- Question index: 1015
- Chapter: Urinary Elimination
- JSON path: `$.questions[1014].rationale`
- Detail: Known source or extraction contamination detected.

```text
The nurse assistant can help the nurse by keeping the urine collection container cool on ice, dumping the urine from the patient‘s first void, and reminding the patient not to put toilet tissue in the urine specimen. NTheRnurIse aGsUs i sBSt a.n tCca nMa l so transport the speci…
```

### 1766. PFQ-fundamentals-000001016 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1016
- Chapter: Death and Loss
- JSON path: `$.questions[1015].stem`
- Detail: Pattern requires human review against the original source.

```text
The hospice nurse is caring for a terminally ill patient. The patient‘s son is distraught because the patient will probably die within the next few days and there is nothing he can do about it. What is the most appropriate nursing diagnosis for the patient‘s son currently?
```

### 1767. PFQ-fundamentals-000001016 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1016
- Chapter: Death and Loss
- JSON path: `$.questions[1015].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1768. PFQ-fundamentals-000001017 — space before punctuation

- Severity: **medium**
- Category: Text
- Question index: 1017
- Chapter: Death and Loss
- JSON path: `$.questions[1016].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a terminally ill patient whose children have come home to be with their mother during her last few days. They spend time looking through picture albums, watching old home movi es , and r eme mNbUe rRi nSg If uNn Gt iTmBe s.s pCeOn tMto ge th er. The nur s…
```

### 1769. PFQ-fundamentals-000001017 — possible split suffix

- Severity: **medium**
- Category: Text
- Question index: 1017
- Chapter: Death and Loss
- JSON path: `$.questions[1016].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a terminally ill patient whose children have come home to be with their mother during her last few days. They spend time looking through picture albums, watching old home movi es , and r eme mNbUe rRi nSg If uNn Gt iTmBe s.s pCeOn tMto ge th er. The nur s…
```

### 1770. PFQ-fundamentals-000001017 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1017
- Chapter: Death and Loss
- JSON path: `$.questions[1016].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1771. PFQ-fundamentals-000001017 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1017
- Chapter: Death and Loss
- JSON path: `$.questions[1016].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1772. PFQ-fundamentals-000001018 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1018
- Chapter: Death and Loss
- JSON path: `$.questions[1017].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1773. PFQ-fundamentals-000001019 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1019
- Chapter: Death and Loss
- JSON path: `$.questions[1018].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1774. PFQ-fundamentals-000001020 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1020
- Chapter: Death and Loss
- JSON path: `$.questions[1019].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1775. PFQ-fundamentals-000001020 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1020
- Chapter: Death and Loss
- JSON path: `$.questions[1019].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1776. PFQ-fundamentals-000001021 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1021
- Chapter: Death and Loss
- JSON path: `$.questions[1020].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1777. PFQ-fundamentals-000001022 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1022
- Chapter: Death and Loss
- JSON path: `$.questions[1021].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1778. PFQ-fundamentals-000001023 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1023
- Chapter: Death and Loss
- JSON path: `$.questions[1022].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1779. PFQ-fundamentals-000001024 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1024
- Chapter: Death and Loss
- JSON path: `$.questions[1023].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1780. PFQ-fundamentals-000001024 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1024
- Chapter: Death and Loss
- JSON path: `$.questions[1023].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1781. PFQ-fundamentals-000001025 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1025
- Chapter: Death and Loss
- JSON path: `$.questions[1024].stem`
- Detail: Pattern requires human review against the original source.

```text
The hospice nurse is caring for a several adult children shortly after the death of a parent. They have various reactions as they deal with their loss. The nurse recognizes which reactions to be in the cognitive domain?
```

### 1782. PFQ-fundamentals-000001025 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1025
- Chapter: Death and Loss
- JSON path: `$.questions[1024].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1783. PFQ-fundamentals-000001026 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1026
- Chapter: Death and Loss
- JSON path: `$.questions[1025].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1784. PFQ-fundamentals-000001026 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1026
- Chapter: Death and Loss
- JSON path: `$.questions[1025].rationale`
- Detail: Pattern requires human review against the original source.

```text
Often caregivers neglect their own needs while in the caregiver role. The spouse understands the patient will die soon and is being realistic in understanding his or her o wn physical needs have been neglected. This shows healthy coping.
```

### 1785. PFQ-fundamentals-000001027 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1027
- Chapter: Death and Loss
- JSON path: `$.questions[1026].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1786. PFQ-fundamentals-000001027 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1027
- Chapter: Death and Loss
- JSON path: `$.questions[1026].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1787. PFQ-fundamentals-000001028 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1028
- Chapter: Death and Loss
- JSON path: `$.questions[1027].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1788. PFQ-fundamentals-000001028 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1028
- Chapter: Death and Loss
- JSON path: `$.questions[1027].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1789. PFQ-fundamentals-000001029 — multiple spaces

- Severity: **medium**
- Category: Text
- Question index: 1029
- Chapter: Death and Loss
- JSON path: `$.questions[1028].stem`
- Detail: Pattern requires human review against the original source.

```text
The home care nurse is caring for a terminally ill patient who states that he wants to set up a scholarship in his name at the local university before he dies. What is the best action by the nurse?
```

### 1790. PFQ-fundamentals-000001029 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1029
- Chapter: Death and Loss
- JSON path: `$.questions[1028].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1791. PFQ-fundamentals-000001030 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1030
- Chapter: Death and Loss
- JSON path: `$.questions[1029].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1792. PFQ-fundamentals-000001031 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1031
- Chapter: Death and Loss
- JSON path: `$.questions[1030].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1793. PFQ-fundamentals-000001031 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1031
- Chapter: Death and Loss
- JSON path: `$.questions[1030].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1794. PFQ-fundamentals-000001032 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1032
- Chapter: Death and Loss
- JSON path: `$.questions[1031].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1795. PFQ-fundamentals-000001033 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1033
- Chapter: Death and Loss
- JSON path: `$.questions[1032].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1796. PFQ-fundamentals-000001034 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1034
- Chapter: Death and Loss
- JSON path: `$.questions[1033].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1797. PFQ-fundamentals-000001035 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1035
- Chapter: Death and Loss
- JSON path: `$.questions[1034].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1798. PFQ-fundamentals-000001036 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1036
- Chapter: Death and Loss
- JSON path: `$.questions[1035].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1799. PFQ-fundamentals-000001036 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1036
- Chapter: Death and Loss
- JSON path: `$.questions[1035].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1800. PFQ-fundamentals-000001037 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1037
- Chapter: Death and Loss
- JSON path: `$.questions[1036].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1801. PFQ-fundamentals-000001038 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1038
- Chapter: Death and Loss
- JSON path: `$.questions[1037].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1802. PFQ-fundamentals-000001038 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1038
- Chapter: Death and Loss
- JSON path: `$.questions[1037].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1803. PFQ-fundamentals-000001039 — space inside parentheses

- Severity: **medium**
- Category: Text
- Question index: 1039
- Chapter: Death and Loss
- JSON path: `$.questions[1038].stem`
- Detail: Pattern requires human review against the original source.

```text
The nurse is caring for a patient who just died after a lengthy illne ss. Which portions of postmortem care may be delegated by the nurse to the nursing assistant? ( Select all that apply.)
```

### 1804. PFQ-fundamentals-000001039 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1039
- Chapter: Death and Loss
- JSON path: `$.questions[1038].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1805. PFQ-fundamentals-000001039 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1039
- Chapter: Death and Loss
- JSON path: `$.questions[1038].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1806. PFQ-fundamentals-000001040 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1040
- Chapter: Death and Loss
- JSON path: `$.questions[1039].choices[0].label`
- Detail: Pattern requires human review against the original source.

```text
A
```

### 1807. PFQ-fundamentals-000001040 — abrupt ending

- Severity: **high**
- Category: Text
- Question index: 1040
- Chapter: Death and Loss
- JSON path: `$.questions[1039].correct_answers[0]`
- Detail: Pattern requires human review against the original source.

```text
A
```
