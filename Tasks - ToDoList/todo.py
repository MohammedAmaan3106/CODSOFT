import os
import json

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        content = f.read().strip()
        if not content:
            return []
        return json.load(content)
    

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks,f,indent =2)

# Show tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

# Add task
def add_task(tasks):
    task = input("Enter new task: ")
    due = input("Enter due date (e.g. 30-Apr): ")
    tasks.append(f"{task} [Due: {due}]")
    save_tasks(tasks)
    print("Task added!")

# Mark complete
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num-1] += " ✔"
        save_tasks(tasks)
        print("Task marked as complete!")
    except:
        print("Invalid input!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num-1)
        save_tasks(tasks)
        print(f"Deleted: {removed}")
    except(ValueError,IndexError):
        print("Invalid input!")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
