print("Average age of students calculator")

# declare variables outside of the loop

total_age = 0
count = 0 

while True:
    age = input("Enter the age of a student or 'stop' to finish: ")

    if age == "stop":
        break
    else:
        total_age += int(age)
        count += 1


print(f"The average age of the students is {total_age/count}")
