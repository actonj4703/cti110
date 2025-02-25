#Python's f-strings offer a concise way to embed expressions inside string literals for formatting. Alignment can be achieved using format specifiers within the curly braces {}. 
#Alignment Options 

#• Left alignment: < 
#• Right alignment: > 
#• Center alignment: ^ 

#Syntax 
#The general syntax for alignment within an f-string is: 

# f"{variable : {width}{alignment}}"

#• variable: The variable to be formatted. 
#• width: The total width of the field, including padding. 
#• alignment: The alignment character (<, >, or ^). 

#Examples 
name = "Alice"
age = 30

# Left alignment with width 10
print(f"{name:<10} is {age} years old.")
# Output: Alice      is 30 years old.

# Right alignment with width 10
print(f"{name:>10} is {age} years old.")
# Output:      Alice is 30 years old.

# Center alignment with width 10
print(f"{name:^10} is {age} years old.")
# Output:   Alice    is 30 years old.

# Fill with a character other than space
print(f"{name:*^10} is {age} years old.")
# Output: **Alice*** is 30 years old.

#Numeric alignment 
num = 123.456
print(f"{num:10.2f}") # Right-align, width 10, 2 decimal places
# Output:   123.46

print(f"{num:<10.2f}") # Left-align, width 10, 2 decimal places
# Output: 123.46   



