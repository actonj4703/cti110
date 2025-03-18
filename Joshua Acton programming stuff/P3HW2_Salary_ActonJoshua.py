# Joshua Acton
# 03/18/2025
# P3HW2
# Calculate  pay

name= input("Enter employee's name: ")
hours= float(input("Enter number of hours worked: "))
rate= float(input("Enter employee's pay rate: "))

if hours > 40:
    reg_pay = 40 * rate
    ovt_hrs = hours - 40
    ovt_pay = ovt_hrs * rate * 1.5
    gross_pay = ovt_pay + reg_pay

else:
    reg_pay = 40 * rate
    ovt_hrs = 0
    ovt_pay = 0
    gross_pay = ovt_pay + reg_pay

print("\n-------------------------------------")
print(f"{"Employee name:":<20} {name}")
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<15}{"OverTime":<15}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<15}')
print('-'*97)
print(f'{hours:<15.2f}{rate:<15.2f}{ovt_hrs:<15.2f}{ovt_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}')

