# # class User:
# # 	app_name = "FB"

# # 	def __init__(self, email, age):
# # 		self.email = email
# # 		self.age = age
# # 	def get_name(self):
# # 		print(self.app_name)

# # user1 = User("email", 1)
# # user1.ma
# # # print(User.email)

# # #AttributeError: type object 'User' has no attribute 'email'
# # # print(user1.brand)
# # # user2 = User("2@gmail.com", 20)


# class Product:
# 	company_name = "Moon Inc."
# 	all_products = []

# 	def __init__(self, name, price):
# 		print("called")
# 		self.name = name
# 		self.price = price

# 		self.all_products.append(self)
	
# 	def get_total_price(self, quantity):
# 		return self.price * quantity
		
# 	def get_product_info(self):
# 		return f"Price:{self.price}  name: {self.name}  Company name: {self.company_name}"
	
# 	# def __str__(self):
# 	# 	return "Hey"
# 	# def __repr__(self):
# 	# 	return f"Product({self.name}, {self.price})"

# 	# def __repr__(self):
# 	# 	return f"{self.__class__.__name__}({self.name}, {self.price})"
	
# 	@classmethod
# 	def get_product_count(cls):
# 		platform_products = cls.all_products
		
# 		return len(platform_products)
	
# 	@staticmethod
# 	def get_current_time():
# 		return "12pm"
    


# class Shirt(Product):
	
# 	def __init__(self, name, price):
# 		super().__init__(name, price)

# 	def get_product_info(self):
# 		return "Shirt info is different"
# 	# def __init__(self):
# 	# 	print("called from Laptop init")
# 	# def __init__(self, name, price):
# 	# 	# super().__init__(name, price)
# 	# 	pass
# 	pass



# l1 = Shirt()
# print(l1)
# # product1 = Product("Shoe", 10)
# # product1 = Product("Bag", 10)
# # product1 = Product("Socks", 10)
# # product1 = Product("Shirt", 10)

# # print(product1.get_current_time())
# # # print(Product.all_products)
# # # print("Product Count:", Product.get_product_count())

# # print("Time", Product.get_current_time())



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age   # private variable

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if age > 0:
#             self.__age = age

# person = Person("Alice", 30)
# print(person.__age)


# class Product:
# 	company_name = "Moon Inc."
# 	all_products = []

# 	def __init__(self, name, price):
# 		self.name = name
# 		self.price = price

# p1 = Product("Bag", 50)
# print(p1.price)
# p1.price = 100
# print(p1.price)

# p1.price =  "10"
# print(p1.price)


class Product:
	company_name = "Moon Inc."
	all_products = []

	def __init__(self, name, price):
		self.name = name
		self.__price = price

		self.all_products.append(self)
	
	@property
	def price(self):
		return self.__price
	
	@price.setter
	def price(self, value):
		if not isinstance(value, (int,float)):
			raise ValueError("Price must be a numeric value")
		if value < 60:
			raise ValueError("Mininum amount is 60")
		else:
			self.__price = value
	
	def get_total_price(self, quantity):
		return self.__price * quantity
		
	def get_product_info(self):
		return f"Price:{self.__price}  name: {self.name}  Company name: {self.company_name}"
    
	def __repr__(self):
		return f"Product({self.name}, {self.__price})"
	
	def __repr__(self):
		return f"{self.__class__.__name__}({self.name}, {self.price})"


p1 = Product("Bag", 50)
print(p1.price)
p1.price = 140