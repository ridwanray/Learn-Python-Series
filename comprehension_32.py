# numbers = [1, 2, 3, 4, 5, 4]

# result = []

# for num in numbers:
#     result.append(num * num)

# result = [num * num for num in numbers]
# print(result)
# new_list = [expression for member in iterable]

# [expression for member in iterable if condition]
# numbers = [1, 4, 5, 6, 8, 9, 4, 7]

# result = [num  for num in numbers]
# print(result)

# result = [true_expr if cond else false_expr for member in iterable]
# numbers = [1, 2, 3, 4]
# result = ["Yes" if num > 2 else "No" for num in numbers]
# print(result)
# set comprehension {}
# numbers = [1, 2, 3, 4, 5, 4]
# result = {num:num for num in numbers}
# print(type(result))

squares = (x**2 for x in range(10))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


















