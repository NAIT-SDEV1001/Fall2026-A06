# Import the class data using the data module.
from data.course_data import student_data, assignment_data, submission_data

from tools.course import Course
from tools.student import Student
from tools.assignment import Assignment
from tools.submission import Submission

def load_student_data(course: Course) -> None:
    # students = list[Student] = []

    # for student in student_data:
    #     new_student: Student = Student(student["id"], student["name"])
    #     students.append(new_student)

    # course.add_students(students)

    for student in student_data:
        new_student: Student = Student(student["id"], student["name"])
        course.add_student(new_student)

def load_assignment_data(course: Course) -> None:
    for assignment in assignment_data:
        new_assignment = Assignment(assignment["id"], assignment["name"])
        course.add_assignment(new_assignment)

def load_submission_data(course: Course) -> None:
    for submission in submission_data:
        # create new submission
        student = course.get_student(submission["student_id"])

        if student == None:
            print("Student not found trying to load submission.")
            continue
        
        assignment = course.get_assignment(submission["assignment_id"])
        new_submission = Submission(student, assignment, submission["grade"])
        
        student.add_submission(new_submission)


if __name__ == "__main__":
    course = Course("SDEV1001")

    # load data from file
    load_student_data(course)
    load_assignment_data(course)
    load_submission_data(course)
    
    print(course)