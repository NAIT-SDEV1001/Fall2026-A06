class Vehicle:
    def __init__(self) -> None:
        self.logging_string = "It's a vehicle"

    def __str__(self) -> str:
        return self.logging_string

class Car(Vehicle):
    def __str__(self):
        return "It's a car"

my_vehicle = Vehicle()

print(my_vehicle)

my_car = Car()

print(my_car)