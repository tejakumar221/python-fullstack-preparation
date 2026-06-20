print("----- Practice questions on while loop -----")
"""count = int(input("Enter the starting value: "))
cond = int(input("Enter the condition: "))
update = int(input("Enter the step increase value: "))
while count <= cond:
    print(count)
    count += update"""

'''start_value = int(input("Enter the start value: "))
end_value = 1
while start_value >= end_value:
    print(start_value)
    start_value -= 1'''

"""print("----- Counting the number of digits in the given number -----")
number = int(input("Enter a random number: "))

if number == 0:
    count = 1
else:    
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    
print(f"Count: {count}")"""

"""print("----- Sum of digits in a number -----")
number = int(input("Enter a random number: "))
sum_digits = 0
if number == 0:
    sum = 0
else:
    while number > 0:
        remainder = number % 10
        sum_digits += remainder
        number = number // 10
    
print(f"Sum: {sum_digits}")"""
    
"""print("----- Reversing a number -----")
number =int(input("Enter a random number: "))
print(f"Original Number: {number}")
reverse_of_number = 0
while number > 0:
    last_digit = number % 10
    reverse_of_number = (reverse_of_number * 10) + last_digit
    number = number // 10
print(f"Reversed_number: {reverse_of_number}") """    

"""print("---- Checking - Palindrome -----")
number = int(input("Enter a random number: "))
reverse_of_number = 0
original_number = number
while number > 0:
    last_digit = number % 10
    reverse_of_number = (reverse_of_number * 10) + last_digit
    number = number // 10
if (original_number == reverse_of_number):
    print(f"The number {original_number} is Palindrome")
else:
    print(f"The number {original_number} is not Palindrome")"""

"""print("----- Armstrong Number Check -----")
number = int(input("Enter a random number: "))
original_number = number
print(f"Original number: {original_number}")

armstrong_number = 0
count = 0
count_number = number

print("Finding the number of digits in the given number")
while count_number > 0:
    count_number = count_number // 10
    count += 1
print(f"Count: {count}")
print(f"Number: {number}")

while number > 0:
    last_digit = number % 10
    armstrong_number = (last_digit ** count) + armstrong_number
    number = number // 10

print(f"Armstrong Number: {armstrong_number}")
if (original_number == armstrong_number):
    print(f"{original_number} is an Armstrong Number")
else:
    print(f"{original_number} is not an Armstrong Number")"""

print("--- Count, Reverse, Palindrome, Armstrong ---")

number = int(input("Enter a random number: "))

original_number = count_number = number
print(f"Original number: {original_number}")
reversed_number = armstrong_number = count = 0

print("Finding the number of digits")
while count_number > 0:
    count_number = count_number // 10
    count += 1
print(f"Number of digits in {number}: {count}")

while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    armstrong_number = (last_digit ** count) + armstrong_number
    number = number // 10

print(f"Reversed Number: {reversed_number}")
print(f"Armstrong Number: {armstrong_number}")

if original_number == reversed_number:
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")

if original_number == armstrong_number:
    print("Its an Armstong Number")
else:
    print("Its not an Armstrong Number")