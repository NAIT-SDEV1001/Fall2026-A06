def calculate_sum_of_squares(square):
    total = 0

    for number in range(int(square)):
        total += (number+1) ** 2

    return total