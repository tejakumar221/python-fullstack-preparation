"""print("---- Multiplication Table ----")
number = int(input("Enter a number: "))
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
for i in range (start_number, end_number + 1):
    result = number * i
    print(f"{number} * {i} = {result}")

print("--- Print tables from 1 to N ---")
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
for i in range (start_number, end_number + 1):
    print(f"This is the table of {i}")
    for j in range (start_number, end_number + 1):
        result = i * j
        print(f"{i} * {j} = {result}")
    print()
"""
"""print("--- Q3-A: Generate and Sum the First N Multiples ---")
number = int(input("Enter a number: "))
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
sum_multiples = 0
for i in range (start_number, end_number + 1 ):
    result = number * i
    print(f"{result}", end = " ")
    sum_multiples += result
print()
print(f"Sum of the multiples of {number} is {sum_multiples}")

print("--- Q3-B: Find and Sum Multiples Within a Given Range ---")

number = int(input("Enter a number: "))
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

sum_multiples = 0

print(f"Multiples of {number}:")

for i in range(start_number, end_number + 1):
    if i % number == 0:
        print(i, end=" ")
        sum_multiples += i

print()
print(f"Sum of multiples of {number} is {sum_multiples}")"""

"""print("--- Count Factors of a Number ---")
number = int(input("Enter the number: "))
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
count = 0
for i in range (start_number, end_number + 1):
    if number % i == 0:
        print(i, end = " ")
        count += 1
print()
print(f"The total number of factors of {number}: {count} ")"""

"""print("--- Squares of a number in the given range ----")
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
for i in range (start_number, end_number + 1):
    result = i * i 
    print(f"The square of {i} = {result}")"""

"""print("--- Cubes of a number in the given range ----")
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
for i in range (start_number, end_number + 1):
    result = i * i * i
    print(f"The cubes of {i} = {result}")"""

"""print("--- Prime Number Check ---")
number = int(input("Enter the number: "))
if number == 1:
    print(f"The number {number} is neither Prime nor Composite")
else:
    count = 0
    for i in range (1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        print(f"The number {number} is Prime")
    else:
        print(f"The number {number} is Composite")"""

print("--- Finding Prime Numbers from a range ---")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
count_prime = 0
print(f"The prime numbers between {first_number} and {second_number} are: ", end = " ")
for i in range (first_number, second_number + 1):
    count = 0
    if i == 1:
        continue
    else:
        for j in range (1, i + 1):
            if i % j == 0:
                
                count += 1
               
    if count == 2:
        print(i, end = " ")
        count_prime += 1
print()        
print(f"\nThe total number of prime numbers are: {count_prime} " )
        
        
        
        