                                        # Object Oriented Programming

# user1_email = "a@a.com"
# user1_username = "ray"
# user1_dob = "1950"

# def user1_create_post():
#     print("First post")

# user2_email = "a@a.com"
# user2_username = "ray"
# user2_dob = "1950"

# def user2_create_post():
#     print("First post")

                                        # Classes and Objects

# 1st part
# class User:
#     def __init__(self, email, age):
#         self.email = email
#         self.age = age

# user1 = User("1@gmail.com", 10)
# user2 = User("2@gmail.com", 20)

# print("Before updated:",user1.email)
# user1.email = "3@gmail.com"
# print("After update:", user1.email)
# user1.price = 100
# print(user1.price)

# # print(user1.age)

# class User:
#     def __init__(self, email, age):
#         self.email = email
#         self.age = age
    
#     def create_post(self, content):
#         print(f"{content} by {self.email}")


# user1 = User("1@gmail.com", 10)
# user1.create_post("Hello world")

# user2 = User("2@gmail.com", 20)
# user2.create_post("Hi there")

# class Product:
# 	def __init__(self, name, price):
# 		self.name = name
# 		self.price = price
	
# 	def get_total_price(self, quantity):
# 		return self.price * quantity

# product1 = Product("Bag", 20)
# product1.get_total_price(5)

                                        # class attributes

# class Product:
# 	all_products = []
# 	company_name = "Moon Inc."
	
# 	def __init__(self, name, price):
# 		self.name = name
# 		self.price = price
# 		self.all_products.append(self)
		
# 	def get_total_price(self, quantity):
# 		return self.price * quantity
        
# 	# def __repr__(self):
# 	# 	return f"Product({self.name} {self.price})"
	
# 	def __repr__(self):
# 		return f"{self.__class__.__name__}({self.name} {self.price})"
	
    
        


# Product("Bag", 20)
# Product("Socks", 10)
# Product("Shoe", 40)
# print(Product.all_products)
# product1.get_total_price(5)

# print(Product.name)
# # print(product1.company_year)

                                    # class methods
# class Product:
# 	all_products = []
# 	company_name = "Moon Inc."
	
# 	def __init__(self, name, price):
# 		self.name = name
# 		self.price = price
# 		self.all_products.append(self)
		
# 	def get_total_price(self, quantity):
# 		return self.price * quantity
	
# 	@classmethod
# 	def get_product_count(cls):
# 		platform_products = cls.all_products
# 		return len(platform_products)
	
# 	def __repr__(self):
# 		return f"{self.__class__.__name__}({self.name} {self.price})"
	
# product1 = Product("Bag", 20) 
# Product("Socks", 20) 
# Product("Shoe", 20) 
# Product("Shirt", 20) 
# # product_count = Product.get_product_count()
# # print(product_count)
# product_count = product1.get_product_count()
# print(product_count)

                                #static methods
# class Product:
# 	all_products = []
# 	company_name = "Moon Inc."
	
# 	def __init__(self, name, price):
# 		self.name = name
# 		self.price = price
# 		self.all_products.append(self)
		
# 	def get_total_price(self, quantity):
# 		return self.price * quantity
	
# 	@classmethod
# 	def get_product_count(cls):
# 		platform_products = cls.all_products
# 		return len(platform_products)
	
# 	def __repr__(self):
# 		return f"{self.__class__.__name__}({self.name} {self.price})"
	
# 	@staticmethod
# 	def get_current_time():
# 		return "12PM"
	
# product1 = Product("Bag", 20) 
# # current_time = Product.get_current_time()
# current_time =product1.get_current_time()
# print(current_time)

                                # read-only attributes: getters & setters
# class Product:
# 	all_products = []
# 	company_name = "Moon Inc."
	
# 	def __init__(self, name, price):
# 		self.name = name
# 		self.__price = price
# 		self.all_products.append(self)
		
# 	def get_total_price(self, quantity):
# 		return self.__price * quantity
	
# 	@classmethod
# 	def get_product_count(cls):
# 		platform_products = cls.all_products
# 		return len(platform_products)
	
# 	def __repr__(self):
# 		return f"{self.__class__.__name__}({self.name} {self.__price})"
	
# 	@staticmethod
# 	def get_current_time():
# 		return "12PM"
	
# 	@property
# 	def price(self):
# 		return self.__price
        
# 	@price.setter
# 	def price(self, value):
# 		if not isinstance(value, (int, float)):
# 			raise ValueError("Price must be a number!")
# 		if value < 60:
# 			raise ValueError("Minimum amount is 60")
# 		else:
# 			self.__price = value
		
