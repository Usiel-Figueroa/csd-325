# Usiel Figueroa
# November 26, 2024
# Module 8.2 Assignment: JSON
# CSD325 Advanced Python


import json

# Load the student.json file
try:
    with open('student.json', 'r') as file:
        students = json.load(file)
except FileNotFoundError:
    print("Error: The file 'student.json' was not found. Please check the file location.")
    exit()

# Function to print student details
def print_students(students_list):
    for student in students_list:
        print(f"{student['F_Name']}, {student['L_Name']}: ID = {student['Student_ID']}, Email = {student['Email']}")

# Notify user and print the original list
print("Original Student List:")
print_students(students)

# Append your data
new_student = {
    "F_Name": "Usiel",
    "L_Name": "Figueroa",
    "Student_ID": 46464,
    "Email": "ufigueroa@my365.belevue.edu."
}
students.append(new_student)

# Notify user and print the updated list
print("\nUpdated Student List:")
print_students(students)

# Save changes back to the JSON file
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file has been updated.")

