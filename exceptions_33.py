# # # numbers = [1, 2, 3]

# # # # for num in numbers:
# # # #     print("hi")
# # # return "Hi"
# # # try-except
# # # x = 20
# # # y = 0
# # # try:
# # #     print(f"{x} divided by {y} is {x/y}")
# # # except Exception as e:
# # #     print("Error:", e)

# # # print("The end")
# # # try-except-else
# # # x = 20
# # # y = 0

# # # try:
# # #      result = x/y

# # # except ZeroDivisionError:
# # #      print("You cannot divide by zero")

# # # else:
# # #      print(f"{x} divided by {y} is {result}")
# # # try-except-finally
# # from io import UnsupportedOperation

# # file = open("test.txt")

# # try:
# #     file.write("New Line")
# # except UnsupportedOperation:
# #     print("From Exception: File closed ?:", file.closed)
# # finally:
# #     file.close()
# #     print("From Finally: File closed ?:", file.closed)
# # raise
# x = 20
# y = 0

# if y == 0:
#     raise ValueError("Division by zero not allowed")

# print(x/y)
# Multiple Exceptions
# x = 10
# y = "10"

# try:
#     # some code that may raise exceptions
#     result = x / y
# except ZeroDivisionError as e:
#     print(f"Division by zero error: {e}")
# except TypeError as e:
#     print(f"Type error: {e}")
# else:
#     print(f"Result is {result}")

# Multiple Exceptions with Tuple
x = 10
y = "0"

try:
    result = x / y

except (ZeroDivisionError, TypeError) as e:
    print("Error:", e)

else:
    print(f"Result is {result}")





























