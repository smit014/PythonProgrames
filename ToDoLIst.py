"""To-Do List Manager: Build a program to manage a to-do list,
allowing users to add, remove, and view tasks."""
tasks = []


def AddTask(TaskName, TaskDescription):
    task = {"Name": TaskName, "Description": TaskDescription}
    tasks.append(task)


def RemoveTask(TaskName):
    for task in tasks:
        if task["Name"] == TaskName:
            tasks.remove(task)
            return True
    return False


def view_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. Name: {task['Name']}, Description: {task['Description']}")


while True:
    print("\n*** Task Management Menu ***")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        TaskName = input("Enter the task Name: ")
        TaskDescription = input("Enter the task Description: ")

        AddTask(TaskName, TaskDescription)
        print("Task added successfully!")

    elif choice == "2":
        TaskName = input("Enter the task Name to remove: ")

        if RemoveTask(TaskName):
            print(f"Task '{TaskName}' removed successfully!")
        else:
            print(f"Task '{TaskName}' not found!")

    elif choice == "3":
        if not tasks:
            print("No tasks to display.")
        else:
            print("\n*** Tasks ***")
            view_tasks()

    elif choice == "4":
        print("Exiting the Task Management Program.")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
