print("---- Question Number.1 : Print Numbers from 1 to 10 in the same line ----")
first_number = 1
while first_number <= 10:
    print(first_number, end = " ")
    first_number += 1
print()
print("---- Question Number.2 : Print Numbers from 1 to 10 and Stop when number becomes 6 ----")
first_number = 1
while first_number <= 10:
    print(first_number, end = " -> ")
    if first_number == 6:
        break
    first_number += 1
print()
print("---- Question Number.3 : Print Even Numbers from 2 to 20 ----")
first_number = 2
while first_number <= 20:
    print(first_number, end = ", ")
    first_number += 2
