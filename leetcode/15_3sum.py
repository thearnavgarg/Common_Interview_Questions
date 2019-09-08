class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def getNewStartIndex(startIndex, nums):
            newStartIndex = startIndex+1
            while newStartIndex < len(nums) and \
                    nums[newStartIndex] == nums[startIndex]:
                newStartIndex += 1
            return newStartIndex
        
        def getNewEndIndex(endIndex, nums):
            newEndIndex = endIndex - 1
            while newEndIndex > -1 and \
                    nums[newEndIndex] == nums[endIndex]:
                newEndIndex -= 1
            return newEndIndex
        
        if len(nums) < 3:
            return []
        
        nums.sort()
        outputList = []
        # Main body of the alogrithm. 
        for i in range(0, len(nums)-2):
            # So we don't get repeating numbers in the 
            # outputList array. 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            fixedValue = nums[i]
            startIndex = i+1
            endIndex = len(nums)-1
            while startIndex < endIndex:
                firstValue = nums[startIndex]
                secondValue = nums[endIndex]
                currentSum = fixedValue + firstValue + secondValue
                if currentSum == 0:
                    outputList.append([fixedValue, firstValue, secondValue])
                    startIndex = getNewStartIndex(startIndex, nums)
                    endIndex = getNewEndIndex(endIndex, nums)
                elif currentSum > 0:
                    endIndex = getNewEndIndex(endIndex, nums)
                else:
                    startIndex = getNewStartIndex(startIndex, nums)
                    
        return outputList
