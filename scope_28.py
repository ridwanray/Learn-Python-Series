# def function_a():
#     var_a = "Ray" #local scope
#     print(f'value of var_a is {var_a}')

# function_a() #function call

# print(f"value of var_a {var_a}")
# def outer_function():
#   #local scope for outer_function
#   name = 'Ray'
#   # enclosing scope for inner_function

#   def inner_function():
#      # local scope for inner_function
#      print(f'Name from inner function():',name)
#   inner_function()

# outer_function()
# def outer_function():
#    name = 'Ray' #local scope for outer_func
 
#    def inner_function():
#        age = 12 #local scope for inner_function
   
#    print(age) #using variable 'age'
     
# outer_function()
#Global Scope
# name = "Python"

# def show_name():
#     print("Name coming from function", name)

# class Test:
#     def show(self):
#         print("Name coming from class", name)

# show_name()
# Test().show()

# age = 9 # global scope
# def outer_func():
#     # local scope of outer_func()
#     # enclosing scope of inner_func()
#     age = 6
#     def inner_func():
#         # local scope of inner_func()
#         print(age)

#     inner_func()

# outer_func()
# Builtin Scope
# sum = 6
# print(sum([1, 2, 4]))
# global keyword

# global_variable = 10  #global scope
 
# def modify():
#    global global_variable
#    global_variable = 80
#    print("Value from modify function ",global_variable)

# modify()

# print("Value from global",global_variable)

# initial_value = 9 #global scope

# def increment():
#    global initial_value
#    initial_value = initial_value + 1
#    print(initial_value)

# # [*]usage
# increment()
# nonlocal keyword
# def outer():
#     # local scope for outer()
#     x = 10
#     # enclosing scope for inner()
    
#     def inner():
#         #local scope for inner()
#         nonlocal x
#         x = 20
#         print("coming from inner", x)
        
#     inner() #function call
#     print("coming from outer", x)

# outer()


# globals() and locals()
name = "Python"

def show_name():
    age = 10
    print(locals())

# print(globals())
show_name()























