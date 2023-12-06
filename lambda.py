# lambda parameter(s) : expression
# x = lambda : print("Hey, lambda")
# x()

# (lambda : print("Hey, lambda"))()

# x = lambda : print("Hey, lambda")
# x()
# def greet():
#     print("Hi")

# def say_hi(func):
#     func()

# say_hi(greet)

# lambda parameter(s) : expression
# greet = lambda name, age : print(f'name is {name} and age is {age}')
# greet("Ray", 9)

# # if elif else
# Arbitrary arguments
# summation = lambda *x : sum(x)
# print(summation(5, 7, 9))
# map(function, iterable)

# numbers = [1, 2, 3, 4, 5]
# def square(x):
#     return x*x

# result = map(square, numbers)
# result = map(lambda x : x * x, numbers)
# print(list(result))
# filter(function, iterable)
my_list = [1, 4, 5, 6, 8, 11, 3, 12]
result = filter(lambda x : x > 3, my_list)
print(list(result))

#Todo: logic for getting cur takska and logs
#invite a supervior into a project multiple accounts alabarise@gmail.com















































