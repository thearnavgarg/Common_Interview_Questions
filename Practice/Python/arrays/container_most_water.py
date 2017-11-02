''' 
Given n non-negative integers a1, a2, ..., an, where each represents a
point at coordinate (i, ai). n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most
water.

Note: You may not slant the container and n is at least 2.
'''

def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """ 
    start = 0
    end = len(height)-1
    max_water = 0
    while(start < end):
        if min(height[start], height[end])*(end-start) > max_water:
            max_water = min(height[start], height[end])*(end-start)
        elif height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return max_water
