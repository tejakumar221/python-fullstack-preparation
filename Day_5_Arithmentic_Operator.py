import math as m
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print(f"Sum = {first_number + second_number}")
print(f"Difference = {first_number - second_number}")
print(f"Product = {first_number * second_number}")
print(f"Division = {first_number / second_number}")
print(f"Floor Division = {first_number // second_number}")
print(f"Remainder = {first_number % second_number}")

print(f"Square of the first number = {first_number **2}")
print(f"Cube of the second number: {second_number ** 3}")

print(f"Area of a square : {first_number ** 2}")
print(f"Area of a rectangle : {first_number * second_number}")

print(f"Perimeter of a square : {4 * first_number}")
print(f"Perimeter of a rectangle : {2 * (first_number+second_number)}")

print(f"Area of a circle : {m.pi * (first_number ** 2)}")
print(f"Area of a triangle: { (1/2) * (first_number * second_number)}")
print(f"Circumference of a circle: { 2 * m.pi * first_number} ")