'''
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
'''

'''
Solved the table on a piece of paper.
'''

def subset_sum(arr, sum):
    table = [[True for i in range(0, sum+1)] for j in range(0, len(arr)+1)]
    
    # Making the first row all false except the first value.
    for i in range(1, len(table[0])):
        table[0][i] = False

    # The main logic
    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            ele = arr[i-1]
            if j < ele:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-ele]

    return table[len(table)-1][len(table[0])-1]

print(subset_sum([3, 34, 4, 12, 5, 2], 9))


