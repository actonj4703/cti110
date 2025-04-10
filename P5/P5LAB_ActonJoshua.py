# Joshua Acton
# 04/10/2025
# P5LAB
#Calculate change

import random
def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    amount_paid = float(input("How much cash will you put into the self_checkout? "))

    change_owed = amount_paid - amount_owed

    print(f"Change is ${change_owed:.2f}")
    print()

    change_owed = round(change_owed * 100)
    disperse_change(change_owed)



def disperse_change(change):
    if change == 0:
        print("No Change Due!")

    # calculate change for each coin type
    # integer division //
    num_dollars = change // 100
    change = change % 100
    #change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change % 25
    #change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change % 10
    #change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change % 5
    #change = change - (num_nickels * 5)

    num_pennies = change // 1

    # display amounts used

    if num_dollars > 0:
        print(num_dollars, end=' ')
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")

    if num_quarters > 0:
        print(num_quarters, end=' ')
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")
    if num_dimes > 0:
        print(num_dimes, end=' ')
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")
    if num_nickels > 0:
        print(num_nickels, end=' ')
        if num_nickels == 1:
            print("Nickel")
        else:
            print("Nickels")
    if num_pennies > 0:
        print(num_pennies, end=' ')
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")
        





main()