class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        def getConsecutiveLength(num: int, lookup, alreadyChecked):
            
            if num in alreadyChecked:
                return 0
            
            alreadyChecked.add(num)
            
            if num not in lookup:
                return 0
            return 1 + getConsecutiveLength(num+1, lookup, alreadyChecked) \
                     + getConsecutiveLength(num-1, lookup, alreadyChecked)

        
        lookup = set(nums)
        alreadyChecked = set()
        currentCounter = 0
        maxCounter = 0
        for num in nums:
            maxCounter = max(maxCounter, getConsecutiveLength(num, lookup, alreadyChecked))
        
        return maxCounter
            
