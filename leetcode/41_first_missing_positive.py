class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x >= 0, nums))
        if not nums:
            return 1
        s_nums = set(nums)
        min_element = min(nums)
        element = 1
        while element in s_nums:
            element += 1
        return element
