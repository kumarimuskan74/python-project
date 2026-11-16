# To-Do List Application

## Project Information
- **PS No.:** 5
- **Project Title:** To-Do List Application
- **Language:** Python 3
- **Semester:** First Semester
- **Concepts:** Lists, Functions, Loops, File Handling

## Description
This is a menu-driven To-Do List Application developed using Python. It allows users to add tasks, view all tasks, mark tasks as completed, and delete tasks. Tasks are stored in `todo.txt`, so the list is loaded when the program starts and saved after every change.

## Features
1. Add a new task.
2. View all saved tasks.
3. Mark a task as completed.
4. Delete a task.
5. Save and load tasks using file handling.
6. Validate empty task titles and invalid task numbers.
7. Handle a missing `todo.txt` file safely.

## Project Files
- `todo_list.py` – Main Python program.
- `todo.txt` – File used to store tasks.
- `README.md` – Project documentation.
- `Summary.md` – Brief project summary.

## Requirements
- Python 3 installed on your computer.
- A code editor or terminal.

## How to Run
1. Open the project folder in VS Code or a terminal.
2. Open the terminal in that folder.
3. Run:

   ```bash
   python todo_list.py
   ```

   On some systems, use:

   ```bash
   python3 todo_list.py
   ```

4. Select a menu option from 1 to 5.

## Menu Options
| Option | Action |
|---|---|
| 1 | Add Task |
| 2 | View Tasks |
| 3 | Complete Task |
| 4 | Delete Task |
| 5 | Exit |

## Task Storage
Each task is stored in `todo.txt` in this format:

```text
1|Buy books|Pending
2|Pay bill|Pending
```

Task numbers begin at 1. New tasks are assigned the next available number and start with the status `Pending`. Completed tasks use the status `Done`.

## Test Cases
The project is designed to cover the four test cases in the problem statement:
1. Normal input – add a task.
2. Boundary/minimum input – view an empty list.
3. Invalid input – complete a task number that does not exist and try to add an empty title.
4. Different valid scenario – add two tasks, complete task 1, view tasks, and delete task 2.

## Concepts Used
- Lists and dictionaries
- User-defined functions
- `while` loop and conditional statements
- File handling with `open()`
- Exception handling with `try-except`
- Input validation
