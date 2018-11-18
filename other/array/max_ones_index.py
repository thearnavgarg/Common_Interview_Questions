"""
Find the index of 0 to be replaced with 1 to get
longest continuous sequence
of 1s in a binary array.
Returns index of 0 to be
replaced with 1 to get longest
continuous sequence of 1s.
If there is no 0 in array, then
it returns -1.

e.g.
let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
If we replace 0 at index 3 with 1, we get the longest continuous
sequence of 1s in the array.
So the function return => 3
"""

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
[1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]

mapping
{
   3: 8
   9: 8
}
'''

def max_ones_index(arr):
    from collections import defaultdict
    import sys
    if arr.count(0) == 0:
        return -1
    mapping = defaultdict(int)
    current = 0
    for i, num in enumerate(arr):
        if num == 0:
            mapping[i] = current
            current = 0
        else:
            current += 1
    current = 0
    for i in reversed(range(len(arr))):
        num = arr[i]
        if num == 0:
            mapping[i] += current
            current = 0
        else:
            current += 1
    count = -sys.maxsize
    result = -1
    for key, value in mapping.items():
        if count < value:
            count = value
            result = key
        if count == value and result > key:
            result = key
    return result


def max_ones_index_v2(arr):
    n = len(arr)
    max_count = 0
    max_index = 0
    prev_zero = -1
    prev_prev_zero = -1

    for curr in range(n):
        # If current element is 0,
        # then calculate the difference
        # between curr and prev_prev_zero
        if arr[curr] == 0:
            if curr - prev_prev_zero > max_count:
                max_count = curr - prev_prev_zero
                max_index = prev_zero

            prev_prev_zero = prev_zero
            prev_zero = curr
    if n - prev_prev_zero > max_count:
        max_index = prev_zero

    return max_index
    
print(max_ones_index([1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]))
