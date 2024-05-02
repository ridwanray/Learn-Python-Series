# def outer_func(x):

#    def inner_func():
#       print("Value of x from inner::",x)

#    return inner_func

# inner = outer_func(50)
# inner()
# # print(type(inner))

# class User:
#     def __init__(self, permission:str):
#         self.name = "ridwanray"
#         self.age = 10
#         self.permission = permission

#     def get_user_info(self):
#         return {
#             "name":self.name,
#             "age": self.age,
#             "permission": self.permission
#         }

# read_only_user = User("READ_ONLY")
# write_only_user = User("WRITE_ONLY")
# print(read_only_user.get_user_info())

def user_factory(permission:str):

    def user():
        user_info = {
            "name":"ridwanray",
            "age": 10,
            "permission": permission
        }
        return user_info
    return user
read_only_user = user_factory("READ_ONLY")
print(read_only_user())

