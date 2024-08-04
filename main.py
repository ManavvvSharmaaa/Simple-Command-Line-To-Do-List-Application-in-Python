import os
import json

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description):
    tasks.append({'description': description, 'completed': False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        status = 'Done' if task['completed'] else 'Not Done'
        print(f"{index + 1}. [{status}] {task['description']}")

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print(f"Marked task {index + 1} as complete.")
    else:
        print("Invalid task number.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {task['description']}")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            list_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark as complete: ")) - 1
                complete_task(tasks, task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            list_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
