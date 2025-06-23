# Function to check grade based on score
def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Ask for number of students
num_students = int(input("Enter the number of students: "))

# Loop through each student
for i in range(num_students):
    name = input("Enter the student's name: ")
    score = int(input("Enter the student's score (0–100): "))
    grade = check_grade(score)
    print(f"{name}  the grade {grade}")