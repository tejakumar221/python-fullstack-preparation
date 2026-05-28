# Find first and last digit of a number

original_number = 7539

# Extract last digit
last_digit = original_number % 10
print(f"Last Digit: {last_digit}")

# Remove digits step-by-step
remaining_number_1 = original_number // 10
remaining_number_2 = remaining_number_1 // 10
remaining_number_3 = remaining_number_2 // 10

# Remaining single digit becomes first digit
first_digit = remaining_number_3

print(f"First Digit: {first_digit}")