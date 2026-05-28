# Sum of digits of a 3-digit number
original_number = 753
#original_number = int(input("Enter a number: "))
first_remainder = original_number % 10 # 3
second_number = original_number // 10 # 75
second_remainder = second_number % 10 # 5
third_number = second_number //10 #7
third_remainder = third_number % 10 #
sum_of_digits = first_remainder + second_remainder + third_remainder
print(f"Sum of digits: {sum_of_digits}")