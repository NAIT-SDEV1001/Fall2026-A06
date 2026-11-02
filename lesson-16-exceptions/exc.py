user_id = "123"
date = "Today"

try:
    num = float(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print(f"That's not a valid number! {user_id}")
except ZeroDivisionError:
    print("You can't divide by zero!")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("An error may or may not have occured :)")


