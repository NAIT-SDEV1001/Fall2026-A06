import random

user_guess = input("Guess! heads or tails? (h/t)")

print(user_guess)

random_number = random.randint(0, 1) # inclusive

if random_number == 0:
    print("The coin flip was: heads")
elif random_number == 1:
    print("The coin flip was: tails")


if (random_number == 0 and user_guess == "h") or (random_number == 1 and user_guess == "t"):
    print("you guessed correct!")
else:
    print("you guessed wrong!")