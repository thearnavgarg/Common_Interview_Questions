
"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""

'''
scratch work

[3, 4, 5, 10] and 1 -> 10

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

def missing_ranges(arr, low, high):
    curr = low
    result = []
    while curr <= high:
        # logic
        if curr in arr:
            end = curr-1
            if low <= end:
                result.append((low, end))
            low = curr+1
        curr += 1
    if low <= high:
        result.append((low, high))
    return result

def main():
    arr = [3, 5]
    low = 1
    high = 10
    print(missing_ranges(arr, low, high))

main()

