# name = "Alex"
# message = "Your name is %s" %name 
# print(message)

# name = "Alex"
# age = 9
# message = "Your name is %s and your age is %d" % (name, age)
# print(message)

# name = "Alex"
# age = 9
# message = "Your name is %(name)s and your age is %(age)d"%{'age':8,'name':'Ray'}
# print(message)

# name = "Alex"
# age = 9
# message  = "Name:{} Age:{}".format(name,age)
# message  = "Name:{0} Age:{1}".format(name,age)
# message  = "Name:{name} Age:{age}".format(name=name,age=age)
# F-string
# message =  f"Name: {name}  Age:{age}"
# message =  f"Name: {name.upper()}  Age:{age + 1}"
# print(message)


from string import Template
name = "Alex"
age = 9
message_template = Template('Name: $name Age: $age')
message = message_template.substitute(name=name, age=age)
print(message)