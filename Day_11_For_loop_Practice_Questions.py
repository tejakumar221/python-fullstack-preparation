"""print("--- Multiplication Table ---")
number = int(input("Enter the number: "))
end_number = int(input("Enter the end number: "))
for i in range (1, end_number + 1):
    number_result = number * i
    print(f"{number} * {i} = {number_result}")

print()
print("--- Factorial of a given number ----")
number = int(input("Enter a number: "))
factorial_number = 1
for i in range (1,number + 1):
    factorial_number *= i
print(f"Factorial of {number} is {factorial_number}")

print("--- Sum of even numbers ---")
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
sum_even_number = 0
for i in range (start_number, end_number + 1):
    if i % 2 == 0:
        sum_even_number += i
print(f"Sum of even numbers is: {sum_even_number}")

print("--- Printing each character in a string ---")
user_word = input("Enter a word: ")
for character in user_word:
    print(character)

"""
"""print("--- Count of Vowels in the given the string ---")
word = input("Enter the word: ")
count_vowels = 0
for character in word:
    if character in "aeiouAEIOU":
        count_vowels += 1
print(f"The total number of vowels in {word} is {count_vowels}")"""

"""print("--- Count Upper Case and Lower Case letters in the given string ---")
word = input("Enter the text: ")
count_upper_case = 0
count_lower_case = 0
for character in word:
    if character.isupper():
        count_upper_case += 1
    elif charcater.islower():
        count_lower_case += 1
print(f"The total number of Upper case letters in {word}: {count_upper_case}")
print(f"The total number of lower case letters in {word}: {count_lower_case}")
print()"""

print("---- String Reverse and Palindrome Check----")
word = input("Enter the word: ")
original_word = word
print(f"The original word is: {original_word}")

reversed_word = ""
#for character in rane(len(word) -1, -1, -1):
    #reversed_word += word[character]
for character in word:
    reversed_word = character + reversed_word
print(f"Reversed_word is: {reversed_word}")
if original_word == reversed_word:
    print("It's Palindrome")
else:
    print("It's not Palindrome") 