def program1():
    print("you are in program 1")
    
def program2():
    print("you are in program 2")
    
def program3():
    print("you are in program 3")
            
def main():
    keep_going = 'y'
    while (keep_going.lower()=='y'):
        #print menu
        print('\nMenu')
        print('  1. Program 1')
        print('  2. Program 2')
        print('  3. Program 3')
        print('  4. Exit Program\n')
        choice = int(input('Please enter your choice: '))
        #get choice
        if choice == 1:
            program1()
        elif choice == 2:
            program2()
        elif choice == 3:
            program3()
        elif choice == 4:
            print("Choice was 4.")
            print("Exiting program")
            print("Goodbye")
            keep_going = 'n'
        else:
            print('Choice was not valid.  Please choose a valid option.')
            input('Press any key to continue.')
main()


            
            
