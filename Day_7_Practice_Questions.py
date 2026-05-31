'''print("-----Using MemberShip Operator-----")
name_1 = input("Enter a random name: ")
character_1 = input("Enter a random character: ")
print(character_1 in name_1)

sentence_1 = input("Enter a random sentence: ")
word_1 = input("Enter a random word: ")
print(word_1 in sentence_1)'''

'''print("----- Using Comparison Operator -----")
num_1 = int(input("Enter thr first number: "))
num_2 = int(input("Enter the second number: "))
print(f"First number is greater: {num_1 > num_2}")

marks = int(input("Enter the marks: "))
print(f"Perfect Score: {marks == 100}")'''

print("------ Logical Operators -----")
age = int(input("Enter the age: "))
print(f"Eligible: {(age >= 18 and age <= 60)}")

marks = int(input("Enter the marks: "))
print(f"Special category: {(marks >= 90 or marks <= 35)}")

print("----- Identity Operator -----")
list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1

print(list1 == list2)
print(list1 is list2)

print(list1 == list3)
print(list1 is list3)

name1 = "Python"
name2 = "Python"

print(name1 == name2) #True
print(name1 is name2) #True

print(id(name1))
print(id(name2))

name = input("Enter a name: ")
print(("a" in name) and ("e" in name))

password = input("Enter the password: ")
print(("@" in password) or ("#" in password))

number = int(input("Enter a random number: "))
print((number > 10) and (number < 100))

sentence = "Python Programming"
character = input("Enter a random character: ")
print(character in sentence)

fruits = ["Apple", "Mango", "Banana", "Orange"]
selection = input("Enter a fruit name: ")
print(selection in fruits)

employee_salary = int(input("Enter the salary: "))
print((employee_salary >= 30000) and (employee_salary <= 100000))

username = input("Enter the username: ")
print(username == "Teja")