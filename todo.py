tasks = []

while True:
    print("-TO-DO LIST-")
    print("1. View Due Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print(len(tasks))

    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove")
        else:
            i=0 
            while i<len(tasks):
                print(f"{i+1}.{tasks[i]}")
                i+=1

                num = int(input("Enter task number: "))

                if 1 <= num and num <= len(tasks):
                    rem=tasks.pop(num-1)
                    print(f"{rem} removed from the list.")
                else: 
                    print("Task number is invalid, try with a valid number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")