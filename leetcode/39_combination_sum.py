class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        def helper(candidates, target, sol_list, current_list, last):
            if target == 0:
                sol_list.append(current_list[:])
                return True
            if target < 0:
                return False
            for idx in range(last, len(candidates)):
                value = candidates[idx]
                current_list.append(value)
                if not helper(candidates, target-value, sol_list, current_list, idx):
                    current_list.pop()
                    break
                current_list.pop()
            return True
        
        sol_list = []
        candidates.sort()
        helper(candidates, target, sol_list, [], 0)
        return sol_list
