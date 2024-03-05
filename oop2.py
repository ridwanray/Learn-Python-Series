class Product:
	company_name = "Moon Inc."
	all_products = []

	def __init__(self, name, price):
		self.name = name
		self.price = price
		
		self.all_products.append(self)
	
	def get_total_price(self, quantity):
		return self.price * quantity
		
	def get_production_info(self):
		return f"Price:{self.price}  name: {self.name}  Company name: {self.company_name}"
	
	@classmethod
	def get_product_count(cls):
		platform_products = cls.all_products
		return len(platform_products)
	

product1 = Product("Shoe", 10)
Product("Bag", 10)
Product("Socks", 10)
Product("Shirt", 10)

# print(Product.all_products)

# print(Product.get_product_count())

# print(product1.get_product_count())

product1.price =  "abc"
print(product1.get_total_price(3))
#start at 440 in script


from abc import ABC, abstractmethod


class AbstractProduct(ABC):

	@abstractmethod
	def get_total_price(self):
		pass

class Product(AbstractProduct):
	def get_total_price(self):
		pass

product1 = Product()
