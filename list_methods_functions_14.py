#list.insert(i, x)
# courses = ["Agriculture", "Biology", "Chemistry"]
# # courses.insert(0, "Physics")
# # courses.insert(5, "Math")
# courses.insert(-1, "Eco")
# print(courses)
# #list.pop()
# courses = ["Agriculture", "Biology", "Chemistry"]
# removed_item = courses.pop(4)
# print(courses)
# .append()
# numbers = [1, 2, 3, 4]
# numbers.append(5)
# print(numbers)
# .extend()
# courses = ["Biology", "Chemistry"]
# # courses.extend(["Agric", "Math"])
# courses.extend("Math")
# print(courses)
# .reverse()
# numbers = [1, 2, 3, 6, 5, 9]
# new_numbers = numbers.reverse()
# print(new_numbers)
# .remove()
# courses = ["Biology", "Chemistry", "Biology"]
# courses.remove("Biology1")
# print(courses)
# .count()
# numbers = [1, 2, 3, 1]
# times = numbers.count(1)
# print(times)
# # .sort() 
# numbers = [4,2,9,0,8]
# numbers.sort(reverse=True)
# print(numbers)
# .clear()
# numbers = [1, 2, 3]
# numbers.clear()
# print(numbers)
# # sum()
# result = sum([])
# print(result)
# min()
# # numbers = [1, 2, 3, 4, 5]
# numbers = []
# minimum = min(numbers)
# print(minimum)
# max()
# numbers = [4, 1, 7, 2, 8]
# numbers = []
# maximum = max(numbers)
# print(maximum)
# list()
# var_name = list()
# print(var_name)
# my_list = [3,1,2,4]
# new_list = sorted(my_list)
# print("new list:", new_list)
# print("original list", my_list)
# my_list = [1,2,3,4,5]
# del my_list[0:4]
# print(my_list)
# my_list = ["A","B","C","D"]
# my_list[0:2] = [1, 2, 3]
# print(my_list)
# string.split()
# name = "Anas Ridwan".split()
# print(name)

# name = "Anas,Ridwan".split(",")
# print(name)
import copy
original_list = [1, [2, 3], 4]
new_list = copy.deepcopy(original_list)
original_list[1][1] = 9
print(original_list)
print(new_list)























































































































