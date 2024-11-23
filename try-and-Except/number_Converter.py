while True:
    print("Welcome to the number type converter!")
    usr_Input = input("\nEnter a number or\npress enter to exit: ")
    if usr_Input == "":
        print("\nSee you later!\n")
        break
    try:
        if '.' in usr_Input:
            conv_num = float(usr_Input)
            print(f"\nThe number {usr_Input} is now a float ({conv_num})!")
        else:
            conv_num = int(usr_Input)
            print(f"\nThe number {usr_Input} is now an integer ({conv_num})!")
    except ValueError:
        print("\n\nInvalid Input! Please enter a number (e.g., 42, or 3.14).")