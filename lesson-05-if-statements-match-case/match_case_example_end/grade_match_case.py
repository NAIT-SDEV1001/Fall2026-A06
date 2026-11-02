# Get user grade
letter_grade = input("Enter your letter grade (e.g. A, B+, C-): ")

# Convert letter grade to uppercase
letter_grade = letter_grade.upper()

# Convert letter grade to number
match letter_grade:
    case "A+" | "A" | "A-":
        gpa = 4.0
    case "B+" | "B" | "B-":
        gpa = 3.3
    case "C+" | "C" | "C-":
        gpa = 2.5
    case "D":
        gpa = 2.0
    case "F":
        gpa = 1.0
    case _:
        print("could not determine numeric grade")
        gpa = 0.0

# Print numeric grade
print(f"Your GPA is {gpa}")