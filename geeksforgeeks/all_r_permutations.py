'''
https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
'''

def permutations(nums, r):

    def helper(nums, r, perm, current):
        if r == 0:
            perm.append(current[:])
            return
        for i in range(0, len(nums)):
            current.append(nums[i])
            helper(nums[i+1:], r-1, perm, current)
            current.pop()
        return

    if not nums:
        return []
    if r > len(nums):
        return []
    if r == len(nums):
        return [nums]
    
    perm = []
    current = []
    helper(nums, r, perm, current)
    return perm

nums = [1, 2, 3, 4, 5]
r = 3
print(permutations(nums, r))