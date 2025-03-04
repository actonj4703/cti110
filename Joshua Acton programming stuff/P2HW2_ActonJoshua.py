#Joshua Acton
 #02/27/2025
 #P2HW2
 #The program should store the grades entered in a list.

mod1 =float(input("Enter grade for module 1: "))
mod2 =float(input("Enter grade for module 2: "))
mod3 =float(input("Enter grade for module 3: "))
mod4 =float(input("Enter grade for module 4: "))
mod5 =float(input("Enter grade for module 5: "))
mod6 =float(input("Enter grade for module 6: "))
gradelist = []
gradelist = [mod1, mod2, mod3, mod4, mod5, mod6]

#Lowest, highest, sum and the length
lowest = min(gradelist)
highest = max(gradelist)
total = sum(gradelist)
average = total / len(gradelist)

#print the results
print("\n----------Results----------")
print(f'{"Lowest Grade: ":<20}{lowest}')
print(f'{"Highest Grade : ":<20}{highest}')
print(f'{"Sum of Grades : ":<20}{total}')
print(f'{"Average: ":<20}{average:.2f}')
print('-'*30)

