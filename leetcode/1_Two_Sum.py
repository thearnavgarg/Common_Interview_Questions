class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexLookup = {element: idx for idx, element in enumerate(nums)}
        
        for idx, num in enumerate(nums):
            element = target - num
            
            if element in indexLookup:
                if indexLookup[element] != idx:
                    return [idx, indexLookup[element]]
        return []
