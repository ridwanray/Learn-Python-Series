# def function_name():
#     body of the function 		
#     <statement1>
#     <statemen2>

# def greet(name,age ):
#     print(f"Your name is {name} and your age is {age}")
#     print("How are you ?")

# greet("Ali", 10)

# Sum of two numbers

# def sum_numbers(n1, n2):
#     result = n1 + n2
#     print("Sum of the two numbers is", result)

# sum_numbers(10, 40)
# sum_numbers(50, 40)
#Positional & Keywords arguments
# def greet(name, age):
#     print(f"Your name is {name} and your age is {age}")
#     print("How are you ?")

# # greet(name="Ali", age=10)
# greet("Ali", age=10)


# Default args <name>=<value>

# def greet(name="Ray", age=15):
#     print(f"Your name is {name} and your age is {age}")
#     print("How are you ?")

# greet()
# 	The return keyword
# 	def function_name(parameters):
#     	function body
# 		return

# def sum_numbers(n1, n2):
#     result = n1 + n2
#     return result

# summation = sum_numbers(5, 4)
# print("Sum of numbers is", summation )
# The pass keyword
# def add_nums():
#     pass
# if 5 > 6:
#     pass
# Function Docstring
# def sum_numbers(n1, n2):
#     """Takes two numbers and return ther sum"""
#     result = n1 + n2
#     return result

# print(sum_numbers.__doc__)
# print(print.__doc__)
# def calculate_area(length, width):
#     """
#     This function calculates the area of a rectangle.

#     Parameters:
#     - length (float): The length of the rectangle.
#     - width (float): The width of the rectangle.

#     Returns:
#     float: The calculated area of the rectangle.
#     """
#     area = length * width
#     return area
# Create a project that takes student scores & computes the corresponding grades.
# calculates average score
# determine the grade

def calculate_average(scores):
    if not scores:
        return 0.0
    total = sum(scores)
    average = total / len(scores)
    return average

def determine_grade(average_score):
    if average_score >= 90:
        return "A"
    if average_score >= 80:
        return "B"
    if average_score >= 70:
        return "C"
    if average_score >= 60:
        return "D"
    else :
        return "F"

average_score_value = calculate_average([])
grade_value = determine_grade(average_score_value)
print("Your grade is", grade_value)