import json
import os

FILENAME = "todo.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return json.load(f)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a task
def add_task(task_text):
    tasks = load_tasks()
    tasks.append({"task": task_text, "done": False})
    save_tasks(tasks)
    print("Task added.")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{idx+1}. [{status}] {task['task']}")

# Mark task as done
def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    except IndexError:
        print("Error: Invalid task number.")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    except IndexError:
        print("Error: Task number doesn't exist.")

# Command loop
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(index)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            list_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
