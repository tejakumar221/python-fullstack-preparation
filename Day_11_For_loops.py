print("---- Q.No.1 Print Numbers from 1 to 50 ----")
for i in range (1, 51):
    print(i, end = " ")
print()
print("---- Q.No.2 Print Numbers from 50 to 1 ----")
for i in range (50, 0, -1):
    print(i, end = " ")   
print()
print("---- Q.No.3 Print even Numbers from 2 to 30 ----") 
for i in range (2, 31, 2):
    print(i, end = " ")
print()
print("---- Q.No.4 Print odd Numbers from 1 to 25 ----") 
for i in range (1, 26, 2):
    print(i, end = " ")
print()
print("---- Q.No.5 Multiples of a number ----")
number = int(input("Enter a number: ")) 
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
for i in range (start_number, end_number + 1):
    print(number * i, end = " ")   
print()     
print("---- Q.No.6 Sum of numbers ----") 
total = 0
for i in range (1, 6):
    total += i
print(total,  end = " ") 
print()
print("---- Q.No.6-B Sum of numbers ----") 
total = 0
start = int(input("Enter the starting value: "))
stop = int(input("Enter the ending value: "))
for i in range (start, stop + 1):
    total += i
print(total,  end = " ")    