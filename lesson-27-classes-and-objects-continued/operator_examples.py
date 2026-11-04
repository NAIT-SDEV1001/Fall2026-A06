class Museum:
    pass

class Artwork:
    
    def __init__(self, name: str, artist: str, price: float):
        self.name = name
        self.artist = artist
        self.price = price

    def __eq__(self, value):
        return self.name == value.name

    def __repr__(self):
        return f'Artwork("{self.name}", "{self.artist}", {self.price})'

    def __str__(self):
        return f"{self.name} by {self.artist}"

    def __lt__(self, other):
        return self.price < other

    def __gt__(self, other):
        return self.price > other



painting_a = Artwork("Sunset", "Picasso", 0.00)
painting_b = Artwork("Sunset", "Picasso", 100000.00)

print(-painting_a)