"""
Docstring for core-python.data-collections 2-tuple

Tuple | immutable | ordered | indexing | slicing | dupllicate values are allowed

syntax:

tuple_name = tuple()
tuple_name = ()

Example :

tuple_name = (ele1, ele2, ..., elen)
"""

nums = (1,2,3,4,5)
# print(nums)
# print(type(nums))

nums[0] = 111
print(nums) # TypeError: 'tuple' object does not support item assignment