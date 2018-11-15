'''
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2


'''
def leastBricks(self, wall):
    from collections import defaultdict
    
    if not wall or not wall[0]:
        return 0
    
    sum_freq = defaultdict(int)
    
    for row in wall:
        curr_sum = 0
        for i in range(0, len(row)-1):
            curr_sum += row[i]
            sum_freq[curr_sum] += 1
    
    sum_freq = sorted(sum_freq.items(), key=lambda x: x[1])
    most_freq = sum_freq[-1][1] if sum_freq else 0
    
    
    crosses = len(wall) - most_freq
            
    return crosses
        
        
        
        
