class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # helper functions
        ###############################
        def get_left(i, j, table):
            if j < 1:
                return float('inf')
            return table[i][j-1]
        
        def get_top(i, j, table):
            if i < 1:
                return float('inf')
            return table[i-1][j]
        ###############################
        
        # base checks
        if not grid:
            return 0
        
        if not grid[0]:
            return 0
        
        table = [[0 for val in row] for row in grid]
        
        # first value is fixed. There is no escaping it. 
        table[0][0] = grid[0][0]
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # we have already taken care of this case.
                if i == 0 and j == 0:
                    continue
                table[i][j] = min(get_left(i, j, table), get_top(i, j, table)) + grid[i][j]
        
        return table[-1][-1]
