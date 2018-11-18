"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].
"""

'''
rough
-----

[0, 1, 2, 4, 5, 7]

start = 7
current = 7
prev = 5
'''

def summary_ranges(arr):
    if not arr:
        return []
    result = []
    start = arr[0]
    for i in range(1, len(arr)):
        current = arr[i]
        prev = arr[i-1]
        if current-1 != prev:
            result.append((start, prev))
            start = current
    result.append((start, arr[-1]))
    return result
    

print(summary_ranges([0, 2, 4, 5, 7]))
