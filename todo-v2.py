
tasks = []

def viewAllTasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        sln = 1
        for task in tasks:
            print(f"{sln} . {task}")
            sln += 1

def addTask(taskParam):
    tasks.append(taskParam)
    print("Task added")

def removeTask():
    viewAllTasks()
    toRemove = int(input("Enter task number: "))
    tasks.pop(toRemove-1)

while True:
    print("-TO-DO LIST-")
    print("1. View Due Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        viewAllTasks()

    elif choice == "2":
        task = input("Enter a task: ")

        addTask(task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove")
        else:
            removeTask()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


