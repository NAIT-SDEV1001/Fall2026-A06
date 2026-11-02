class Student:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.submissions = []

    def __str__(self) -> str:
        return f"{self.name}"

    # `submission: "Submission"` is a forward reference — we don't import
    # Submission here because Submission imports Student, which would create
    # a circular import.
    def add_submission(self, submission: "Submission") -> None:
        self.submissions.append(submission)
