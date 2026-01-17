# syntax :
# use : finite
# for var in iterable_var:
#     block of code

# name = "Baroda institute of technology"

# for ch in name:
#     print(ch)

# range syntax :
# range(start, end+1, step+1)
# print(range(10)) # range(0, 10)
# print(list(range(1, 10 + 1))) # range(0, 10)
# print(list(range(1, 10 + 1, 1))) #
# print(list(range(1, 10 + 1, 2))) #

# print(list(range(10, 0, -1)))
# print(list(range(10, 0, -3)))
# print(list(range(10, 0, 1)))

# num = 5
# for num in range(1, num+1):
#     print(num)

# *****

# num = 5
# for row in range(1, num+1):
#     print("*", end="")

# num = 5
# for row in range(1, num+1):
#     print("* ", end="")

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print("* ", end="")
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("* ", end="")
#     print()

# ----*
# ---**
# --***
# -****
# *****

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print("  ", end="")
#     for col in range(1, row+1):
#         print("* ", end="")
#     print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print("  ", end="")
#     for col in range(1, row+1):
#         print("* ", end="")
#     for col in range(1, row):
#         print("* ", end="")
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+2):
#         print("* ", end="")
#     print()

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print(" ", end="")
#     for col in range(1, row+1):
#         print("*", end="")
#     for col in range(1, row):
#         print("*", end="")
#     print()

# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(" ", end="")
#     for col in range(1, num-row+1):
#         print("*", end="")
#     for col in range(1, num-row):
#         print("*", end="")
#     print()