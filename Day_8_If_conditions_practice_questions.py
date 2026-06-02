'''print("----- Admission Program-----")
student_name = input("Enter your name: ")
student_percentage = int(input("Enter your percentage: "))
if student_percentage >= 35:
    print(f"{student_name} has passed")
    if student_percentage >= 60:
        print(f"{student_name} got admission")
    else:
        print(f"{student_name}'s Admission Denied")
else:
    print(f"{student_name} is Not Eligible for Admission")'''

'''print("----- Employee Bonus System -----")
employee_status = input("Is employee working in this company (yes/no)? ").lower()
if employee_status in ("yes", "y"):
    employee_experience = int(input("Years of experience: "))
    if employee_experience  >= 5:
        print("Bonus granted")
    else:
        print("No Bonus granted")
else:
    print("Employee Not Eligible")'''

'''print("-----ATM Card -PIN verification-----")
card_status = input("Is the card inserted (yes or no): ").lower()
if card_status in ("yes", "y"):
    card_pin= int(input("Enter your card pin: "))
    if card_pin == 1234:
        print("Access granted")
    else:
        print("Invalid PIN")
else:
    print("Insert Card First")'''

'''print("----- Company's Employee Rating System -----")

employee_name = input("Enter employee's name: ")
employee_status = input(f"Is {employee_name} active (Yes/No): ").lower()

if employee_status in ("yes", "y"):
    employee_rating = int(input(f"What is {employee_name}'s rating: "))
    print(f"{employee_name} is active")
    if employee_rating >= 9:
        print("Outstanding")
    elif employee_rating >= 7:
        print("Excellent")
    elif employee_rating >= 5:
        print("Good")
    else:
        print("Needs improvemt")
else:
    print(f"{employee_name} is not active")'''

print("----- Student's Marks Report")

student_name = input("Enter the student name: ")
total_subjects = int(input("Enter the number of subjects: "))
fl_marks = int(input("Enter the FL marks: "))

if fl_marks >= 91:
    fl_grade_points = 10
    fl_grade = "A1"
    print(f"FL grade points: {fl_grade_points}, grade: {fl_grade}")
elif fl_marks >= 81:
    fl_grade_points = 9
    fl_grade = "A2"
    print(f"FL grade points: {fl_grade_points}, grade: {fl_grade}")
elif fl_marks >= 71:
    fl_grade_points = 8
    fl_grade = "B1"
    print(f"FL grade points: {fl_grade_points}, grade: {fl_grade}")
elif fl_marks >= 61:
    fl_grade_points = 7
    fl_grade = "B2"
    print(f"FL grade points: {fl_grade_points}, grade: {fl_grade}")
elif fl_marks >= 51:
    fl_grade_points = 6
    fl_grade = "C1"
    print(f"FL grade points: {fl_grade_points}, grade: {fl_grade}")
elif fl_marks >= 41:
    fl_grade_points = 5
    fl_grade = "C2"
    print(f"FL grade points: {fl_grade_points}, grade: {fl_grade}")
elif fl_marks >= 35:
    fl_grade_points = 4
    fl_grade = "D"
    print(f"FL grade points: {fl_grade_points}, grade: {fl_grade}") 
else:
    fl_grade_points = 0
    fl_grade = "E"
    print(f"FL grade points: {fl_grade_points}, grade: {fl_grade}") 
       
sl_marks = int(input("Enter the SL marks: "))
if sl_marks >= 90:
    sl_grade_points = 10
    sl_grade = "A1"
    print(f"SL grade points: {sl_grade_points}, grade: {sl_grade}")
elif sl_marks >= 79:
    sl_grade_points = 9
    sl_grade = "A2"
    print(f"SL grade points: {sl_grade_points}, grade: {sl_grade}")
elif fl_marks >= 68:
    sl_grade_points  = 8
    sl_grade = "B1"
    print(f"SL grade points: {sl_grade_points}, grade: {sl_grade}")
elif sl_marks >= 57:
    sl_grade_points = 7
    sl_grade = "B2"
    print(f"SL grade points: {sl_grade_points}, grade: {sl_grade}")
elif sl_marks >= 46:
    sl_grade_points = 6
    sl_grade = "C1"
    print(f"SL grade points: {sl_grade_points}, grade: {sl_grade}")
elif sl_marks >= 35:
    sl_grade_points = 5
    sl_grade = "C2"
    print(f"SL grade points: {sl_grade_points}, grade: {sl_grade}")
elif sl_marks >= 20:
    sl_grade_points = 4
    sl_grade = "D"
    print(f"SL grade points: {sl_grade_points}, grade: {sl_grade}") 
else:
    sl_grade_points = 0
    sl_grade = "E"
    print(f"SL grade points: {sl_grade_points}, grade: {sl_grade}")

english_marks = int(input("Enter the English marks: "))
if english_marks >= 91:
    english_grade_points = 10
    english_grade = "A1"
    print(f"English grade points: {english_grade_points}, grade: {english_grade}")
elif english_marks >= 81:
    english_grade_points = 9
    english_grade = "A2"
    print(f"English grade points: {english_grade_points}, grade: {english_grade}")
elif english_marks >= 71:
    english_grade_points = 8
    english_grade = "B1"
    print(f"English grade points: {english_grade_points}, grade: {english_grade}")
elif english_marks >= 61:
    english_grade_points = 7
    english_grade = "B2"
    print(f"English grade points: {english_grade_points}, grade: {english_grade}")
elif english_marks >= 51:
    english_grade_points = 6
    english_grade = "C1"
    print(f"English grade points: {english_grade_points}, grade: {english_grade}")
elif english_marks >= 41:
    english_grade_points = 5
    english_grade = "C2"
    print(f"English grade points: {english_grade_points}, grade: {english_grade}")
elif english_marks >= 35:
    english_grade_points = 4
    english_grade = "D"
    print(f"English grade points: {english_grade_points}, grade: {english_grade}") 
else:
    english_grade_points = 0
    english_grade = "E"
    print(f"English grade points: {english_grade_points}, grade: {english_grade}")

total_marks = fl_marks + sl_marks + english_marks

print(f"Total marks of {student_name}: {total_marks}")
total_grade_points = int((fl_grade_points + sl_grade_points + english_grade_points) / total_subjects)
print(f"Total grade points of {student_name}: {total_grade_points}")

maximum_marks = total_subjects * 100
percentage = int((total_marks/maximum_marks) * 100)
print(f"Percentage of {student_name}: {percentage}")
