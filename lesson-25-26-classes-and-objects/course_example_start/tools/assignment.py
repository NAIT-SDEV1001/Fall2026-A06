class Assignment:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    def __repr__(self):
        return f"Assignment(id={self.id}, name='{self.name}')"
