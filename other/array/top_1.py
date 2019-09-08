"""
This algorithm receives an array and returns most_frequent_value
Also, sometimes it is possible to have multiple 'most_frequent_value's,
so this function returns a list. This result can be used to find a 
representative value in an array.

For example: top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]

(TL:DR) Get mathematical Mode
Complexity: O(n)
"""

'''
'''

def top_1(arr):
    from collections import defaultdict
    if not arr:
        return []
    table = defaultdict(int)
    for num in arr:
        table[num] += 1
    result = []
    table = sorted(table.items(), key=lambda x:-x[1])
    freq = table[0][1]
    for value in table:
        if freq == value[1]:
            result.append(value[0])
        else:
            break
    return result

arr = [1,  2, 2, 3, 4]
print(top_1(arr))


