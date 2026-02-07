"""
# Docstring for core-python.data-collections.4-dict

# Dict : mutable, ordered, duplicate keys are not allowed

# dict_name = dict()
# dict_name = {
#     "k1" : v1,
#     "k2" : v2,
#     ...
#     "kn" : vn
# }
# """

# fruits = {
#     "apple" : 150,
#     "banana" : 300,
#     "grapsh" : 1000
# }

# # print(fruits)
# # print(fruits["apple"])
# # print(fruits["grapsh"])

# contacts = {
#     "M" : [
#         { 
#             "Monika" : {
#                 "mobile" : "3985674378",
#                 "email": ["monica@gmail.com", "monika1@gmail.com"]
#             }
#         }
#     ],
#     "B" : [
#         { 
#             "brijesh" : {
#                 "mobile" : "3985674378",
#                 "email": ["brijesh@gmail.com"]
#             }
#         }
#     ]
# }
# # print(contacts["B"])
# print(contacts["B"])
# print(contacts["B"][0])
# print(contacts["B"][0]["brijesh"])
# print(contacts["B"][0]["brijesh"]["mobile"])
# print(contacts["B"][0]["brijesh"]["email"])
# print(contacts["B"][0]["brijesh"]["email"][0])


car = {
    "name": "bmw",
    "price" : 50,
    # "color": "black"
}

# car.setdefault("color", "red")


# print(car)
# print(car.keys())
# print(car.values())
# print(car.items())

# car.clear()


# print(car)

# new_data = {
#     "model" : "XYZ"
# }
# car.update(new_data)
# print(car)

# items = ["tomato", "potato", "onion"]
# price = 50

# empty_dict = dict()
# new_dict = empty_dict.fromkeys(items, price)
# print(new_dict)