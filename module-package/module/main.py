# import product

# print(product.MAX_PRICE)

# from module_name import specific_object
# from helpers import *

from product import *

#from product import Product as GenericProduct, MAX_PRICE as price

# product1 = GenericProduct("shirt", price)
product1 = Product("shirt", MAX_PRICE)

if (__name__ == "__main__"):
    print(product1.get_total_price(5))
