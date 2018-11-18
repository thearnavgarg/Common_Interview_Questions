def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    from collections import defaultdict
    
    if not nums:
        return []
    
    mapper = defaultdict(int)
    for i, num in enumerate(nums):
        other = target-num
        if other in mapper:
            return [mapper[other], i]
        mapper[num] = i
    return []