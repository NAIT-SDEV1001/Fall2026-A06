# print("Enter numbers that add up to 10")

# sum = 0

# while sum != 10:
#     try:
#         user_input = input("Your number:")
#         valid_number = float(user_input)
#         sum += valid_number
        
#         print(sum)
#     except ValueError:
#         print("Invalid number entered")

# print("Job done")

import random
random_number = random.randint(1, 10)
guessed_number = 0

print("Guess a number between 1 and 10")

while guessed_number != random_number:
    try:
        user_input = input("Your number:")
        guessed_number = float(user_input)
        
    except ValueError:
        print("Invalid number entered")

print("Job done")