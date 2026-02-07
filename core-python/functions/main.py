# syntax :

# def function_name(para1, para2,...,paran):
#     block of statments

# function call
# function_name(val1, val2,...,valn)

# a = 10
# b = 20
# res = a + b
# print(res)

# a = 150
# b = 250
# res = a + b
# print(res)

# positional parameters
# def addition(num1, num2):
#     res = num1 + num2
#     print(res)

# addition(10, 20)
# addition(150, 250)

# defualt/keywords para
# def bill(tomato=20, potato=30):
#     print(tomato + potato)

# bill(tomato=50)

# def add(a,b,c):
#     print(a+b+c)
    
# add(10, 20, 30)

# variable length *args

# def add(*nums):
#     print(sum(nums))
    
# add(10, 20, 30, 40)


# **kwargs

# def bill(**products):
#     total = 0
#     for key, value in products.items():
#         print(f"name: {key} | price: {value}")
#         total = total + value
#     print("Total amount: ", total)

# bill(pen=20, gold_milk=56, potato=35, thums_up=45)


nums = [1,2,3,4,5]
nums_square = list(map(lambda num: num**2, nums ))
print(nums_square)