

# an empty list, imagine this has our student data in it
my_students = []

# loop through students and check..
# if age >= 15 and grade == 10 and score >= 0.8:
#     print("Found a student")

# if age != 15:
#     print("Student is not 15.")

age = 15
grade = 1
score = 0.8

# true or false
if grade == 10 or (age == 15 and score < 0.8):
    print("Did we print this?")

match grade:
    case 9:
        print("grade is 9")
    case 10:
        print("grade is 10")
    case 11:
        print("grade is 11")
    case _:
        print("grade is not 9, 10 or 11, it's something else")






