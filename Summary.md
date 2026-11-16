# Project Summary – To-Do List Application

The To-Do List Application is a menu-driven Python 3 program that helps users manage daily tasks.

## Main Features
- Add a task with a unique task number.
- View all tasks and their current status.
- Mark a selected task as completed.
- Delete a selected task.
- Store tasks permanently in `todo.txt`.
- Load previously saved tasks when the program starts.

## Functions Used
- `add_task()` – Adds a new task after validating its title.
- `view_tasks()` – Displays all tasks or an empty-list message.
- `complete_task()` – Changes the selected task status to `Done`.
- `delete_task()` – Removes the selected task.
- `save_tasks()` – Saves the current task list to the file.
- `load_tasks()` – Loads tasks from the file safely.
- `main()` – Displays the menu and controls the program.

## Concepts Applied
Lists, dictionaries, functions, loops, conditional statements, file handling, and exception handling.

## Result
The application provides the required add, view, complete, and delete operations. Task information is saved after every change and can be accessed again when the program is restarted.
