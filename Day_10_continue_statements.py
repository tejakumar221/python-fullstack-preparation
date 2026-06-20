"""print("----- Q.No.1 Print numbers from 1 to 10; skip 5 ----")
count = 1
while count <= 10:
    if count == 5:
        count += 1
        continue
    print(count, end = " ")
    count += 1
print()
print("---- Q.No.2 Print numbers from 2 to 20; skip 10 ----")
count = 2
while count <= 20:
    if count == 10:
        count += 1
        continue
    print(count, end = " ")
    count += 2
print()
print("---- Q.No.3 Print Numbers from 10 to 1 ----")
count = 10
while count >= 0:
    if count == 7:
        count -= 1
        continue
    print(count, end = " ")
    count -= 1
print()
print("---- Q.No.4 Print Numbers from 5 to 50; skip all multiples of 5 ----")
count = 5
while count <= 50:
    if count % 5 == 0:
        count += 1
        continue
    print(count, end = " ")
    count += 1
print()"""
print("---- Q.No.5 Ask the user to enter 5 number----")
count = 1
while count <= 5:
    number = int(input("Enter a number: "))
    if number == 0:
        count += 1
        continue
    print(f"You entered: {number}")
    count += 1
    print()

