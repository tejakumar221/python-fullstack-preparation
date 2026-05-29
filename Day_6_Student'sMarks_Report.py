print("Student's Marks Report")

student_name = input("Enter the student name: ")
total_number_of_subjects = int(input("Enter the total number of subjects: "))
fl_marks = int(input("Enter FL marks: "))
sl_marks = int(input("Enter SL marks: "))
tl_marks = int(input("Enter TL marks: "))
maths_marks = int(input("Enter Maths marks: "))
science_marks = int(input("Enter Science marks: "))
social_studies_marks = int(input("Enter Social marks: "))

bonus_marks = int(input("Enter the bonus marks: "))

tl_marks += bonus_marks
sl_marks += bonus_marks

maximum_marks = total_number_of_subjects * 100
total_marks_obtained = fl_marks + sl_marks + tl_marks + maths_marks + science_marks + social_studies_marks
print(f"Total marks obained by { student_name}: {total_marks_obtained}")
percentage = (total_marks_obtained / maximum_marks) * 100
print(f"Percentage obtained by { student_name}: {percentage}")


