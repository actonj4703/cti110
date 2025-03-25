#Joshua Acton
#03/25/2025
#P4LAB2
#Write a program that asks the user to enter an integer

keep_going = 'yes'

while keep_going.lower() == 'yes':
    
    num = int(input("Enter an integer: "))
    print("\n")
    if(num >= 0):
        for i in range(1,12+1):
         print(f'{num} * {i} = {num * i}')
    else:
        print("This program does not handle negative values")
        print("\n")
    keep_going = input("Do you want to run the program again? Enter yes or no: ")
print("\n")
print("Exiting the program...")












    
