# Joshua Acton
 # 02/25/2025
 # P2LAB2
 # how to write code that uses a dictionary to store user input and displays output to the user


#create dictionary
cars={
    "Camaro":18.21,
    "Prius":52.36,
    "Model S":110,
    "Silverado":26
    }
# Display Results of all keys in dictionary

keys=cars.keys()
print(keys)
print()

car_input=input("Enter a vechicle to see it's mpg: ")
print()
mpg_output=cars[car_input]
#Display Output
print(f"The {car_input} gets {mpg_output}mpg.\n")




