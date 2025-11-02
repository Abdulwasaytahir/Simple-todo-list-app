# Simple To-Do List App

tasks = []  # List to store tasks


def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task added: {task}\n")


def show_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    print("\n------ Your Tasks ------")
    for i, t in enumerate(tasks, start=1):
        status = "Done" if t["done"] else "Not Done"
        print(f"{i}. {t['task']} - {status}")
    print("------------------------")
    print(f"Total Tasks: {len(tasks)}\n")


def mark_done():
    show_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print(f"Task marked as done: {tasks[num]['task']}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task():
    show_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            deleted = tasks.pop(num)
            print(f"Deleted task: {deleted['task']}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! Keep working on your goals.")
            break
        else:
            print("Invalid option! Try again.\n")


if __name__ == "__main__":
    main()
