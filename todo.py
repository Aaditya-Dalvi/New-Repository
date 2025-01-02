import os

TODO_FILE = "tasks.txt"

def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")
    print(f"Task added: {task}")

def view_tasks():
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    print("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

def remove_task(task_number):
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    try:
        task_number = int(task_number)
        removed_task = tasks.pop(task_number - 1)
        with open(TODO_FILE, "w") as file:
            file.writelines(tasks)
        print(f"Removed task: {removed_task.strip()}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def clear_tasks():
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)
        print("All tasks cleared.")
    else:
        print("No tasks to clear.")

def main():
    print("Welcome to To-Do List Manager!")
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = input("Enter task number to remove: ").strip()
            remove_task(task_number)
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
