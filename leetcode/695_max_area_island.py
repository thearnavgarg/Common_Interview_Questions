'''
Given a non-empty 2D array grid of 0's and 1's, an island 
is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the grid 
are surrounded by water.

Find the maximum area of an island in the given 2D array. 
(If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, 
because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(grid, i, j):
            if i >= len(grid) or i < 0 or \
               j >= len(grid[0]) or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return dfs(grid, i+1, j) + \
                   dfs(grid, i-1, j) + \
                   dfs(grid, i, j+1) + \
                   dfs(grid, i, j-1) + 1
        
        if not grid or not grid[0]:
            return 0
    
        area = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, dfs(grid,i,j))
        return area