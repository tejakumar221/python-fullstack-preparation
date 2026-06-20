"""print("---- Printing 1 to 5 using while True ----")
count = 1
while True:
    print(count, end = " ")
    if count == 5:
        break
    count += 1
print()
print("---- Printing 5 to 1 using while True ----")
count = 5
while True:
    print(count, end = " ")
    if count == 1:
        break
    count -= 1
print()
print("--- Ask the user to enter a word repeatedly, if the use enters 'exit', terminate the loop ----")
while True:
    word = input("Enter a word: ")
    print(f"You entered: {word}")
    if word == "exit":
        break
print()
print("----  Even or Odd Checker ----")
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    elif number % 2 == 0:
        print(f"The entered number {number} is even")
    else:
        print(f"The entered number {number} is odd")
print()
print("---- Password Verification ----")
count = 1
correct_password = "python123"
while True:    
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access Granted")
        break
    print("Wrong password")
    if count == 5:
        print("Exceeded the given count")
        break    
    count += 1       """
print("--- ATM Menu ----")
while True:
    print("\n----- ATM MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        print("Deposit selected")
    elif choice == 2:
        print("Withdraw Selected")
        pin = int(input("Enter the pin number:"))
        if pin == 1234:
            print("Access Granted")
        else:
            print("Enter the correct pin")
    elif choice == 3:
        print("Check Balance is selected")
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice \nPlease Try Again")