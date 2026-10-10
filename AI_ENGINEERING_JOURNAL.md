# AI Engineering Journal

## Experiment
Student CGPA Performance Management System

---

## Interaction 1 – Code Generation

### Prompt
Create a Python function to calculate CGPA from a list
of grade points.

### AI Suggestion
AI generated a CGPA calculation function.

### Human Validation
The generated code was reviewed manually.
Input validation was added to prevent invalid grade points.

### Decision
Accepted after modification.

---

## Interaction 2 – Test Generation

### Prompt
Generate pytest unit tests for the CGPA calculation function.

### AI Suggestion
AI generated tests for normal and invalid inputs.

### Human Validation
The tests were reviewed and executed using pytest.

### Result
All tests passed.

---

## Interaction 3 – Code Explanation

### Prompt
Explain the calculate_cgpa function line by line.

### AI Suggestion
AI explained the validation, calculation and rounding.

### Human Validation
The explanation was compared with the actual implementation.

### Decision
Explanation accepted.

---

## Interaction 4 – Debugging

### Problem
A test failed because an incorrect calculation was introduced.

### AI Prompt
Identify the likely cause of the failing test.

### AI Suggestion
AI identified an incorrect calculation.

### Human Action
The developer manually corrected the code.

### Result
All tests passed.

---

## Interaction 5 – Refactoring

### Prompt
Suggest improvements for readability and maintainability.

### AI Suggestion
AI suggested type hints, documentation and
improved code organization.

### Human Validation
Suggestions were reviewed before implementation.

### Decision
Useful suggestions were accepted.