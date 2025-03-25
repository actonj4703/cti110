


keep_going = 'yes'
total = 0

while keep_going.lower() == 'yes':
    num = int(input("Enter a number: "))
    total += num
    keep_going = input("Do you want to run the program again? Enter yes or no: ")
    print(total)

