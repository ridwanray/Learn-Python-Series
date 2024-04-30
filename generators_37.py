# # my_number: int = 1232434343
# # for each in my_number:
# #     print(each)

# my_list = [1,2,3]
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
                    # Generators

# def get_sum(a, b):
# 	"""Returns the summation of two numbers"""	# docstring
# 	result = a + b # function body
# 	return result
   
# total = get_sum(1, 4)

# def generate_data():
#    print('processing a very large dataset')
#    print('First set of the data is ready!')
#    yield "Batch 1 returned"					
#    print('Second set of the data is ready!')
#    yield "Batch 2 returned"
#    print('Third set of the data is ready!')
#    yield "Batch 3 returned"

# # print(type((generate_data())))
# data = generate_data()
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))

# def get_infinite_sequence():
#    num = 0
#    while True:
#       yield num
#       num += 1 # num = num + 1

# sequence = get_infinite_sequence()
# # print(type(sequence))
# # print(next(sequence)) 
# # print(next(sequence)) 
# for each in sequence:
#    print(each)
                           # yield from
def inner_gen():
    yield 1

    yield 2
    yield 3

def outer_gen():
    
    yield from inner_gen()

gen = outer_gen()
print(next(gen))
print(next(gen))



