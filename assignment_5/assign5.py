# Assignment 5 - Student Result Checker

student_name = input("Enter Student Name: ")
score = int(input("Enter Score(between 0 and 100): "))

print("\n===== STUDENT RESULT =====")
print("Student Name:", student_name)
print("Score:", score)

if 70 <= score <= 100:
    print("Grade: A")
    print("Remark: Excellent")
    print("Bonus: Congratulations ")
elif 60 <= score <= 69:
    print("Grade: B")
    print("Remark: Very Good")
    print("Bonus: Congratulations ")
elif 50 <= score <= 59:
    print("Grade: C")
    print("Remark: Good")
    print("Bonus: Congratulations")
elif 45 <= score <= 49:
    print("Grade: D")
    print("Remark: Pass")
    print("Bonus: Better Luck Next Time")
elif 40 <= score <= 44:
    print("Grade: E")
    print("Remark: Pass")
    print("Bonus: Better Luck Next Time")
elif 0 <= score <= 39:
    print("Grade: F")
    print("Remark: Fail")
    print("Bonus: Better Luck Next Time")
else:
    print("Invalid score!.")
