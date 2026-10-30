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

    def add_students(self, students: list[Student]) -> None:
        for student in students:
            self.add_student(student)

    def get_student(self, id: int) -> Student | None:
        for student in self.students:
            if student.id == id:
                return student

        return None
    
    def add_assignment(self, assignment: Assignment) -> None:
        self.assignments.append(assignment)

    def get_assignment(self, id: int) -> Assignment | None:
        for assignment in self.assignments:
            if assignment.id == id:
                return assignment

        return None

    def get_course_grade_min() -> int:
        pass

    def get_course_grade_max() -> int:
        pass

    def get_course_grade_average() -> float:
        pass