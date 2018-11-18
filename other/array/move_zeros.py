"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""

'''
[false, 1, 1, 2, 1, 3, 0, 0, "a"]
                       |
'''

def move_zeros(arr):
    if not arr:
        return []
    # The index of the first zero that we can 
    # switch
    zero_idx = -1
    for i in range(0, len(arr)):
        # if this is the first zero that we have 
        # encountered. 
        if arr[i] == 0 and zero_idx == -1:
            zero_idx = i
        # if it's a non-zero element and we have seen a zero
        # before, then we swap te first zero with the element
        if arr[i] != 0:
            if zero_idx != -1:
                arr[i], arr[zero_idx] = arr[zero_idx], arr[i]
                zero_idx += 1
    return arr

print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
