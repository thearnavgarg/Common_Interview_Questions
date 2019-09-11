class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 0 and n == 0:
            return 0
        
        if m == 1 and n == 1:
            return 1
        
        table = [[0 for i in range(m)] for j in range(n)]
        table[0][0] = 1
        
        # print(table)
        
        for i in range(1, n):
            table[i][0] = 1
        
        for j in range(1, m):
            table[0][j] = 1
                
        for i in range(1, n):
            for j in range(1, m):
                table[i][j] += table[i-1][j] + table[i][j-1]
        
        return table[-1][-1]
