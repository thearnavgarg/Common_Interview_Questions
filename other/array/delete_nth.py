'''
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
'''
'''
Input: [1,2,3,1,2,1,2,3], 2
'''

def delete_nth(arr, n):
    if not arr:
        return []

    from collections import defaultdict
    mapper = defaultdict(int)
    new_arr = []

    for num in arr:
        mapper[num] += 1
        if mapper[num] <= n:
            new_arr.append(num)
    
    return new_arr

arr = [1,2,3,1,2,1,2,3]
n = 2
print(delete_nth(arr, n))

