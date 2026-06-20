"""print("--- Reversing a string ---")
name = input("Enter a random word: ").lower()
reversed_text = name[::-1]
if reversed_text == name:
    print(f"{name} is Palindrome")
else:
    print(f"{name} isn't a Palindrome")"""

'''print("--- Reversing a string using While loop ---")
name = input("Enter a random name: ").lower()
length_name = len(name)
print(f"Length of {name}: {length_name}")
index = len(name) - 1
original_name = name
reversed_name = ""
while index >= 0:
    reversed_name += name[index]
    index -= 1

print(f"The reversed name is {reversed_name}")
if reversed_name == original_name:
    print("Its a Palindrome")
else:
    print("It's not a Palindrome")'''

'''name = input("Enter a text: ")
print(len(name))
character_finding = int(input("Enter the index to find that character: "))
print(name[character_finding])
start_index = int(input("From which index position the characters to be found: "))
end_index = int(input("Upto which index position the characters to be found: "))
print(name[start_index:end_index])
print(len(name[start_index:end_index]))

name = input("Enter a text: ")
print(len(name))
character_finding = int(input("Enter the index to find that character: "))
print(name[character_finding])
print(name[2:])
print(name[:len(name)-1])
print(name[:len(name) - 3 ])
print(name[-len(name): - 3])
print(name[-len(name):])

step_count = int(input("Enter the step value: "))

print(name[0:len(name):step_count])'''

name = input("Enter a sentence: ")
original_name = name
print(f"Original name: {original_name}")
length_name = len(name)
print(f"Length: {length_name}")
reversed_name =""
index = length_name -1
print(f"Index: {index}")
while index > -1:
    reversed_name += name[index]
    index -= 1
print(f"Reversed name: {reversed_name}")
