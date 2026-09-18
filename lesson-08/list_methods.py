number_list = [1, 9, 2, 34, 50, 11, 13, 66, 1000]

length = len(number_list)

# print(number_list)

# Sorting a list
number_list.sort()

# print(number_list)

# Reverse order
number_list.sort(reverse=True)

# print(number_list)

number_list.append(999)

# print(number_list)

number_list.insert(0,777)

# print(number_list)

removed_item = number_list.pop(3)

# print(number_list)
# print(removed_item)

class_list = ["SDEV", "ITBA", "DMIT"]
print(class_list)

course_code = "ITBA"

if course_code in class_list:
    class_list.remove(course_code)

# if "ITBA" in class_list:
#     class_list.remove("ITBA")

print(class_list)
# len(class_list) returns a number, the count of items in the list
popped_course_code = class_list.pop(0)

print(popped_course_code)
print(class_list)

class_list.append("DMIT")
class_list.append("DMIT")

print(class_list)

class_list.remove("DMIT")

print(class_list)

class_list.clear()

print(class_list)



