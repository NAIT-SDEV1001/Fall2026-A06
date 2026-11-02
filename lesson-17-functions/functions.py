def say_hello():
    print("Hello!")

def power_of(a, b):
    return a ** b

# say_hello()
# power_of(10, 10)

def get_greeting(user_name):

    return f"Hello {user_name}"

greeting = get_greeting("Dominic")

print(greeting)


customers = ["A", "B", "C"]

def find_last_two_customers():
    return customers[-2:]

last_two_customers = find_last_two_customers()


print(len(find_last_two_customers()))