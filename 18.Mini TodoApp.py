#Mini To-Do App

# json_data =[
#     {"task": "Learn Python JSON", "status": "Incomplete"},
#     {"task": "Build a To-Do App", "status": ""}
# ]

import json

with open('json_data.json','r') as file:
    tasks = json.load(file)
    print(tasks)

tasks = [
    {"task": "Complete Project", "status": "Incomplete"}
]

with open('tasks.json','w') as file:
    json.dump(tasks, file, indent=4)

with open('tasks.json','r') as file:
    tasks = json.load(file)

tasks.append({"task": "Learn Python", "status": "Incomplete"})

with open('tasks.json','w') as file:
    json.dump(tasks, file, indent=2)


with open('tasks.json','r') as file:
    tasks = json.load(file)

tasks.append({"task": "Learn Python 2", "status": "Incomplete"})

with open('tasks.json', 'w') as file:
    json.dump(tasks, file, indent=2)


#Mini To-Do App Using JSON
import json
import os

#File for storing tasks
TASK_FILE='my_tasks.json'

if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'w') as file:
        json.dump([], file)

#Step 1: Load Tasks from JSON
def load_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

#Step 2: Save Tasks to JSON
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

#Step 3: Add a new task
def add_task():
    task_name = input("Enter the task name: ").strip()
    tasks = load_tasks()
    tasks.append({"task": task_name, "status": "Incomplete"})
    save_tasks(tasks)
    print(f'Task "task" added successfully !')

#Step 4: View All Tasks
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n--- To-Do List ------")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['task']} - {task['status']}")
    else:
        print("No tasks found.")

#Step 5: Update Task Status
def update_status():
    task = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_status = input("Enter the new status (Complete/Incomplete): ").strip()
            tasks[task_index]['status']= new_status
            save_tasks(tasks)
            print("Task status updated sucessfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

#Step 6: Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delte: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f'Task "{deleted_task['task']}" deleted successfully!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

#Step 7: Display Menu
def display_menu():
    print("\n----- Mini To-Do Menu -----")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update task status")
    print("4. Delete a task")
    print("5. Exit")

#Step 8: Main Program Loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ").strip()
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_status()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the To-Do List App. Goodbye!")
        break 
    else:
        print("Invalid Choice. Please enter a number between 1 and 5.")