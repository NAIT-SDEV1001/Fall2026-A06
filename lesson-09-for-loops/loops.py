my_list = [1, 2, 3, 4, 5, 6]

for a_tuple in enumerate(my_list):
    print(a_tuple)
    # my_list[i] = my_list[i] + 1  # crashes because 

# # f string
# my_name = "Dominic"
# print(f"My name is {my_name}")


# # list declaration
# another_list = []
# my_first_tuple = ("Dominic", "Sabatier")
# not_a_tuple = ("Dominic")
# is_a_tuple = ("Dominic",)

# python tutorials
# https://www.w3schools.com/python/python_tuples.asp

for i, item in enumerate(my_list):
    print(f"[{i}]: {item}")

# no need for 1 here because range max is exclusive
for i in range(0, len(my_list)): 
    print(f"[{i}]: {my_list[i]}")

for i, value in enumerate(my_list):
    if i == 0:
        continue
    print(i)