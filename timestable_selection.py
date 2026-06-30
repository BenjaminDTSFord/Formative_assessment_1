import random

def timestable_select():
    
    while True:
        print("Which timestable would you like to practice?")
        print("Enter a number from 1 to 12")
        print("or alternatively enter R to be tested randomly on any of the times tables")

        timestable_choice = input("Enter your choice")

        if timestable_choice == "R":
            return "R"
    
        elif timestable_choice.isdigit():
            timestable_choice = int(timestable_choice)

            if timestable_choice in range (1, 13):
                return timestable_choice
    
        print("incorrect choice, please try again")