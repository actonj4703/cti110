# Joshua Acton
# 03/18/2025
# P3HW2
# Calculate  pay

name = input("Enter employee's name or \"Done\" to terminate: ")
overtime_total = 0.0
regPay_total = 0.0
gross_total = 0.0
Employee_count = 0
while name != "Done":
    Employee_count +=1
    hoursWorked = float(input("How many hours did "+name+" work? "))
    payRate = float(input("What is "+name+"'s pay rate? "))
    if hoursWorked >40 :
        reg_Pay = 40 * payRate
        ovt_hrs = hoursWorked - 40
        ovt_pay = ovt_hrs * payRate * 1.5
        gross_pay = ovt_pay + reg_Pay  
        gross_total += gross_pay
        
    
    
    
    else:
        reg_Pay = 40 * payRate
        ovt_hrs = 0
        ovt_pay = 0
        gross_pay = ovt_pay + reg_Pay
        gross_total += gross_pay




    print(f"{"Employee name:":<20} {name}")
    print(f'{"Hours Worked":<15}{"Pay Rate":<15}{"OverTime":<15}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<15}')
    print("\n------------------------------------------------------------------------------------------")
    print()
    print(f'{hoursWorked:<15.2f}{payRate:<15.2f}{ovt_hrs:<15.2f}{ovt_pay:<15.2f}{reg_Pay:<15.2f}{gross_pay:<15.2f}')
    name = input("Enter employee's name or \"Done\" to terminate: ")

print("\nTotal number of employee's entered: ", Employee_count, sep="")
print("Total amount paid for overtime: $", format(overtime_total,".2f"), sep="")
print("Total amount for regular hours: $", format(regPay_total,".2f"), sep="")
print("Total amount paid in gross: $", format(gross_total,".2f"), sep="")

