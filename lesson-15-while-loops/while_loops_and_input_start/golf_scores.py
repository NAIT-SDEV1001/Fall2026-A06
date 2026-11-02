print("Golf Score Calculator")
count = 0
total_score = 0

while True:
    try:
        user_input = input("What was your most recent golf score? (enter 'quit' to stop) ")
        
        if user_input == 'quit': # quit if the user enters 'quit'
            break
        else: # add the score to the total and increment the count
            total_score += int(user_input)
            count += 1
    except ValueError as e:
        print(f"Please enter a valid number or 'quit' to stop ({e})")

# only calculate the average if we have at least one score

try:
    average = total_score / count
    print(f"Your average golf score is {average}.")
except ZeroDivisionError:
    print("No scores entered.")
