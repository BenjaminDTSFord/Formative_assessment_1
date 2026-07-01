def times_table_select():
    
    while True:
        print("Which times table would you like to practice?")
        print("Enter a number from 1 to 12")
        print("or alternatively enter R to be tested randomly on any of the times tables")

        times_table_choice = input("Enter your choice:")

        if times_table_choice == "R":
            return "R"
    
        elif times_table_choice.isdigit():
            times_table_choice = int(times_table_choice)

            if times_table_choice in range(1, 13):
                return times_table_choice
    
        print("Incorrect choice, please try again")