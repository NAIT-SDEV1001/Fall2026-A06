from tools.student import Student
from tools.assignment import Assignment


class Submission:
    def __init__(self, student: Student, assignment: Assignment, grade: int) -> None:
        self.student = student
        self.assignment = assignment
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.student.name} received {self.grade} on {self.assignment}"
