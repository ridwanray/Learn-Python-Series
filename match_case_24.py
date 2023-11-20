# status = 200

# match status:
#     case 400:
#             print("Bad request")
#     case 401:
#             print("Unauthorised")
#     case 403:
#             print("Permission denied")
#     case 500:
#             print("Server error")
#     case _:
#             print("Default error")

# day = "OP"

# match day:
#     case "Mon":
#         print("Monday")
#     case "Sun":
#         print("Sunday")
#     case "Fri":
#         print("Friday")
#     case _:
#         print("No match found")


# status = 403

# match status:
#     case 400:
#             print("Bad request")
#     case 401 | 403:
#             print("Authentication error")
#     case 500:
#             print("Server error")
#     case _:
#             print("Default error")
# items =  ["Ray", 2, 4, 5]

# match items:
#     case ["Ray", *b]:
#         print("Ray is present")
#         print(b[0])
#         print(b[3])
#         print(f"b is {b}")
    
#     case [a]:
#         print("One item is present")
#         print(f"a is {a}")
    
#     case []:
#         print("No item in the collection")
    
#     case _:
#         print("No match found")


info = {"name":"ray", "level": 10, "age": 9}

match info:
    # case {"age": age, "name": name}:
    #     print(f"age is {age} and name is {name}")

    # case {"age": 9, "name": "ray"}:
    #     print("age is 9 and name is ray")
    
    case {"age": 9, **rest}:
        print(rest["name"])
        print(rest["contact"])
        # print("age is 9 and name is ray")
    
    case _:
        print("No match found")
# Conditional/Guard matching: case x if expression
# status = 0

# match status:
#     case x if x > 0:
#         print("+ve number", x)
    
#     case x if x < 0:
#         print("-ve number", x)
#     case _:
#         print("Zero")

# item = [1, 5]
# match item:
#     case [x, y] if x + y > 4:
#         print("Sum is > 4")
    
#     case [x, y] if x + y < 4:
#         print("Sum is below 4")

#Sub-pattern match: A pattern in a pattern
# route = ["go", "east"]
# match route:
#     case ["go", ("east" | "west" | "south" | "north") as direction]:
#         print("go to the ", direction)
#     case _:
#         print("No match")

# Type matching
# x = "age"
# match x:
#     case str(x):
#         print("x is a string", x)
#     case int(x):
#         print("x is an integer", x)
    
# item = {1, 2}
# match item:
#     case [int(x), int(y)] if x + y > 4:
#         print("Sum is > 4")
    
#     case [int(x), int(y)] if x + y < 4:
#         print("Sum is below 4")
#     case set(x):
#         print("x is a set", x)
#         print("type of x", type(x))
#     case _:
#         print("No match")
















































