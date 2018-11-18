'''

I think we all know what this problem is. 
'''

def three_sum(arr):
    if not nums:
        return []
    result = []
    nums.sort()
    for i in range(0, len(nums)-2):
        target = -nums[i]
        left = i+1
        right = len(nums)-1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while left < right:
            if nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right:
                    if nums[left] != nums[left-1]:
                        break
                    left += 1
                while left < right:
                    if nums[right] != nums[right+1]:
                        break
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    return result