class Student:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.submissions = []

    def __str__(self) -> str:
        return self.name

    def add_submission(self, submission: "Submission") -> None:
        self.submissions.append(submission)