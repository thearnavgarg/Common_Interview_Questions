"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""

'''
[1, 2, [3, 4, [5]], 6]

1, 2
3, 4
5
6
'''

def flatten(arr):
    def helper(arr, new_arr):
        if type(arr) == int:
            new_arr.append(arr)
            return
        for num in arr:
            helper(num, new_arr)

    if not arr:
        return []
    new_arr = []
    helper(arr, new_arr)
    return new_arr

print(flatten([1, 2, [3, 4, [5]], 6]))
