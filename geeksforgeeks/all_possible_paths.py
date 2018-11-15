'''
https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
'''

'''
m = 3, n = 2

0,0 -> 0,1
|
1,0
'''


def all_possible_path(m, n):

    def helper(m, n, i, j):
        if i >= m or j >= n:
            return 0
        if i == m-1 or j == n-1:
            return 1
        
        return helper(m, n, i+1, j) + helper(m, n, i, j+1)

    if m == 0 and n == 0:
        return 0
    print(helper(m, n, 0, 0))

all_possible_path(2, 2)
