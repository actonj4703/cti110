#Python dictionaries have several built-in methods that allow you to manipulate them efficiently. Here are some commonly used dictionary methods:

### 1. **`keys()`** - Returns a view of all keys in the dictionary

student = {"name": "Alice", "age": 22, "major": "Computer Science"}
print(student.keys())  # Output: dict_keys(['name', 'age', 'major'])


### 2. **`values()`** - Returns a view of all values in the dictionary

print(student.values())  # Output: dict_values(['Alice', 22, 'Computer Science'])


### 3. **`items()`** - Returns a view of all key-value pairs as tuples

print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 22), ('major', 'Computer Science')])


### 4. **`get(key, default)`** - Retrieves a value for a key, with an optional default value if the key is missing

print(student.get("name"))  # Output: Alice
print(student.get("GPA", "Not available"))  # Output: Not available


### 5. **`update()`** - Updates the dictionary with another dictionary or key-value pairs

student.update({"GPA": 3.8, "age": 23})
print(student)  # Output: {'name': 'Alice', 'age': 23, 'major': 'Computer Science', 'GPA': 3.8}

### 6. **`pop(key, default)`** - Removes a key and returns its value, or returns a default if key is missing

age = student.pop("age")
print(age)  # Output: 23
print(student)  # 'age' key is now removed


### 7. **`popitem()`** - Removes and returns the last key-value pair (useful for LIFO operations)

last_item = student.popitem()
print(last_item)  # Output: ('GPA', 3.8)
print(student)  # GPA key is removed


### 8. **`setdefault(key, default)`** - Returns the value of a key, setting it to default if it doesn't exist

student.setdefault("GPA", 4.0)  # If GPA doesn't exist, it will be set to 4.0
print(student)  


### 9. **`clear()`** - Removes all key-value pairs

student.clear()
print(student)  # Output: {}

