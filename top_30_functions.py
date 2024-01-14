# #enumerate(iterable)
# my_list = ["Orange", "Banana", "Apple"]

# # for index, item in enumerate(my_list, 1):
# #     print(f"{index}: {item}")
# for each in enumerate(my_list):
#     print(each)
# zip()
# first_names = ["Ali", "Ray", "Node", "Bill"]
# last_names = ["Kay", "Bob", "Lee"]

# # for each in zip(first_names,  last_names):
# #     print(each)
# for first, last in zip(first_names, last_names):
#     print(first,last)
# #all(iterable)

# my_list = [5, 7, 8, ""]
# print(all(my_list))
# def check_user_has_permissions(user, required_permissions):

#     """
#     Function to check if a user has any of the permissions required.
#     """
#     #required_permisions ["ViewUsers"]

#     user_permissions = get_user_permissions(user)
#     #["ViewTransaction", "DeleteTransaction"]

#     return any(user_perm in required_permissions for user_perm in user_permissions)
#     # any(True, False, True, )
# abs(x)
# var_1 = "-10"
# var_2 = 22.3

# print(abs(var_1))
# print(abs(var_2))

# class CustomObject:
#     def __abs__(self):
#         return 5
    
# instance = CustomObject()
# abs_value = abs(instance)
# print(abs_value)
# bool(x)

# x = 1
# y = [1]
# z = "o"

# print(bool(x))
# print(bool(y))
# print(bool(z))
# iter() and next()

# my_string = "ray"

# for each in my_string:
#     print(each)
# my_list = [1, 2, 3]
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator, None))
# class RangeIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         else:
#             # Return the current value and then increment it for next iteration
#             value = self.current 
#             self.current += 1
#             return value

# my_range = RangeIterator(2, 5)
# for num in my_range:
#     print(num)
# locals()

# my_list = ["A", "B", "C"] # global variable

# def sample_function():
#     local_var = 90 # local variable
#     print(locals())

# sample_function()

# # sorted(iterable)

# numbers = [9, 6, 2, 10]

# sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)
# reversed(iterable)

# numbers = "abc" #[9, 6, 2, 10]

# reversed_numbers = reversed(numbers)

# print(list(reversed_numbers))
# map(function, iterable)

# numbers = [1, 2, 3, 4, 5]

# def square(x):
#     return x*x

# result = map(square, numbers)

# print(list(result))
# filter
# # filter(function, iterable)
# my_list = [1, 4, 5, 6, 8, 11, 3, 12]

# def is_above_4(x):
#     return x > 4

# result = filter(is_above_4, my_list)

# print(list(result))
# open(filter, mode='r')
# my_courses =  ["Python", "FastAPI", "Django", "Deployment"]

# file_path = "courses2.txt"
# # file = open(file_path, "w")

# # for course in my_courses:
# #     file.write(course + "\n")

# # file.close()

# # with open(file_path, 'w') as file:
# #     for course in my_courses:
# #         file.write(course + '\n')

# with open(file_path, "r") as file:
#     for line in file:
#         print(line.rstrip())
        
# # print("File saved!")
# super()
# class Animal:
#    def move(self):
#      print('Animal is moving')

#    def eat(self):
#       print('Animal is eating')

# class Cat(Animal):
#    def move(self):
#      super().move()
#      print('Cat is moving')


# cat_1 = Cat()
# cat_1.move()
class Parent1:
   def move(self):
     print('Parent1 move')

# class Parent2:
#    def move(self):
#      print('Parent2 move')
     
# class Parent3:
#    def move(self):
#      print('Parent3 move')
     
     
# class Child1(Parent2, Parent1, Parent3):
#     def move(self):
#        super().move()
#        print('Child move')

# child_1_obj = Child1()
# child_1_obj.move()
# print(Child1.__mro__)
# staticmethod
# class Cat:
#     group = 'Domestic'

#     def __init__(self, name, age):
#        self.name = name
#        self.age = age

#     def eat(self):
#         print(f'{self.name} is eating. Group: {self.group}')

#     @staticmethod
#     def compute_time():
#         # Do some computation to be returned by this method
#         return "13:00"

# current_time = Cat.compute_time()
# print(current_time)
# callable(object)

# def simple_function():
#         return "Something"

# x = "hi"
# y = simple_function

# x()
# print(callable(x))
# print(callable(y))

# class Cat:
#     group = 'Domestic'

#     def __init__(self, name, age):
#        self.name = name
#        self.age = age
#     def __call__(self):
#        return "Callable"


# cat_1 = Cat("OOP", 2)
# print(cat_1())
# range(start, stop)
# numbers = range(1, 10)
# # print(list(numbers))

# # for each in range(1, 10, 2):
# #    print(each)

# print(list(range(1, 20, 2)))
# # len(object)
# languages = ["Kay", "Ray", "Node"]

# print(len(languages))
# sum(iterable)
# numbers = [4, 5]

# result = sum(numbers, 1)
# print(result)
# max(iterabe) min(iterable)
# numbers = (2, 9, 4)

# print("Max:", max(numbers))
# print("Min", min(numbers))

# my_string = ["a", "b", "c"]

# print("Max:", max(my_string))
# print("Min", min(my_string))
#hasattr(object, name)    #getattr(object, name)  #setattr(object, name, value)
# class Cat:

#     group = 'Domestic'

#     def __init__(self, name, age):
#        self.name = name
#        self.age = age

# cat_1 = Cat("Node", 2)
# name_value = getattr(cat_1, "name")
# print(name_value)
# setattr(cat_1, "level", 10)
# print("Cat's level:", hasattr(cat_1, "level"))
# print("Cat's age:", hasattr(cat_1, "age"))
# print("Cat's group:", hasattr(cat_1, "group"))
# isinstance(object, classinfo)
# my_list =  ["a", "b", "c"]

# # is_list = isinstance(my_list, list)
# # print(is_list)

# is_str = isinstance(my_list, str)
# print(is_str)
# issubclass(class, classinfo)
# class Parent1:
#     pass

# class Parent2:
#     pass

# class Child1(Parent1):
#     pass
# result = issubclass(Child1, Parent2)
# print(result)
# id(object)
# x = 5
# y = 10
# sum_value = x + y
# print(id(x))
# print(id(y))
# print(id(sum_value))
# round(number)
# num1 = round(20.44)
# num2 = round(22.78)
# num1 = round(20.44, 1)
# num2 = round(22.78, 1)

# print(num1)
# print(num2)
# num1 = round(6.5)
# num2 = round(7.5)

# print(num1)
# print(num2)
#frozenset()
     
# regular_set = set(["Lagos", "Kano", "Abia"]) 
# cities = frozenset(["Lagos", "Kano", "Abia"]) # frozenset

# # cities.add("New")
# regular_set.add("New")
# print(regular_set)
# property
class Person:
   
   def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name
       
#    def get_fullname(self):
#         return f"{self.first_name} {self.last_name}"
   @property
   def fullname(self):
        return f"{self.first_name} {self.last_name}" 
   
person_1 = Person("Kay", "Ray")
print(person_1.fullname)
person_1.first_name = "Ali"
print(person_1.fullname)

 






























































