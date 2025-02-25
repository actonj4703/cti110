
# Creating a dictionary with some key-value pairs
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

# Accessing values using keys
print(f"Student Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Major: {student['major']}")

# Adding a new key-value pair
student["GPA"] = 3.8

# Updating a value
student["age"] = 23

# Removing a key-value pair
del student["major"]

# Accessing updated dictionary values
print(f"Updated Age: {student['age']}")
print(f"GPA: {student['GPA']}")

