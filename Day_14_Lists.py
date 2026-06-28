"""
Program Name : Even and Odd Number Analysis

Author : Batchu Manikanta Mounesh Teja

Date : 28-06-2026

Purpose :
This program accepts a list of integers from the user and displays:
1. Even numbers
2. Odd numbers
3. Count of even and odd numbers
4. Sorted even and odd lists
5. Largest and smallest numbers
6. Sum of even and odd numbers
"""
"""numbers = []
numbers.append(10)
numbers.extend([20, 25, 31, 35, 44, 52, 63, 24, 16])
print(numbers)
even_numbers = []
count_even_numbers = 0
odd_numbers = []
count_odd_numbers = 0
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        count_even_numbers += 1
        
    else:
        odd_numbers.append(num)
        count_odd_numbers += 1
        
sorted_even_numbers = sorted(even_numbers)
sorted_odd_numbers = sorted(odd_numbers)

sum_even_numbers = sum(even_numbers)
sum_odd_numbers = sum(odd_numbers)

largest_even_number = max(even_numbers)
largest_odd_number = max(odd_numbers)

smallest_even_number = min(even_numbers)
smallest_odd_number = min(odd_numbers)

print(f"The total numbers of even numbers in the list: {count_even_numbers}")
print(f"The total numbers of odd numbers in the list: {count_odd_numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print(f"Sorted Even Numbers: {sorted_even_numbers}")
print(f"Sorted Odd Numbers: {sorted_odd_numbers}")
print(f"Sum of even numbers: {sum_even_numbers}")
print(f"Sum of odd numbers: {sum_odd_numbers}")
print(f"The largest even number : {largest_even_number}")
print(f"The smallest even number : {smallest_even_number}")
print(f"The largest odd number : {largest_odd_number}")
print(f"The smallest odd number : {smallest_odd_number}")"""

"""list_elements = []
size = int(input("Enter the number of elements: "))
for i in range(size):
    list_element = int(input(f"Enter the element {i + 1}: "))
    list_elements.append(list_element)
print(list_elements)

even_numbers = []
odd_numbers = []

for j in list_elements: 
    if j % 2 == 0:
        even_numbers.append(j)
    else:
        odd_numbers.append(j)    
count_even_numbers = len(even_numbers)
count_odd_numbers = len(odd_numbers)
print(f"Count of even numbers: {count_even_numbers}")
print(f"Count of odd numbers: {count_odd_numbers}")

sorted_even_numbers = sorted(even_numbers)
sorted_odd_numbers = sorted(odd_numbers)
print(f"Sorted Even Numbers: {sorted_even_numbers}")
print(f"Sorted Odd Numbers: {sorted_odd_numbers}")

largest_even_number = max(even_numbers)
largest_odd_number = max(odd_numbers)
print(f"Largest even number: {largest_even_number}")
print(f"Largest odd number: {largest_odd_number}")

smallest_even_number = min(even_numbers)
smallest_odd_number = min(odd_numbers)
print(f"Smallest even number: {smallest_even_number}")
print(f"Smallest odd number: {smallest_odd_number}")

sum_even_number = sum(even_numbers)
sum_odd_number = sum(odd_numbers)
print(f"Sum of even numbers: {sum_even_number}")
print(f"Sum of odd numbers: {sum_odd_number}")"""

"""print("==================================================================================")
numbers = []
strings = []
size = int(input("Enter the number of values: "))
for i in range(size):
    value = input(f"Enter the {i + 1} value: ")
    if value.isdigit():
        numbers.append(int(value))
    elif value.isalpha():
        strings.append(value)
print(f"Numbers: {numbers}")
print(f"Count of Numbers: {len(numbers)}")
print(f"Strings: {strings}")
print(f"Count of strings: {len(strings)}")

sum_numbers = sum(numbers)
largest_number = max(numbers)
smallest_number = min(numbers)
sorted_numbers = sorted(numbers)
print(f"Sorted Numbers: {sorted_numbers}")
print(f"Largest Number: {largest_number}")
print(f"Smallest Number: {smallest_number}")
print(f"Sum of Numbers: {sum_numbers}")
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")
print(f"Count of even numbers: {len(even_numbers)}")
print(f"Count of odd numbers: {len(odd_numbers)}")
print(f"Sum of Even Numbers: {sum(even_numbers)}")
print(f"Sum of Odd Numbers: {sum(odd_numbers)}")
print(f"Largest even number: {max(even_numbers)}")
print(f"Largest odd number:{max(odd_numbers)}")
print(f"Smallest even number: {min(even_numbers)}")
print(f"Smallest odd number: {min(odd_numbers)}")
print(f"Sorted Even Numbers: {sorted(even_numbers)}")
print(f"Sorted Odd Numbers: {sorted(odd_numbers)}")
print("==================================================================================")"""

numbers = []
alphabets = []
alphanumeric = []
others = []

size = int(input("How many elements do you want? "))
for i in range(size):
    value = input(f"Enter the value {i + 1}: ")
    if value.isdigit():
        numbers.append(int(value))
    elif value.isalpha():
        alphabets.append(value)
    elif value.isalnum():
        alphanumeric.append(value)
    else:
        others.append(value)
print(f"Numbers: {numbers}")
print(f"Total Numbers: {len(numbers)}")
print(f"Sum of Numbers: {sum(numbers)}")
print(f"Sorted Numbers: {sorted(numbers)}")
print(f"Largest of Numbers: {max(numbers)}")
print(f"Smallest of Numbers: {min(numbers)}")
print(f"Alphabets: {alphabets}")
print(f"Total Alphabets: {len(alphabets)}")
print(f"Alphanumeric: {alphanumeric}")
print(f"Total AlphaNumeric: {len(alphanumeric)}")
print(f"Others: {others}")
print(f"Total Others: {len(others)}")