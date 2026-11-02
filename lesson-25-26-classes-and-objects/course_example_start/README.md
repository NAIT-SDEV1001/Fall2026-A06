# Classes and Objects

## Why is this important?

In the library example, you saw the basics of how to define a class, create objects from it, and add methods. Now we're going to take it further.

The approach we've been learning is called **Object-Oriented Programming (OOP)** — a way of organizing code by modeling real-world things as objects. The main benefits are:
- **Modularity** — breaking a complex problem into smaller, manageable pieces. Each class handles its own slice of the problem.
- **Encapsulation** — grouping data and the functions that operate on that data together.
- **Reusability** — once you've defined a class, you can create as many objects from it as you need, and you can reuse the class across different programs.
- **Abstraction** — hiding the details of how something works behind a simple interface.

In this lesson, you'll see OOP's real strength: **multiple classes working together**. We'll build an app where a `Course` holds `Student` objects, students hold `Submission` objects, and submissions reference `Assignment` objects. Objects can have *other objects* as attributes — that's where modeling things in code really starts to feel powerful.

## What are we going to do?

We're going to build an application that models a course. We'll have four classes:
- `Course` — the course itself, holding lists of students and assignments
- `Student` — a student enrolled in the course
- `Assignment` — an assignment in the course
- `Submission` — a student's submission for a specific assignment, with a grade

## Steps

1. Take a look at `data/course_data.py` and observe the data in that file. You can see here that we're going to be working with a list of dictionaries to create some objects.

2. Let's create a file called `tools/course.py`. This file will contain a class called `Course`. Add the following code to the file:

```python
class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []
        self.assignments = []

    def __str__(self) -> str:
        return f"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"

```
- Note: the attribute `students` will be of type `list[Student]` and the attribute `assignments` will be of type `list[Assignment]`. We'll be creating these in the next steps.


3. Let's create a file called `tools/student.py`. This file will contain a class called `Student`. Add the following code to the file:
```python
class Student:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.submissions = []

    def __str__(self) -> str:
        return f"{self.name}"
```
- Note: the attribute `submissions` will be of type `list[Submission]`.

4. Now let's create a file called `tools/assignment.py`. This file will contain a class called `Assignment`. Add the following code to the file:

```python
class Assignment:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"Assignment ID: {self.id}, Assignment Name: {self.name}"

    def __repr__(self) -> str:
        return f"Assignment(id={self.id}, name='{self.name}')"
```
- You've seen `__str__` already in the library example — it controls how an object looks when you `print()` it. `__repr__` is a related dunder method that controls the **"official" string representation** of an object, which is mainly useful for developers and debugging.
  - When you inspect an object in the Python shell, or call `repr(obj)`, Python uses `__repr__`.
  - If a class doesn't define `__str__`, `print()` will fall back to `__repr__`.
  - Best practice: `__repr__` should return a string that, if possible, could be used to *recreate the object*. Notice the example above looks almost like the constructor call you'd write yourself: `Assignment(id=1, name='...')`. That's intentional.
- A common convention is to define both: `__str__` for end-users, `__repr__` for developers.

5. Now let's create a submission class. This file will contain a class called `Submission`. Add the following code to the file:

```python
from tools.student import Student
from tools.assignment import Assignment


class Submission:
    def __init__(self, student: Student, assignment: Assignment, grade: int) -> None:
        self.student = student
        self.assignment = assignment
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.student.name} received {self.grade} on {self.assignment}"
```
- Notice the two imports at the top. Because we're using `Student` and `Assignment` in the type hints for `__init__`, we need to import those classes — type hints can only reference names that are in scope.

6. Let's use our classes to create some objects. In the `course_app.py` file add the following code:

```python
from data.course_data import student_data, assignment_data, submission_data

from tools.course import Course

if __name__ == "__main__":
    # Create course
    course = Course("Dans Basketball Mastery Course")
    # display the course information.
    print(course)
```
- now if you run the `course_app.py` file you should see the following output:
```
$ python course_app.py
Dans Basketball Mastery Course has 0 students and 0 assignments
```

7. Let's create the functionality to add students to the `Course` class and add those objects in the `course_app.py` file. Add the following code to the file.
- First, let's add the following method to the course class in `tools/course.py` file (note we also need to import `Student` at the top so we can use it in the type hint):
```python
from tools.student import Student


class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []
        self.assignments = []

    def __str__(self) -> str:
        return f"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"

    # new method to add students.
    def add_student(self, student: Student) -> None:
        self.students.append(student)
```

- Second, let's create an `add_student` method in the `course_app.py` file which will add student objects by the `Student` class to the course object. Add the following code to the `course_app.py` file:
```python
from data.course_data import student_data, assignment_data, submission_data

from tools.course import Course
from tools.student import Student

def add_students(course: Course) -> None:
    for student in student_data:
        student_instance = Student(student["id"], student["name"])
        course.add_student(student_instance)


if __name__ == "__main__":
    # Create course
    course = Course("Dans Basketball Mastery Course")

    # Add students to course
    add_students(course)

    # display course information
    print(course)
```
- Now you'll see that the course has 3 students, take a look at the output below:
```
$ python course_app.py
Dans Basketball Mastery Course has 3 students and 0 assignments
```

