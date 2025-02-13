#Joshua Acton
#2-13-2025
#P1HW2
#This program will demo python code

print()
print("This program calculates and displays travel expenses")

print()

budget= int(input("Enter Budget: "))

print()

travel= str(input("Enter your travel destination: "))

print()

gas= int(input("How much do you think you will spend on gas? "))

print()

hotel= int(input("Approximately, how much will you need for accomodation/hotel? "))

print()

food= int(input("Last, how do you need for food? "))

print()

print("-"*12, "Travel Expenses","-"*12)

print("Location: ",travel)
print("Initial Budget: ",(budget))
#calculation
print()
print()


print("Fuel:",(gas))
print("Accomodation:",(hotel))
print("Food:",(food))





balance=budget-gas-hotel-food
print()
print()
print("Remaining Balance:",(balance))














##pseudocode
##Ask user to enter their budget
##Ask user to enter travel destination
##Ask user for amount they will spend on gas
##Ask user for amount they will spend on accommodation
##Ask user for amount they will spend on food
##Add expenses
##Subtract expenses from budget
##Display results
