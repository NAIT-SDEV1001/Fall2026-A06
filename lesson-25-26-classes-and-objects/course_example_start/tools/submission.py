from tools.student import Student
from tools.assignment import Assignment

class Submission:
    def __init__(self, student: Student, assignment: Assignment, grade: int):
        self.student = student
        self.assignment = assignment
        self.grade = grade

    def __str__(self):
        return f"{self.student} received {self.grade} on {self.assignment}"