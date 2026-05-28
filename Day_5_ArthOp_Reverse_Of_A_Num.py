# Reverse of a two digit number
"""original_number = 45
print(f"Original Number: {original_number}")
first_number = original_number % 10 
print(f"First Number: {first_number}")
shifted_number = first_number * 10
print(f"Shifted Number: {shifted_number}")
last_number= original_number// 10
print(f"Last Number: {last_number}")
reversed_number = shifted_number + last_number
print(f"Reversed Number: {reversed_number}")"""

# Reverse of a 3-digit number

original_number = int(input("Enter a random number: "))  # 123

# Extract last digit
last_digit = original_number % 10
print(f"Last Digit: {last_digit}")  # 3

# Remove last digit
remaining_number_after_last_digit = original_number // 10
print(f"Remaining Number After Last Digit: {remaining_number_after_last_digit}")  # 12

# Shift last digit to tens place
shifted_last_digit = last_digit * 10
print(f"Shifted Last Digit: {shifted_last_digit}")  # 30

# Extract middle digit
middle_digit = remaining_number_after_last_digit % 10
print(f"Middle Digit: {middle_digit}")  # 2

# Remove middle digit
remaining_number_after_middle_digit = remaining_number_after_last_digit // 10
print(f"Remaining Number After Middle Digit: {remaining_number_after_middle_digit}")  # 1

# Build partial reversed number
partial_reversed_number = (shifted_last_digit + middle_digit) * 10
print(f"Partial Reversed Number: {partial_reversed_number}")  # 320

# Extract first digit
first_digit = remaining_number_after_middle_digit % 10
print(f"First Digit: {first_digit}")  # 1

# Final reversed number
reversed_number = partial_reversed_number + first_digit
print(f"Reversed Number: {reversed_number}")  # 321