8. Let's create the functionality to add assignments to the `Course` class and add those objects in the `course_app.py` file. Add the following code to the file.
- First, let's add the following method to the course class in `tools/course.py` file (note the new `Assignment` import — same reason as before, we need it for the type hint):
```python
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

    # new method to add assignments.
    def add_assignment(self, assignment: Assignment) -> None:
        self.assignments.append(assignment)
```
- Second, let's create an `add_assignments` method in the `course_app.py` file which will add assignment objects by the `Assignment` class to the course object. Add the following code to the `course_app.py` file:
```python
# other imports.
from tools.assignment import Assignment

# ... previous add_students code ...

def add_assignments(course: Course) -> None:
    for assignment in assignment_data:
        assignment_instance = Assignment(assignment["id"], assignment["name"])
        course.add_assignment(assignment_instance)

# if __name__ == "__main__": ... previous code ...
```
- Now you'll see that the course has 3 students and 2 assignments, take a look at the output below:
```
$ python course_app.py
Dans Basketball Mastery Course has 3 students and 2 assignments
```

9. Let's create the functionality to add submissions to the `Course` class and add those objects in the `course_app.py` file. Add the following code to the file.
- First, let's create a couple of helper methods in `Course` class so that we can get students from the course and get assignments from the course.
```python
class Course:
    # ... other methods ...
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
```
- Recall from the library lesson that `Student | None` means this method returns either a `Student` object **or** `None`. We use this here because the loop might not find a matching student, in which case we fall through and return `None`. Same logic for `get_assignment`.
- Callers should remember to check for `None` before using the result, just like we did with `find_book` in the library lesson.

- Second, let's create a method in the `Student` class so that a student can have submissions.
```python
class Student:
    # ... other methods ...
    def add_submission(self, submission: "Submission") -> None:
        self.submissions.append(submission)
```
- Notice we wrote `submission: "Submission"` (in quotes) — the same forward-reference syntax we used for `__eq__` in the `Book` class, but here it's solving a **circular import** problem.
- **The problem:** we already added `from tools.student import Student` to `submission.py` so we could type-hint Submission's `__init__`. If we now added `from tools.submission import Submission` here in `student.py`, Python would need to load `submission.py` to satisfy the import — but `submission.py` is already in the middle of loading `student.py`. Neither file finishes loading, and Python raises an `ImportError`.
- **The fix:** by writing `"Submission"` as a string, we get the type hint without needing the import. Type checkers and editors know how to resolve the string; Python at runtime doesn't have to (remember, hints aren't enforced), so there's no circular import.
- This pattern — string forward references to break circular imports — is common any time two classes refer to each other in their type hints.

- Third, let's create a method on `add_submissions` method in the `course_app.py`. We'll be creating the `Submission` objects in this method and adding them to a "student instance".
```python
# ... other imports ...
from tools.submission import Submission

# ... other methods ...
def add_submissions(course: Course) -> None:
    for submission in submission_data:
        student = course.get_student(submission["student_id"])
        assignment = course.get_assignment(submission["assignment_id"])
        submission = Submission(student, assignment, submission["grade"])
        student.add_submission(submission)

if __name__ == "__main__":
    # Create course
    course = Course("Dans Basketball Mastery Course")

    # Add students to course
    add_students(course)

    # Add assignments to course
    add_assignments(course)

    # Add submissions to the course
    add_submissions(course)

    # display course information
    print(course)
```

- Once we have this add a `breakpoint()` to the `course_app.py` file right under the `print(course)` line. Run the file and you can actually see the relationship between the course, students, and submissions by writing `[submission.grade for submission in course.students[0].submissions]` in the debugger. Take a look at the output below.
```
$ python course_app.py
Dans Basketball Mastery Course has 3 students and 2 assignments
--Return--
> c:\users\dmouris\sdev1001-master-course\classes-and-objects\course_example_start\course_app.py(44)<module>()->None
-> breakpoint()
(Pdb) [submission.grade for submission in course.students[0].submissions]
[100, 90]
(Pdb)
```
- You can see that you can traverse the course object to get the students and then the submissions for each student using the attributes here.

10. Let's create a course average method on the `Course` class that will leverage traversing the students and submissions to get the average grade for the submission. - Add the following code to the `tools/course.py` file.
```python
class Course:
    # ... other methods ...

    def get_course_average(self) -> float:
        total = 0
        number_of_submissions = 0

        for student in self.students:
            for submission in student.submissions:
                total += submission.grade
                number_of_submissions += 1

        return total / number_of_submissions
```

- Let's add the following code to the `course_app.py` file to display the course average.
```python
# ... other imports ...

if __name__ == "__main__":
    # Create course
    course = Course("Dans Basketball Mastery Course")

    # ... adding students, assignments, and submissions ...
    # display course information
    print(course)

    # display course average
    print(F"Course average: {course.get_course_average()}")

```
