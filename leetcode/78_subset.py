class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Helper functions
        ##################################
        
        def find_subsets(nums, sol_list, current_list, i):
            sol_list.append(current_list[:])
            for idx in range(i, len(nums)):
                current_list.append(nums[idx])
                find_subsets(nums, sol_list, current_list, idx+1)
                current_list.pop()
        ##################################
        
        # base conditions
        if not nums:
            return []
        
        sol_list = []
        find_subsets(nums, sol_list, [], 0)
        return sol_list
