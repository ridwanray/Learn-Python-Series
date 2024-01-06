# def do_something_on_int(passed_int):
#    passed_int = 10
#    print("Integer inside the function", passed_int)

# a = 2

# do_something_on_int(a)

# print("Interger after function call",a)
# def do_something_on_list(passed_list):
#    passed_list.append(4)
#    print("List inside function", passed_list)
 
# my_list = [1, 2, 3]

# do_something_on_list(my_list)

# print("List after function call", my_list)
# def do_something_on_int(passed_int):
#    # local scope
#    print(locals())
#    passed_int = 10

# a = 2

# do_something_on_int(a)
from copy import deepcopy
def do_something_on_list(passed_list):
    print(locals())
    passed_list = deepcopy(passed_list)
    passed_list.append("Four")
    print("List inside function", passed_list)
 
my_list = [1, 2, 3]

do_something_on_list(my_list)
print("List after function call", my_list)

