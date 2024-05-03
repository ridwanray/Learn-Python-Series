# def user_factory(permission:str):

#     def user():
#         user_info = {
#             "name":"ridwanray",
#             "age": 10,
#             "permission": permission
#         }
#         return user_info
#     return user
# import functools

# def greeting_decorator(func):

#     def wrapper(passed_name):
#         """Greeting Decorator Doc"""
#         name = func(passed_name)
#         decorated_name = f"Hi, {name}"
#         return decorated_name
#     return wrapper

# # decorated_greeting = greeting_decorator(greet)
# # print(decorated_greeting("Ray"))

# # print(greet("RAY"))
#                         # Multiple Decorators(Chaining Decorators)
# # @decorato2 
# # @decorator1
# # def ordinary_function():
# #    pass

# def prefix_decorator(func):

#     @functools.wraps(func)
#     def wrapper(passed_name):
#         """Prefix Decorator Doc"""
#         name = func(passed_name)
#         prefixed_name = f"Mr. {name}"
#         return prefixed_name
#     return wrapper


# # @greeting_decorator
# @prefix_decorator
# def greet(name:str):
#     """Greets a user incorrectly"""
#     return name

# # # print(greet("Ray"))
# # decorated_greeting = greeting_decorator(prefix_decorator(greet))
# # print(decorated_greeting("Ray"))
# print(greet.__name__)
# print(greet.__doc__)
                            # Class as a decorator
# def greet(name:str):
# 	return name

# def greet_decorator(func):

# 	def wrapper():
# 		name = func()
# 		decorated_name = f"Hi, {name}"
# 		return decorated_name
		
# 	return wrapper
# greet_decorator = "abc"


class GreetDecorator:
	def __init__(self, func):
		self.func = func
		
	def __call__(self, name:str):
		returned_value = self.func(name)
		return f"Hi, {returned_value}"


# decorated_greeting = GreetDecorator(greet)
# print(decorated_greeting("ridwanray"))
@GreetDecorator
def greet(name:str):
	return name
print(greet("Ray"))