import os
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear()
    print("+____________________________________________+")
    print("|      cAn YOu GuEss whAt i'M tHinKIng!?     |")
    print("|============================================|")
    print("|                                            |")
    print("|  I'll think of a number between 1 and 100  |")
    print("|                                            |")
    print("|          See if you can guess it!          |")
    print("|                                            |")
    print("+============================================+")
    print(" Enter 'exit' to end the game.\n")

number_to_Guess = random.randint(1,100)

menu()

while True:
    user_input = input("What's your guess?: ")

    if user_input.lower() == "exit":
        print(f"\nOh.. Well, thanks for playing, I guess.\n...it was {number_to_Guess}, by the way...\n\n")
        break
    try:
        user_Guess = int(user_input)
        if user_Guess == number_to_Guess:
            print(f"\nOMG... How did you even guess that?!\n...are you peeking at my code?\nYes, the number was {number_to_Guess}.")
            break
        elif user_Guess < number_to_Guess:
            print("\nAwe... Too low. Try again.")
        else:
            print("\nWhoa... Too high. Calm down and try again.")
    except ValueError:
        print("\nUm... This is a number game. Enter a number doofus.\n")