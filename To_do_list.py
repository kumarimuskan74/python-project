
import os

FILE_NAME = "todo.txt"


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(
                f"{task['number']}|{task['title']}|{task['status']}\n"
            )


def load_tasks():
    tasks = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) == 3:
                    try:
                        task = {
                            "number": int(parts[0]),
                            "title": parts[1],
                            "status": parts[2]
                        }
                        tasks.append(task)
                    except ValueError:
                        continue

    return tasks



def add_task(tasks):
    title = input("Enter task title: ").strip()

    if title == "":
        print("Task title cannot be empty.")
        return

    if "|" in title:
        print("Task title cannot contain |.")
        return

    if tasks:
        task_number = max(task["number"] for task in tasks) + 1
    else:
        task_number = 1

    task = {
        "number": task_number,
        "title": title,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added. {task_number} | {title} | Pending")



def view_tasks(tasks):
    if not tasks:
        print("No tasks found. Your to-do list is empty.")
        return

    print("\nYour To-Do List:")

    for task in tasks:
        print(
            f"{task['number']} | {task['title']} | {task['status']}"
        )



def complete_task(tasks):
    try:
        number = int(input("Enter task number to complete: "))
    except ValueError:
        print("Invalid task number.")
        return

    for task in tasks:
        if task["number"] == number:
            task["status"] = "Done"
            save_tasks(tasks)
            print(f"Task number {number} marked as completed.")
            return

    print(f"Task number {number} not found.")


# Delete a task
def delete_task(tasks):
    try:
        number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Invalid task number.")
        return

    for task in tasks:
        if task["number"] == number:
            tasks.remove(task)
            save_tasks(tasks)
            print(
                f"Task {number} deleted. Tasks left: {len(tasks)}"
            )
            return

    print(f"Task number {number} not found.")



def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Exiting To-Do List Application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

