import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear()
    print("+____________________________________________+")
    print("|           LEt mE PiCk yOuR BrAiN           |")
    print("|============================================|")
    print("|                                            |")
    print("|    Think of a number between 1 and 100.    |")
    print("|                                            |")
    print("|        I'll see if I can guess it!         |")
    print("|                                            |")
    print("+============================================+")
    print("")
    
menu()

input("Press enter when your ready!")

low = 1
high = 100

while True:
    menu()
    guess = (low + high) //2
    
    answer = input(f"Your number is {guess}!\n\n1. Too high\n2. Too low\n3. YES!\n\nAm I right? ")
    if answer == "1":
        high = (guess - 1)
    elif answer == "2":
        low = (guess + 1)
    elif answer == "3":
        menu()
        print(f"I knew it! Your number is {guess}!\n\n")
        break
    else:
        print:("Please enter a valid option (1, 2, or 3).")