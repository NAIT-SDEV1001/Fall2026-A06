# def add(*number_to_add):

#     result = 0

#     for number in number_to_add:
#         result += number

#     return result

# def list_properties(**properties_to_list):
#     # print(properties_to_list)
#     # print(type(properties_to_list))
#     print(properties_to_list["name"])
#     print(properties_to_list["job"])
#     print(properties_to_list["age"])


# list_properties(name="Dominic", job="Farmer", age=100, best_friend="Dominic")

def show_info(name, age):
    print(f"{name} is {age} years old.")
    
person = ("Alice", 30)
show_info(*person)

settings = {"name": "Bob", "age": 25}
show_info(**settings)