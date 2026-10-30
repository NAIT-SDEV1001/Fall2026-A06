class Student:
    def __init__(self, id: int, name: str, submissions: list["Submission"] = []) -> None:
        self.id = id
        self.name = name
        self.submissions = submissions

    def __str__(self) -> str:
        return self.name

    def add_submission(self, submission: "Submission") -> None:
        self.submissions.append(submission)