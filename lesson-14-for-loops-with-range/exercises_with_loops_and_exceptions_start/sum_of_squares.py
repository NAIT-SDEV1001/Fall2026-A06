# get my_square from the user

my_square = input("Enter a number to sum the squares: ")

my_square = int(my_square)

# calculate sum of the squares

# create a list using the user input
numbers_to_square = range(my_square)

total = 0

# loop through the list, adding squares up as we go
for number in numbers_to_square:
    total += (number + 1) ** 2

# print out the result
print(f"The sum of squares is {total}")