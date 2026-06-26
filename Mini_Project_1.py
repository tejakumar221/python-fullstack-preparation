max_marks = 100
min_marks = 0
pass_marks = 35
student_name = ""
student_roll_number = ""
student_marks = 0
grade = ""
result = ""
while True:
    print("==========================================")
    print("       STUDENT MANAGEMENT SYSTEM          ")
    print("==========================================")
    print("1. Enter Student Details ")
    print("2. Generate Report Card ")
    print("3. Exit ")
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid Choice.Please enter digits only")
        continue
    
    if choice == 1:
        print("==========================================")
        print("       STUDENT DETAILS         ")
        print("==========================================")
        student_name = input("Enter the student name: ")
        student_roll_number = input("Enter the student roll number: ")
        try:
            student_marks = int(input("Enter the marks: "))
        except:
            print("Invalid marks. Please enter digits only")
            continue
        if student_marks > max_marks or student_marks < min_marks:
            print("Invalid Marks. \nPlease enter marks between 0 and 100")
        else:
            if student_marks >= 90:
                grade = "A"
            elif student_marks >= 80:
                grade = "B"
            elif student_marks >= 70:
                grade = "C"
            elif student_marks >= 60:
                grade = "D"
            elif student_marks >= 35:
                grade = "E"
            else:
                grade = "F"
            if student_marks >= pass_marks:
                result = "PASS"
            else:
                result = "FAIL"
        
    elif choice == 2:
        if student_name == "":
            print("Please enter the student details first.")
        else:
            print("==========================================")
            print("       STUDENT REPORT CARD         ")
            print("==========================================")
            print(f"Student Name: {student_name}")
            print(f"Student Roll Number: {student_roll_number}")
            print(f"Student Marks: {student_marks}")
            print(f"Grade: {grade}")
            print(f"Result: {result}")
    elif choice == 3:
        print("Thank you for using Student Management System.")
        break
    else:
        print("Invalid Choice.")