# def sum_list(numbers):
#    total = 0
#    for num in numbers:
#         total += num
#    return total
# print(sum_list([1, 2, 3, 4]))
# # תקלה שורה 4
#
# def concatenate_strings(str_list):
#     result = ""
#     for s in str_list:
#           result += s
#     return result
# print(concatenate_strings(["Hello", " ", "World!"]))
# # תקלה שורה 13

# def average_list(numbers):
#     total = sum(numbers)
#     return total / len(numbers)
#
# print(average_list([10, 20, 30, 40]))
# print(average_list([1]))
# תקלה שןרה 18 לא ניתן לחלק 0

# def to_upper_case(s):
#      return s.upper()
# print(to_upper_case("hello world"))
# # תקלה שורה 26 פונקציה שגויה


# def print_list_items(items):
#     for i in range(len(items)):
#         print(items[i])
# print_list_items([10, 20, 30, 40])
# print_list_items("12345")
# שןרה 34 אין len to int

# def swap_elements(lst, index1, index2):
#      lst[index1], lst[index2] = lst[index2], lst[index1]
#      return lst
# my_list = [10, 20, 30, 40]
# print(swap_elements(my_list, 1, 3))
# print(swap_elements(my_list, 1, 2))
# שגיאה שורה 44 index 2 לא בטווח

#
# def multiply_by_two(value):
#     value = value * 2
#     return value
# result = multiply_by_two(10)
# print(result)
# משתנה לא מוגדר

# def create_list(a,b):
#     return [i for i in range(a, 0, -1)]
#     return [i for i in range(a, 0, -1)]
# print(create_list(5,2))
# print(create_list(5, 2))
# פןנקציה שמתאימה רק למספר 1

#
# def add_to_list(lst, value):
#     lst.append(value)
#     return lst
# print(add_to_list([1, 2, 3], 4))
# פקודה שגוייה

# def search_index(lst, value):
#    try:
#        return lst.index(value)
#    except ValueError:
#         return "Value not found"
# def remove_value(lst, value):
#     if value in lst:
#        lst.remove(value)
#     return lst
# my_list = [1, 2, 3, 4, 5]
# print(search_index(my_list, 3))
# print(remove_value(my_list, 3))
# print(search_index(my_list, 3))
# בעית הזחה




