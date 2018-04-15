'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


value = {60, 100, 120}
weight = {10, 20, 30}
total_w = 50

Solution = 50


value = {1, 4, 5, 7}
weight = {1, 3, 4, 5}
total_w = 7

'''

'''
Scratch work

table

V   W   0   1   2   3   4   5   6   7 
1   1   0   1   1   1   1   1   1   1
4   3   0   1   1   4   5   5   5   5
5   4   0   1   1   4   5   6   6   9
7   5   0   1   1   4   5   7   8   9


'''


def knapsack(value, weight, total):
    table = [[0 for i in range(0, total+1)] for j in range(0, len(weight))]

   # Filling in the first row
    for i in range(0, len(table[0])):
        w = weight[0]
        v = value[0]
        if i >= w:
            table[0][i] = v
        else:
            table[0][i] = 0

    # Filling in all the other rows
    for i in range(1, len(table)):
        for j in range(0, len(table[0])):
            v = value[i]
            w = weight[i]
            if w > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j],
                                  v + table[i-1][j-w])

    print(table)
    return table[len(table)-1][len(table[0])-1]


print(knapsack([1, 4, 5, 7], [1, 3, 4, 5], 7))
