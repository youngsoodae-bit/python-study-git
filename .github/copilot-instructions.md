# Copilot Instructions for 20250913-main

## Project Overview
This codebase is a collection of Python scripts for basic programming education, focusing on fundamental concepts such as variables, data types, lists, input/output, and simple data manipulation. Each file demonstrates a specific concept or workflow, often with step-by-step comments in Korean.

## File Structure & Patterns
- Each file (`20250913.py`, `20250913_2.py`, ..., `20250913_10.py`, `20250914_1.py`) is a standalone script, typically illustrating a single topic or exercise.
- Scripts are sequentially numbered, suggesting a lesson or progression order.
- Comments (often in Korean) explain the purpose and logic of each code block.
- No shared modules, classes, or cross-file imports—each script is independent.

## Key Conventions
- Use clear, commented code to explain concepts (especially for beginners).
- Demonstrate both correct and incorrect usage (e.g., shallow vs. deep copy in lists).
- Favor explicit variable names and stepwise logic for educational clarity.
- Input/output is handled via `input()` and `print()`; expect interactive console use.
- Temporary variables and stepwise mutation (e.g., list `append`, `pop`, `insert`) are common.

## Developer Workflows
- No build system or test framework is present; run scripts directly with Python 3.x:
  ```powershell
  python 20250913_5.py
  ```
- Some scripts require user input; be prepared to provide values interactively.
- No external dependencies except for the standard library (e.g., `time`).

## Examples
- List manipulation and restoration: see `20250913_10.py` for a stepwise delete/restore pattern using `pop`, `append`, and `insert`.
- Variable mutation and reassignment: see `20250913_3.py` and `20250913_4.py`.

## Guidance for AI Agents
- When adding new scripts, follow the sequential naming and comment-rich style.
- Keep each script focused on a single concept or lesson.
- Use Korean for comments if matching the existing style.
- Avoid introducing complex abstractions or dependencies unless explicitly requested.

## Reference
- For overall structure and style, see `README.md` and the numbered script files.
