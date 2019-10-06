class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        [-1, 2, 2, 0]
        
        '''
        l_traversal = 1
        r_traversal = 1
        curr_max = nums[0]
        
        for i, val in enumerate(nums):
            l_traversal *= val
            curr_max = max(curr_max, l_traversal)
            if val == 0:
                l_traversal = 1
        
        for i, val in reversed(list(enumerate(nums))):
            r_traversal *= val
            curr_max = max(curr_max, r_traversal)
            if val == 0:
                r_traversal = 1
        
        return curr_max
