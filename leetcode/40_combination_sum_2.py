class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
    
        def find_solutions(sol_list, candidates, target, current_list, idx):
            if target == 0:
                if current_list not in sol_list:
                    sol_list.append(current_list[:])
                return True
            if target < 0:
                return False
            for i in range(idx, len(candidates)):
                # if i > 0 and candidates[i] == candidates[i-1]:
                #     continue
                current_list.append(candidates[i])
                if not find_solutions(sol_list, candidates, target - candidates[i], current_list, i+1):
                    current_list.pop()
                    break
                current_list.pop()
            return True
        
        sol_list = []
        candidates.sort()
        find_solutions(sol_list, candidates, target, [], 0)
        return sol_list
