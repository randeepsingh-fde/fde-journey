
tasks = []

try:
    with open("todo.txt", "r") as file:
        for line in file:
            line_new = line.strip()
            tasks.append(line_new)
except FileNotFoundError:
    tasks = []

while True:
    print("========== TO-DO LIST ==========")
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Mark task as completed")
    print("5. Quit")

    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter a task: ").strip()
        if len(task) <= 0:
            print("Task can not be empty")
        else:
            tasks.append(task)
            print("Task added to the list.")
            with open("todo.txt", "w") as file:
                for i in tasks:
                    file.write(i+"\n")

    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            for i, j in enumerate(tasks, start=1):
                print(f"{i}. {j}")

    elif choice == "3":
        if not tasks:
            print("No tasks in the list to be deleted.")
        else:
            for i, j in enumerate(tasks, start=1):
                print(f"{i}. {j}")
            try:
                delete = int(input("Enter task number to delete: "))
                if 1 <= delete <= len(tasks):
                    tasks.pop(delete-1)
                    print("Task deleted successfully.")
                    with open("todo.txt", "w") as file:
                        for i in tasks:
                            file.write(i+"\n")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("It should be an integer.")

    elif choice == "4":
        if not tasks:
            print("Tasks list is empty.")
        else:
            for i, j in enumerate(tasks, start=1):
                print(f"{i}. {j}")
            try:
                complete = int(input("Enter task number to mark as completed: "))
                if 1 <= complete <= len(tasks):
                    if tasks[complete - 1].startswith("[x]"):
                        print("This task is already completed.")
                    else:
                        tasks[complete - 1] = "[x] " + tasks[complete - 1]
                        with open("todo.txt", "w") as file:
                            for i in tasks:
                                file.write(i+"\n")
                        print("Task marked completed successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("It should be an integer")

    elif choice == "5":
        print("Thanks for using the TO-DO list.")
        break

    else:
        print("Choose a valid option from the menu.")
