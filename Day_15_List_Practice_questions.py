print("--- List Practice Questions ---")
print("Q.No.1 Find Positive,Negative and Zero Numbers")
original_list = []
positive_numbers = []
negative_numbers = []
zero_numbers = []

size = int(input("Enter the number of elements: "))
for i in range(size):
    value = int(input(f"Enter the value {i + 1}:  "))
    original_list.append(value)
print(f"Original list: {original_list}")
for num in original_list:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    else:
        zero_numbers.append(num)
print(f"Positive Numbers: {positive_numbers}")
print(f"Negative Numbers: {negative_numbers}")
print(f"Zero Numbers: {zero_numbers}")

print(f"Count of Positive Numbers: {len(positive_numbers)}")
print(f"Count of Negative Numbers: {len(negative_numbers)}")
print(f"Count of Zero Numbers: {len(zero_numbers)}")