# User Input Example

In this example, we'll be using the `input()` function to get user input from the command line. A function is piece of code that performs a specific operation. Sometimes we need to provide information to the function (known as 'passing a value') and sometimes the function gives us information back (known as 'returning a value'). We will be covering functions in more detail later in the course.

__Input__ is any information (also known as 'data') that a user provides to a software program. It can be any type of data, such as numbers or plain text. For example: a username, a menu option, or a payment amount. The are all different types of __input__.

## Why is this important?

Earlier we wrote a program that just displayed some output. This is great, but most programs need to get input from the user. This is where the `input()` function comes in.

In the future, we'll speak of different ways to get user input, like in a web application, but for now, we'll just focus on getting input from the terminal (also known as the 'command line').

## Steps

### 1. Open your terminal to this example (or where you'll be keeping your notes.)

### 2. Open the the "Python Interpreter" by typing `python` in the terminal and pressing enter.

### 3. Type `input("What is your name? ")` in the python intepreter and press enter. Let's break down the output.
```
>>> input("What is your name? ")
What is your name? Daniel
'Daniel'
>>>
```
- `input()` allows us to 'pass' a value, which is what we are asking the user to enter (known as the 'prompt').
- Here you see the first line after pressing enter is the prompt `What is your name? `. On that line after the `What is your name? `you see the user input `Daniel`, this is what was typed.
- Below the line `What is your name? Daniel` you see the output `'Daniel'`. The single quotes around the output are there to show that it's a 'string'. This is what is 'returned' from the `input()` function.
- A 'string' is a type of data that represents plain text and the `input()` function always returns a string. There are several data types that we will be using in future lessons.

### 4. Let's use a variable to store the output of the `input()` function. Type `name = input("What is your name? ")` and press enter. You should see something like this:
- A 'variable' is a programming concept that allows us to give names to values. Whenever we want to use the value that the variable represents, we simply use the variable instead.
- The value that is 'stored' inside of a variable can change, but the name we give the variable cannot.
- Think of a variable like a box with a name on it. We can put whatever we want inside of the box, but it always has the same name. If we want what is inside of that box, 
```
>>> name = input("What is your name? ")
What is your name? Daniel
```
- Now you have a variable called `name` that contains the user input. Congratulations you've assigned a variable! 
- You haven't used it anywhere yet so let's do that now.
```
>>> name = input("What is your name? ")
What is your name? Daniel
>>> print(name)
Daniel
```
Congrats you've used a variable! Note that variables can be called anything you want, but it's best to use descriptive names. For example, `name` is a good variable name because it describes what it is. `x` is a bad variable name because it doesn't describe what it is.

### 5. Let's move this code into a file. Type `exit()` in the Python interpreter and press enter and let's create that file!
- In your terminal navigate to the right directory (you can also use the terminal in vs code to do this.)
- create a file in that directory called `user_input_example.py` and open it in VS Code.
- Type the following code into the file:
```python
name = input("What is your name? ")
print("hi there")
print(name)
```
- Note you can see here that we're mixing what you've learned in the previous example and this example in our code. This is great! You're learning how to use multiple concepts together to create a program.

### 6. Run the program by typing `python user_input_example.py` in the terminal and pressing enter. You should see something like this:
```
$ python user_input_example.py
What is your name? Daniel
hi there
Daniel
```
- Note that the program is waiting for you to enter your name. Once you do, it will print out `hi there` and then your name.

### 7. Let's use our variable in the string using something called an f-string. Change the code in `user_input_example.py` to the following:
```python
name = input("What is your name? ")
print(f"hi there {name}")
```
What this is doing is using the `f` in front of the string to tell Python that we want to use a variable in the string. The variable is surrounded by curly braces `{}`. This is called an f-string.

And the output once you run your program should be:
```
$ python user_input_example.py
What is your name? Steve
hi there Steve
```

## Conclusion

User input is essential for most programs because you want something unique to happen based on what the user enters.

We'll be using this quite a bit in the future so make sure you understand it well.
