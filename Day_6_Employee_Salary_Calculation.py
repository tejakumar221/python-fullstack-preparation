print("Employee Salary Calculation")

employee_name = input("Enter the name of the employee: ")
employee_salary = int(input("Enter the salary of the employee: "))
bonus = float(input("Enter the bonus:"))

print(f"Bonus: {bonus}%")
employee_salary += employee_salary * (bonus/100)
print(f"Employee's salary after bonus: {employee_salary}")

tax = float(input("Enter the tax: "))
print(f"Tax: {tax}%")
employee_salary -= employee_salary * (tax/100)

print(f"Employee's salary after tax deduction: {employee_salary}")

print(f"Final salary of {employee_name}: {employee_salary}")