"""print("----- Conditional Statement -----")
'''name = input("Enter a name: ")
if name:
    print("Name Entered Successfully")
else:    
    print("No name entered")

list_1 = []
if list_1:
    print("List Contains Data")
else:
    print("List contains No data")'''
    
password = input("Enter your password: ")
if password:
    print("Password Entered")  
else:
    print("Password Missing")

num_1 = int(input("Enter a random number: "))
if num_1 > 0:
    print("Positive")  
else:
    print("Negative")    

if num_1 % 2 == 0:
    print("Even")
else:
    print("Odd")

age = int(input("Enter your age: "))
if age >= 18:       
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

marks = int(input("Enter the marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")    """

print("--- Grade Calculator ---")
marks = int(input("Enter the marks: "))
if marks > 100 or marks < 0:
    print("InValid Marks")
if marks < 0 or marks > 100:
    print("Invalid Marks")

elif marks >= 90:
    print("A")

elif marks >= 80:
    print("B")

elif marks >= 70:
    print("C")

elif marks >= 60:
    print("D")

else:
    print("F")

print("--- Age Category ---")
age = int(input("Enter the age of a child: "))
if age <0:
    print("Invalid Age") 
elif age <= 12 :
    print("Child")
elif age <= 19:
    print("Teenager")
elif age<= 59:
    print("Adult")
else:
    print("Senior Citizen")

print("--- Largest of three numbers ---")
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

if num_1 == num_2 == num_3:
    print("All numbers are equal")
elif num_1 >= num_2 and num_1 >= num_3:
    print("num_1 is greatest")
elif num_2 >= num_1 and num_2>= num_3:
    print("num_2 is greatest")
else:
    print("num_3 is greatest")    

ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character")
    
if 'A' <= ch <= 'Z':
    print("Uppercase")
elif 'a'<= ch <= 'z':
    print("Lowercase")
elif '0'<= ch <= '9':
    print("Digit")
else:
    print("Special Character")