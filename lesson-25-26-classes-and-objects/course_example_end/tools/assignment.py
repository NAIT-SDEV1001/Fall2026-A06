class Assignment:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"Assignment ID: {self.id}, Assignment Name: {self.name}"

    def __repr__(self) -> str:
        return f"Assignment(id={self.id}, name='{self.name}')"