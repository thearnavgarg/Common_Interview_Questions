class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if sum(nums) < s:
            return 0
        
        front = 0
        back = 0
        cs = 0
        min_size = float('inf')
        
        '''
        [1, 4, 4]
        4
        '''
        
        while front < len(nums):
            # add the new front element to the sum
            cs += nums[front]
            
            # if the new sum is less than s, then increase the front and continue with the loop
            if cs >= s:
                while cs >= s and back <= front:
                    cs -= nums[back]
                    back += 1
                back -= 1
                cs += nums[back]
                min_size = min(min_size, front-back+1)
            
            front += 1
        
        min_size = min(min_size, front-back+1)
        return min_size
