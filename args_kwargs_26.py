# def greet(*args, **kwargs):
#     print(args[0])
#     print(args[2])
    
# greet("Ray", 10)

# def sum_numbers(*args,**kwargs):
#     result = sum(args)
#     print("Sum of the numbers is", result)

# sum_numbers(10, 40, 5, 90, 150)

#This is supposed to be a method
# def list(self, request, *args, **kwargs):
#         "Retrieve user lists based on assigned role"
#         return super().list(request, *args, **kwargs)

# def greet(*args, **kwargs):
# 	kwargs["name"] = "Ali"
# 	print(kwargs["name"])

# greet(10, name="Ray")

def notification_logger(**kwargs):
    kwargs["user"] = User.objects.get(id=kwargs["user"])
    notif_obj = Notification.objects.create(**kwargs)
    user_email = kwargs["user"].email
    notification = create_notification(notif_obj.type)
    notification.push_email(user_email,{"message": notif_obj.content})
    return notif_obj

def greet(required, *args, **kwargs):
    print(required)
def sum_numbers(*args):
    result = sum(args)
    return result

# Argument Unpacking
# scores = (20, 50, 40, 50, 60)

# total = sum_numbers(*scores) #sum_numbers(20, 50, 40)
# print(total)

notification_data = {
            "user": user.id,
            "type": "PASSWORD_CHANGED",
            "content": "Your password was changed successfully!",
        }

notification_logger(**notification_data)
notification_logger(user=user.id, type="PASSWORD_CHANGED",
                    content="Your password was changed successfully!")
