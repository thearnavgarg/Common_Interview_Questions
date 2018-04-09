
"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""

'''



'''

def two_sum(arr, target):
    if not arr:
        return None
    map = {}
    for idx, ele in enumerate(arr):
        if ele in map:
            return (map[ele], idx)
        else:
            map[target-ele] = idx
    return -1

def main():
    arr = [2, 7, 11, 15]
    print(two_sum(arr, 9))

main()
