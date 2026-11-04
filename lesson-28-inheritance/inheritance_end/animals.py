class Animal:
    def __init__(self, name: str, color: str, num_legs: int) -> None:
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def eat(self) -> None:
        print(f"{self.name} starts eating. Nom nom nom...")

    def make_a_noise(self) -> None:
        print(f"{self.name} makes an interesting noise.")

    def move(self) -> None:
        print(f"{self.name} runs around!")

    def __str__(self) -> str:
        return f"Name: {self.name}\nColor: {self.color}\nNumber of Legs: {self.num_legs}"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, color={self.color}, num_legs={self.num_legs})"

class Dog(Animal):
    def __init__(self, name: str, color: str, num_legs: int, breed: str) -> None:
        super().__init__(name, color, num_legs)
        self.breed = breed

    def __str__(self) -> str:
        super_string = super().__str__()
        super_string += f"\nBreed: {self.breed}"
        return super_string

    def make_a_noise(self) -> None:
        print(f"{self.name} starts barking loudly! Bark Bark!")

    def chase_car(self) -> None:
        print(f"{self.name} chases after a Honda Civic!")

class Cat(Animal):
    pass

class Bird(Animal):
    pass