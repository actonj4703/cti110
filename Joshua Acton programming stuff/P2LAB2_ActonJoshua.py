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
#car_input=car_input.lower() 
print()
mpg_output=cars[car_input]
#Display Output
print(f"The {car_input} gets {mpg_output} mpg.\n")


# gets the distance in miles car will be driven
distance=float(input(f"How many miles will you drive the {car_input}? "))
print()

#calculate the gallons of gas needed

gallons_needed=distance/mpg_output

#output gallons of gas needed to drive the vehicle the given number of miles

print(f"{gallons_needed:2f} gallon(s) of gas are needed to the drive the {car_input} {distance:2f} miles. ")






