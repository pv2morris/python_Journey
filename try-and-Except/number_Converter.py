while True:
    usr_Input = input("Enter a number to be converted to a float: ")
    if usr_Input == "":
        print("See you later!")
        break
    try:
        converted = float(usr_Input)
        print("Your number has been successfully converted!")
    except ValueError:
        print("Only a number can be accepted.")