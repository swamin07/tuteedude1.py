# Step 1: Create the dictionary of student marks
student_marks = {
    "Swamin": 88,
    "Aarav": 76,
    "Priya": 91,
    "Neha": 85,
    "Rohan": 79
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show message if not found
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print(f"Student named '{name}' not found in the record.")
