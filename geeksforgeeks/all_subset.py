'''
https://www.geeksforgeeks.org/print-sums-subsets-given-set/
'''

def find_subsets(nums):

    def helper(nums, subsets, current):
        subsets.append(current[:])
        for i in range(0, len(nums)):
            current.append(nums[i])
            helper(nums[i+1:], subsets, current)
            current.pop()
        

    if not nums:
        return []
    if len(nums) == 1:
        return [[], nums]
    
    subsets = []
    current = []
    helper(nums, subsets, current)
    return subsets

nums = [1, 2, 3]
print(find_subsets(nums))
