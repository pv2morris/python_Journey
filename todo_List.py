import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear()
    print("+____________________________________________+")
    print("|                   MENU                     |")
    print("|============================================|")
    print("|                                            |")
    print("|   1. Add a new task                        |")
    print("|   2. View all tasks                        |")
    print("|   3. Mark a task completed                 |")
    print("|   4. Exit the program                      |")
    print("|                                            |")
    print("+============================================+")
    print("")

tasks = []

def disp_Tasks(tasks):
    display = ""
    for i, task in enumerate(tasks, start=1):
        display += f"{i}. {task}\n"
    if display == "":
        print("There are currently no tasks.")
    else:
        return display
    return display

def start_Over():
    input("Press any key to return to the menu...")

def add_Task():
    try:
        tasks.append(str(new_task))
    except ValueError:
        print("Please enter the new task as a text string.")
        start_Over()

while True:
    menu()
    option = input("Please choose an option: ")
    if option == "1":
        menu()
        while True:
            new_task =  input("Add a task or enter\nto return to the menu: ")
            if new_task == "":
                break
            else:
                add_Task()
            menu()

    elif option == "2":
        menu()
        print(disp_Tasks(tasks))
        start_Over()

    elif option == "3":
        menu()
        print(disp_Tasks(tasks))
        try:
            task_Num = int(input("Which task would you like to mark completed? "))
            if 1 <= task_Num <= len(tasks):
                rem_Task = tasks.pop(task_Num -1)
                menu()
                print(f"Task '{rem_Task}' has been marked completed and removed from the list.\n")
                print(disp_Tasks(tasks))
                start_Over()
            else:
                print("Invalid task number.")
                start_Over()
        except ValueError:
            print("Please enter a valid task number.")
            start_Over()
    
    elif option == "4":
        clear()
        break