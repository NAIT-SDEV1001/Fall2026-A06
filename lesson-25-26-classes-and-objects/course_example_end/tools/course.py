from tools.student import Student
from tools.assignment import Assignment


class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []
        self.assignments = []

    def __str__(self) -> str:
        return f"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def add_assignment(self, assignment: Assignment) -> None:
        self.assignments.append(assignment)

    def get_student(self, student_id: int) -> Student | None:
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_assignment(self, assignment_id: int) -> Assignment | None:
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                return assignment
        return None

    def get_course_average(self) -> float:
        total = 0
        number_of_submissions = 0
        for student in self.students:
            for submission in student.submissions:
                total += submission.grade
                number_of_submissions += 1
        return total / number_of_submissions
