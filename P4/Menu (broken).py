choice = 'y'
while(choice.lower() == 'y'):
    #print menu
    print("menu")
    print("1. Program 1")
    print("2. Program 2")
    print("3. Program 3")
    print("4. Exit the Program\n")
   # choice = input("Do you want to run the program again? Enter y/n: ")
    #print("Exiting The Program!")
    value = int(input("Please enter your choice: "))
    if value == 1:
        print("You picked option 1")
    elif value == 2:
        print("You picked option 2")
    elif value == 3:
        print("you picked option 3")
    elif value == 4:
        print("You picked option 4")
        print("Exiting the program")
        print("Goodbye")
    choice = 'n'
else:
    print("Invalid choice. Please pick a valid option!")
    input("Press any key to continue")