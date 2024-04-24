MAX_PRICE = 10

class Product:
	all_products = []
	company_name = "Moon Inc."
	
	def __init__(self, name, price):
		self.name = name
		self.__price = price
		self.all_products.append(self)
		
	def get_total_price(self, quantity):
		return self.__price * quantity
	
	@property
	def price(self):
		return self.__price
        
	@price.setter
	def price(self, value):
		if not isinstance(value, (int, float)):
			raise ValueError("Price must be a number!")
		if value < 60:
			raise ValueError("Minimum amount is 60")
		else:
			self.__price = value