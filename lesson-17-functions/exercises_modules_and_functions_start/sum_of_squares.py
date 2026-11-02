#from <file> import <function>
from squares_calculator import calculate_sum_of_squares

my_square = input("Enter a number to sum the squares: ")

total = calculate_sum_of_squares(my_square)

print(F"The sum of squares is {total}")
   