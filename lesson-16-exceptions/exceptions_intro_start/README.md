# Exception Introduction

## Why is this important?

Exceptions are a way to handle errors in your code. You're probably familiar with errors in your code because they happen all the time.

You've probably seen errors like `NameError`, `TypeError`, `ValueError`, `SyntaxError`, etc. These are all examples of exceptions. Exceptions are a way to handle errors in your code so that your program doesn't crash.

Many times we don't want to crash our program when an error occurs. We want to handle the error and move on.

We're going to use `try except` blocks to handle exceptions in our code, so that we can handle the error and move on.

## What are we going to do?

We're going to take a look at the edge cases of our golf score calculator and handle the errors that occur.


### 1. Let's make `golf_scores.py` crash and observe the error.
- Enter "sixty-two" as the first score and let's see what the output is going to be.
```
$ python golf_scores.py
Golf Score Calculator
What was your most recent golf score? (enter 'quit' to stop) sixty-two
Traceback (most recent call last):
  File "C:\Users\dmouris\sdev1001-master-course\looping-and-exceptions\exceptions_intro_start\golf_scores.py", line 11, in <module>
    total_score += int(user_input)
                   ^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'sixty-two'
```
- You can see that we get a `ValueError` because we're trying to convert the string "sixty-two" to an integer. This is not possible because "sixty-two" is not a number.
  - We can also see that this is happening on `line 11` of our code where we're trying to convert the user input to an integer.


### 2. Let's handle this error so that our program doesn't crash.
- We're going to add a `try except` block around the code that is causing the error on `line 11`.
- Let's take a look at the code.
```python
print("Golf Score Calculator")
count = 0
total_score = 0

while True:
    user_input = input("What was your most recent golf score? (enter 'quit' to stop) ")
    if user_input == 'quit': # quit if the user enters 'quit'
        break
    else: # add the score to the total and increment the count
        try:
            total_score += int(user_input)
            count += 1
        except ValueError as error_message:
            print(F"Could not convert input to a number. {error_message}")

# only calculate the average if we have at least one score

if count > 0:
    average = total_score / count
    print(f"Your average golf score is {average}.")
else:
    print("No scores entered.")
```
- You can see here that we're using a `try except` block to handle the `ValueError` that is occurring on `line 11`.
  - We're also printing out the error message so that we can see what the error is.
  - When using `try except` blocks you can also use the `as` keyword to assign the error message to a variable. In this case we're assigning the error message to a variable named `error_message`.
- You want to keep the code that's inside of the `try` block as small as possible. This is because you want to only handle the error that is occurring in that block of code.
  - In this case we're only handling the error that is occurring on `line 11` of our code.

- Let's take a look at the output of our program below.
```output
$ python golf_scores.py
Golf Score Calculator
What was your most recent golf score? (enter 'quit' to stop) sixty-two
Could not convert input to a number. invalid literal for int() with base 10: 'sixty-two'
What was your most recent golf score? (enter 'quit' to stop) 87
What was your most recent golf score? (enter 'quit' to stop) 38
What was your most recent golf score? (enter 'quit' to stop) something else
Could not convert input to a number. invalid literal for int() with base 10: 'something else'
What was your most recent golf score? (enter 'quit' to stop) 76
What was your most recent golf score? (enter 'quit' to stop) 99
What was your most recent golf score? (enter 'quit' to stop) quit
Your average golf score is 75.0.
```
- You can see now that even though we entered "sixty-two" and "something else" our program didn't crash. It handled the error and moved on.
- You may have also noticed the `if count > 0` check at the bottom of the code. This prevents a `ZeroDivisionError` when the user quits without entering any scores. While this approach works, using `try/except` is a more consistent way to handle errors in Python. In Step 3, we'll replace it with a `try/except` block.

### 3. Let's replace the `if/else` guard with a `try/except` block.
- The `if count > 0` check works, but let's look at the error it's preventing and replace it with a `try/except` for consistency. Here's what the error looks like without the guard:
```
$ python golf_scores.py
Golf Score Calculator
What was your most recent golf score? (enter 'quit' to stop) quit
Traceback (most recent call last):
  File "C:\Users\dmouris\sdev1001-master-course\looping-and-exceptions\exceptions_intro_start\golf_scores.py", line 19, in <module>
    average = total_score / count
              ~~~~~~~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```
- You can see that we get a `ZeroDivisionError` because we're trying to divide by zero. This is because we didn't put any scores in so our `count` variable is still 0.
- This should not make our program crash! Let's add a `try except` block around this code handling the `ZeroDivisionError`.
```python
# other code removed for brevity

try:
    average = total_score / count
    print(f"Your average golf score is {average}.")
except ZeroDivisionError:
    print("You didn't enter any scores!")
```
- You can see that we're handling the `ZeroDivisionError` that is occurring on `line 19` of our code. Notice that we're not using an error message here because we already know exactly what went wrong.

- Let's take a look at the output of our program now.
```
$ python golf_scores.py
Golf Score Calculator
What was your most recent golf score? (enter 'quit' to stop)
Could not convert input to a number. invalid literal for int() with base 10: ''
What was your most recent golf score? (enter 'quit' to stop) quit
You didn't enter any scores!
```
- Great! You can see that we didn't enter a score properly the first time and handled the `ValueError` and notified the user. Then we quit without entering a score and we handled the `ZeroDivisionError` as well.

### 4. Using `else` and `finally`

There are two more blocks you can use with `try` and `except`:
- `else` runs only if no exception was raised in the `try` block.
- `finally` always runs, regardless of whether an exception occurred.

Note: it's best to avoid `else` and `finally` unless you have a specific reason to use them — they can make your code harder to read. The examples below are for illustration only and won't be added to our golf score program.

Here's an example using `else` to confirm a score was recorded:
```python
try:
    total_score += int(user_input)
    count += 1
except ValueError as error_message:
    print(f"Could not convert input to a number. {error_message}")
else:
    print("Score recorded!")
```

Here's an example using `finally` to always print a closing message, even if there's an error:
```python
try:
    average = total_score / count
    print(f"Your average golf score is {average}.")
except ZeroDivisionError:
    print("You didn't enter any scores!")
finally:
    print("Thanks for using the golf score calculator!")
```

### 5. Raising Exceptions

Sometimes you want to signal that something is wrong from inside your own code. You can do this with the `raise` keyword. This is useful when you want to enforce rules about what values are acceptable.

The example below is for illustration only and won't be added to our golf score program.

A golf score should always be a positive number. We can write a function that raises a `ValueError` if the score is invalid:
```python
def validate_score(score):
    if score < 1:
        raise ValueError("Golf score must be a positive number!")
    return score

try:
    score = validate_score(int(user_input))
    total_score += score
    count += 1
except ValueError as error_message:
    print(f"Invalid score: {error_message}")
```
- If the user enters `0` or a negative number, `validate_score` raises a `ValueError` with a clear message. The `except` block catches it just like any other `ValueError`.

## Best Practices

- Keep the code inside `try` blocks as small as possible.
- Handle only the exceptions you expect.
- Inform the user about what went wrong.
- Use specific exception types (like `ValueError`, `ZeroDivisionError`) instead of a general `Exception` when possible.

## Conclusion

Handling exceptions is a tool that you can use to make your programs more robust. You can handle exceptions so that your program doesn't crash and you can notify the user of what's going on.

This is a technique that you'll use often when trying to connect or interface with some external system. We'll learn more about this in the future.