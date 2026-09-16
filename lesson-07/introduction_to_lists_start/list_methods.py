groceries = ['lettuce', 'tomatoes', 'bread', 'milk', 'chicken', 'apples']

print("Our grocery list is: ")
print(groceries)

print("Last item:", groceries[-1])

print("First item:")
print(groceries[0])

print("Third item:")
print(groceries[2])

print(len(groceries))

index = 6

if index < len(groceries):
    print(groceries[index])
else:
    print("Index was out of range:", index)

item = 2

groceries[2] = item

item = 'hotdog buns'

groceries[2] = item

print(groceries[2])

print(item)

my_number = 10
my_string = "Hello"
my_other_number = 5

my_number = my_other_number
print(my_number)

my_other_number = 400
print(my_number)

my_number = my_other_number
print(my_number)

print(groceries[-3:])