# product1 = Product("Shirt", 20)
# product1.price = 90
# print(product1.price)
# # # print(product1.price)
# print(product1.get_total_price(4))
                                   # OOP Principles
# 1. Inheritance

# class Animal:
#         animal_type = "Domestic"

#         def eat(self):
#                 print("Animal is eating")

#         def move(self):
#                 print("Animal is moving")


# class Cat(Animal):
#         def eat(self):
#                 super().eat()
#                 print("Cat is eating")


# cat1 = Cat()
# cat1.eat()
# print(cat1.animal_type)
                                    # Multiple Inheritance
# class Parent1:
#    def move(self):
#      print('Parent1 move')

# class Parent2:
#     def move(self):
#       print('Parent2 move')

# class Parent3:
#     def move(self):
#       print('Parent3 move')

# class Child1(Parent1, Parent3, Parent2):
     
#      def move(self):
#         super().move()
#         print('Child move')

# child1 = Child1()
# child1.move()
# print(Child1.__mro__)

                            # Inheritance Practice
# class Product:
# 	all_products = []
# 	company_name = "Moon Inc."
	
# 	def __init__(self, name, price):
# 		self.name = name
# 		self.__price = price
# 		self.all_products.append(self)
		
# 	def get_total_price(self, quantity):
# 		return self.__price * quantity
	
# 	@classmethod
# 	def get_product_count(cls):
# 		platform_products = cls.all_products
# 		return len(platform_products)
	
# 	def __repr__(self):
# 		return f"{self.__class__.__name__}({self.name} {self.__price})"
	
# 	@staticmethod
# 	def get_current_time():
# 		return "12PM"
	
# 	@property
# 	def price(self):
# 		return self.__price
        
# 	@price.setter
# 	def price(self, value):
# 		if not isinstance(value, (int, float)):
# 			raise ValueError("Price must be a number!")
# 		if value < 60:
# 			raise ValueError("Minimum amount is 60")
# 		else:
# 			self.__price = value


# class Shirt(Product):
# 	def __init__(self, name, price):
# 		super().__init__(name, price)
		
# shirt1 = Shirt("Bag", 20)
# Shirt("Socks", 10)
# total_price = shirt1.get_total_price(5)
# print(Shirt.get_product_count())
# # print("total price", total_price)
# # print(shirt1)
                                #Encapsulation 
# class Product:
# 	all_products = []
# 	company_name = "Moon Inc."
	
# 	def __init__(self, name, price):
# 		self.name = name
# 		self.__price = price
# 		self.all_products.append(self)
		
# 	def get_total_price(self, quantity):
# 		return self.__price * quantity
	
# 	def __process_report(self):
# 		print("processing")
		
# 	def send_report(self):
# 		self.__process_report()
# 		print("Report sent to the user!")
	
# 	@classmethod
# 	def get_product_count(cls):
# 		platform_products = cls.all_products
# 		return len(platform_products)
	
# 	def __repr__(self):
# 		return f"{self.__class__.__name__}({self.name} {self.__price})"
	
# 	@staticmethod
# 	def get_current_time():
# 		return "12PM"
	
# 	@property
# 	def price(self):
# 		return self.__price
        
# 	@price.setter
# 	def price(self, value):
# 		if not isinstance(value, (int, float)):
# 			raise ValueError("Price must be a number!")
# 		if value < 60:
# 			raise ValueError("Minimum amount is 60")
# 		else:
# 			self.__price = value
		
# product1 = Product("Shirt", 20)
# product1.send_report()

                                         # Abstraction

# from abc import ABC, abstractmethod

# class AbstractProduct(ABC):

#     @abstractmethod
#     def get_total_price(self):
#         pass

# class Product(AbstractProduct):
#     pass
#     # def get_total_price(self):
#     #     print("Total price is #50")

# product1 = Product()
# # # product1.get_total_price()
# # product2 = AbstractProduct()
                                        # Polymorphism
# 1. Function polymorphism

# string_1 = "abc"
# list_1 = ["a", "b", "c", "e", "f"]


# print(len(string_1))
# print(len(list_1))

# 2. Operator polymorphism

# str1 = "a"
# str2 = "b"

# int1 = 1
# int2 = 2

# print(str1 + str2)
# print(int1 + int2)

# #__add__, __sub__,

# 3. Method overloading

class Summation:
    
    def sum(a, b , c=None):
        pass

# 4. Method overriding
    
class Parent:
   def move(self):
     print('Parent1 move')


class Child(Parent):
     def move(self):
        print('Child move')
