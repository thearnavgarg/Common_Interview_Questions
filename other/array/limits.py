"""
Sometimes you need to limit array result to use. Such as you only need the 
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value

If array, Min, Max value was given, it returns array that contains values of 
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.

ex) limit([1,2,3,4,5], None, 3) = [1,2,3]

Complexity = O(n)
"""

def limit(arr, min, max):
    import sys
    min = min if min != None else -sys.maxsize
    max = max if max != None else sys.maxsize
    result = []
    for num in arr:
        if min <= num <= max:
            result.append(num)
    return result

arr = [1, 2, 3, 4, 5]
min = None
max = 3
print(limit(arr, min, max))
