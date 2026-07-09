
# tasks = []

import json
file= open("data.json", "r")
x=file.read()
finaldata=json.loads(x)

def generateID():
    if finaldata:
        # print('my list is not empty')
        last_item_id = finaldata[-1]['id']
        return last_item_id + 1
        # last_item = my_list[-1]
    else:
        return 1
        # print("The list is empty!")
        

def viewAllTasks():
    if len(finaldata) == 0:
        print("No tasks found.")
    else:
        # sln = id
        for item in finaldata:
            item_id = item["id"]
            print(f"{item_id} . {item["title"]}")
            # sln += 1

def addTask(taskParam):
    finaldata.append(taskParam)
    write_file= open("data.json", "w")
    json.dump(finaldata, write_file, indent=4)
    print("Task added")


def updateStatus(id, status):
    # finaldata.append(taskParam)
    index = id -1 
    item = finaldata[index]
    print("write 1 if completed, write 2 if due")

    item["completed"] = status
    write_file= open("data.json", "w")
    json.dump(finaldata, write_file, indent=4)
    print("Task added")


def removeTask():
    viewAllTasks()
    toRemove = int(input("Enter task number: "))
    tasks.pop(toRemove-1)

while True:
    print("-TO-DO LIST-")
    print("1. View All Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        viewAllTasks()

    elif choice == "2":
        task_title = input("Enter a task: ")
        newID= generateID()
        new_task = {
            "id": newID,
            "title": task_title,
            "completed": False,
            "created_at": "2026-07-04",
            "due_date": "2026-07-08"
        }
        addTask(new_task)

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


