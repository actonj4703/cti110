num_count = int(input("Enter the number of values to add: "))
total = 0
for i in range(num_count):
    num = float(input("Enter a number: "))
    total = num + total
print("Total", total)
