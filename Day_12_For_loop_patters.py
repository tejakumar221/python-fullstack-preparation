start_range = int(input("Enter the starting value: "))
end_range = int(input("Enter the ending value: "))
"""for i in range (start_range, end_range):
    for j in range (start_range, end_range):
        print ("*", end = " ")
    print()
print()
print("---------------------------------------------")    
for i in range (start_range, end_range):
    for j in range( start_range, end_range):
        print(i, end = " ")
    print()
print()
print("---------------------------------------------")    
for i in range (start_range, end_range):
    for j in range (start_range, end_range):
        print(j, end = " ")
    print()
print()
print("---------------------------------------------")
print()
for i in range (start_range, end_range):
    for j in range (start_range, i + 1):
        print(i, end = " ")
    print()
print()
print("---------------------------------------------")
for i in range (start_range, end_range):
    for j in range (start_range, i + 1):
        print(j, end = " ") 
    print()     """
"""number = 1
for i in range(start_range, end_range):
    for j in range (1, i + 1):
        print(number, end = " ")
        number += 1
    print()"""

"""alphabet = 65
for i in range (start_range, end_range):
    for j in range (1, i + 1):
        print(chr(alphabet), end = " ")
        alphabet += 1
    print()"""

for i in range (start_range, 0, -1):
    for j in range (1, i + 1):
        print(i, end = " ")
    print()    
for i in range (start_range, 0, -1):
    for j in range (1, i + 1):
        print(j, end = " ")
    print()     
number = 1
for i in range (start_range, end_range, -1):
    for j in range(1, i + 1):
        print(number, end = " ")
        number += 1
    print()
alphabet = 65
for i in range (start_range, end_range, -1):
    for j in range (1, i + 1):
        print(chr(alphabet), end = " ")
        alphabet += 1
    print()