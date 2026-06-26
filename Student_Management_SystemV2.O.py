# Constants
subject_max_marks = 100
subject_min_marks = 0
subject_pass_marks = 35
total_max_marks = 600

# Student Information
student_name = ""
student_roll_number = ""
student_class = ""
student_section = ""

# First Language
fl_marks = 0
fl_grade = ""
fl_grade_point = 0

# Second Language
sl_marks = 0
sl_grade = ""
sl_grade_point = 0

# English
english_marks = 0
english_grade = ""
english_grade_point = 0

# Mathematics
math_marks = 0
math_grade = ""
math_grade_point = 0

# Science
science_marks = 0
science_grade = ""
science_grade_point = 0

# Social Studies
social_marks = 0
social_grade = ""
social_grade_point = 0

# Final Calculated Values
total_marks = 0
percentage = 0.0
overall_grade = ""
overall_grade_point = 0.0
performance_status = ""
result = ""

while True:
    print("====================================================")
    print("        Student Management System V2.0              ")
    print("====================================================")
    print("Menu")
    print("1. Enter the Student Information")
    print("2. Generate Report Card")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Choice. \nPlease Enter only digits.")
        continue
    if choice == 1:
        print("===================================================")
        print("              STUDENT INFORMATION                  ")
        print("===================================================")
        student_name = input("Enter Student Name: ")
        student_roll_number = input("Enter Student Roll Number: ")
        student_class = input("Enter Student's class: ")
        student_section = input("Enter Student's section: ")
        print("===================================================")
        print("                SUBJECT MARKS                      ")
        print("===================================================")
        try:
            fl_marks = int(input("Enter the FL marks: "))
        except ValueError:
            print("Enter only digits")
            continue
        if fl_marks > subject_max_marks or fl_marks < subject_min_marks:
            print("Invalid Marks. \nEnter marks between 0 and 100")
        else: 
            if fl_marks >= 90:
                fl_grade = "A1"
                fl_grade_point = 10

            elif fl_marks >= 80:
                fl_grade = "A2"
                fl_grade_point = 9

            elif fl_marks >= 70:
                fl_grade = "B1"
                fl_grade_point = 8

            elif fl_marks >= 60:
                fl_grade = "B2"
                fl_grade_point = 7

            elif fl_marks >= 50:
                fl_grade = "C1"
                fl_grade_point = 6

            elif fl_marks >= 40:
                fl_grade = "C2"
                fl_grade_point = 5

            elif fl_marks >= subject_pass_marks:
                fl_grade = "D"
                fl_grade_point = 4

            else:
                fl_grade = "E"
                fl_grade_point = 0
        
        try:
            sl_marks = int(input("Enter the SL marks: "))
        except ValueError:
            print("Enter only digits")
            continue
        if sl_marks > subject_max_marks or sl_marks < subject_min_marks:
            print("Invalid Marks. \nEnter marks between 0 and 100")
        else: 
            if sl_marks >= 90:
                sl_grade = "A1"
                sl_grade_point = 10

            elif sl_marks >= 80:
                sl_grade = "A2"
                sl_grade_point = 9

            elif sl_marks >= 70:
                sl_grade = "B1"
                sl_grade_point = 8

            elif sl_marks >= 60:
                sl_grade = "B2"
                sl_grade_point = 7

            elif sl_marks >= 50:
                sl_grade = "C1"
                sl_grade_point = 6

            elif sl_marks >= 40:
                sl_grade = "C2"
                sl_grade_point = 5

            elif sl_marks >= subject_pass_marks:
                sl_grade = "D"
                sl_grade_point = 4

            else:
                sl_grade = "E"
                sl_grade_point = 0
        try:
            english_marks = int(input("Enter the English marks: "))
        except ValueError:
            print("Enter only digits")
            continue
        if english_marks > subject_max_marks or english_marks < subject_min_marks:
            print("Invalid Marks. \nEnter marks between 0 and 100")
        else: 
            if english_marks >= 90:
                english_grade = "A1"
                english_grade_point = 10

            elif english_marks >= 80:
                english_grade = "A2"
                english_grade_point = 9

            elif english_marks >= 70:
                english_grade = "B1"
                english_grade_point = 8

            elif english_marks >= 60:
                english_grade = "B2"
                english_grade_point = 7

            elif english_marks >= 50:
                english_grade = "C1"
                english_grade_point = 6

            elif english_marks >= 40:
                english_grade = "C2"
                english_grade_point = 5

            elif english_marks >= subject_pass_marks:
                english_grade = "D"
                english_grade_point = 4

            else:
                english_grade = "E"
                english_grade_point = 0
        try:
            math_marks = int(input("Enter the Mathematics marks: "))
        except ValueError:
            print("Enter only digits")
            continue
        if math_marks > subject_max_marks or math_marks < subject_min_marks:
            print("Invalid Marks. \nEnter marks between 0 and 100")
        else: 
            if math_marks >= 90:
                math_grade = "A1"
                math_grade_point = 10

            elif math_marks >= 80:
                math_grade = "A2"
                math_grade_point = 9

            elif math_marks >= 70:
                math_grade = "B1"
                math_grade_point = 8

            elif math_marks >= 60:
                math_grade = "B2"
                math_grade_point = 7

            elif math_marks >= 50:
                math_grade = "C1"
                math_grade_point = 6

            elif math_marks >= 40:
                math_grade = "C2"
                math_grade_point = 5

            elif math_marks >= subject_pass_marks:
                math_grade = "D"
                math_grade_point = 4

            else:
                math_grade = "E"
                math_grade_point = 0 
        try:
            science_marks = int(input("Enter the Science marks: "))
        except ValueError:
            print("Enter only digits")
            continue
        if science_marks > subject_max_marks or science_marks < subject_min_marks:
            print("Invalid Marks. \nEnter marks between 0 and 100")
        else: 
            if science_marks >= 90:
                science_grade = "A1"
                science_grade_point = 10

            elif science_marks >= 80:
                science_grade = "A2"
                science_grade_point = 9

            elif science_marks >= 70:
                science_grade = "B1"
                science_grade_point = 8

            elif science_marks >= 60:
                science_grade = "B2"
                science_grade_point = 7

            elif science_marks >= 50:
                science_grade = "C1"
                science_grade_point = 6

            elif science_marks >= 40:
                science_grade = "C2"
                science_grade_point = 5

            elif science_marks >= subject_pass_marks:
                science_grade = "D"
                science_grade_point = 4

            else:
                science_grade = "E"
                science_grade_point = 0
        try:
            social_marks = int(input("Enter the Social marks: "))
        except ValueError:
            print("Enter only digits")
            continue
        if social_marks > subject_max_marks or social_marks < subject_min_marks:
            print("Invalid Marks. \nEnter marks between 0 and 100")
        else: 
            if social_marks >= 90:
                social_grade = "A1"
                social_grade_point = 10

            elif social_marks >= 80:
                social_grade = "A2"
                social_grade_point = 9

            elif social_marks >= 70:
                social_grade = "B1"
                social_grade_point = 8

            elif social_marks >= 60:
                social_grade = "B2"
                social_grade_point = 7

            elif social_marks >= 50:
                social_grade = "C1"
                social_grade_point = 6

            elif social_marks >= 40:
                social_grade = "C2"
                social_grade_point = 5

            elif social_marks >= subject_pass_marks:
                social_grade = "D"
                social_grade_point = 4

            else:
                social_grade = "E"
                social_grade_point = 0

        total_marks = fl_marks + sl_marks + english_marks + math_marks + science_marks + social_marks
        percentage = (total_marks / total_max_marks) * 100
        overall_grade_point = (fl_grade_point + sl_grade_point + english_grade_point + math_grade_point + science_grade_point + social_grade_point) / 6
        if overall_grade_point >= 9.2:
            overall_grade = "A1"
            performance_status = "Outstanding"
        elif overall_grade_point >= 8.2:    
            overall_grade = "A2"
            performance_status = "Excellent"
        elif overall_grade_point >= 7.2:    
            overall_grade = "B1"
            performance_status = "Very Good"
        elif overall_grade_point >= 6.2:
            overall_grade = "B2"
            performance_status = "Good"
        elif overall_grade_point >= 5.2:
            overall_grade = "C1"  
            performance_status = "Average"
        elif overall_grade_point >= 4.2:
            overall_grade = "C2"
            performance_status = "Below Average"
        elif overall_grade_point >= 3.5:
            overall_grade = "D"
            performance_status = "Marginal/Pass"
        else:
            overall_grade = "E"
            performance_status = "Needs Improvement/Fail"
        if(fl_marks >= subject_pass_marks and sl_marks >= subject_pass_marks and english_marks >= subject_pass_marks and math_marks >= subject_pass_marks and science_marks >= subject_pass_marks and social_marks >= subject_pass_marks):
            result = "PASS"
        else:
            result = "FAIL"  
    elif choice == 2:
        if student_name == "":
            print("Please Enter Student Information First")
        else:
            print("===================================================")
            print("              Student Report Card                  ")
            print("===================================================")
            print(f"{'Name':<25}:  {student_name}")
            print(f"{'Roll Number':<25}:  {student_roll_number}")
            print(f"{'Class':<25}:  {student_class}")
            print(f"{'Section':<25}:  {student_section}")
            print("=========================================================================")
            print(f"{'Subject':<30}{'Marks':<10}{'Grade':<10}{'Grade Point'}")
            print("==========================================================================")
            #Formatted String Alignment: {variable:<width}
            print(f"{'First Language':<30}{fl_marks:<10}{fl_grade:<10}{fl_grade_point}")
            print(f"{'Second Language':<30}{sl_marks:<10}{sl_grade:<10}{sl_grade_point}")
            print(f"{'English':<30}{english_marks:<10}{english_grade:<10}{english_grade_point}")
            print(f"{'Mathematics':<30}{math_marks:<10}{math_grade:<10}{math_grade_point}")
            print(f"{'Science':<30}{science_marks:<10}{science_grade:<10}{science_grade_point}")
            print(f"{'Social Studies':<30}{social_marks:<10}{social_grade:<10}{social_grade_point}")
            print("==========================================================================")
            print(f"{'Total Marks':<25}: {total_marks}/{total_max_marks}")
            print(f"{'Percentage':<25}: {percentage:.2f}%")
            print(f"{'Overall GPA':<25}: {overall_grade_point:.2f}")
            print(f"{'Overall Grade':<25}: {overall_grade}")
            print(f"{'Performance Status':<25}: {performance_status}")
            print(f"{'Result':<25}: {result}")
            print("==========================================================================")
    elif choice == 3:
        print("Thank you for using Student Management System")
        break
    else:
        print("Invalid Choice.")    