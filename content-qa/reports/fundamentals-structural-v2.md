# Fundamentals QA — structural

> Review queue only. The Pack has not been modified.

- Findings: **9**
- Questions affected: **9**

## Counts by rule

- duplicate correct answers: 8
- correct answer not found in choices: 1

## Findings

### 1. PFQ-fundamentals-000000024 — duplicate correct answers

- Question index: 24
- Severity: high
- JSON path: `$.questions[23].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["A", "B", "C", "D", "B", "C"]
```

### 2. PFQ-fundamentals-000000093 — duplicate correct answers

- Question index: 93
- Severity: high
- JSON path: `$.questions[92].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "B", "C"]
```

### 3. PFQ-fundamentals-000000191 — correct answer not found in choices

- Question index: 191
- Severity: high
- JSON path: `$.questions[190].correct_answers`
- Detail: Available choice labels: ['B', 'C', 'D']

```text
A
```

### 4. PFQ-fundamentals-000000518 — duplicate correct answers

- Question index: 518
- Severity: high
- JSON path: `$.questions[517].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "B", "C"]
```

### 5. PFQ-fundamentals-000000566 — duplicate correct answers

- Question index: 566
- Severity: high
- JSON path: `$.questions[565].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["A", "B", "D", "E", "B", "C"]
```

### 6. PFQ-fundamentals-000000654 — duplicate correct answers

- Question index: 654
- Severity: high
- JSON path: `$.questions[653].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "B", "C"]
```

### 7. PFQ-fundamentals-000000795 — duplicate correct answers

- Question index: 795
- Severity: high
- JSON path: `$.questions[794].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "C", "E", "B", "C"]
```

### 8. PFQ-fundamentals-000000871 — duplicate correct answers

- Question index: 871
- Severity: high
- JSON path: `$.questions[870].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["C", "E", "F", "B", "C"]
```

### 9. PFQ-fundamentals-000000955 — duplicate correct answers

- Question index: 955
- Severity: high
- JSON path: `$.questions[954].correct_answers`
- Detail: Correct-answer list contains duplicate values.

```text
["B", "B", "C"]
```
