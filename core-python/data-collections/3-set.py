"""
Docstring for core-python.data-collections.3-set

set : mutbale | unordered | unindexed | slicing is not possible | duplicate values are not allow

syntax :

set_name = set()
set_name = {}

set_name = {ele1, ele2, ..., elen}
"""

nums = {1,2,3,4,1,2,3,4,12,13,1,4,1,3,1,454,4,1,3,1,4,5,6}

# print(nums)
# nums.add(550)
# print(nums)

fset = frozenset(nums) # immutable
print(fset)
fset[2] = 1080
print(fset) # TypeError: 'frozenset' object does not support item assignment