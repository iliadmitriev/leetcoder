class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []
        
        def dp(index: int, target: int) -> List[List[int]]:
            """
            curr - current combination
            index - where to start combinations (for eliminating duplicates)
            target - total target amount
            """            
            if target == 0:
                res.append(curr.copy())
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                if target >= num:
                    curr.append(num)
                    dp(i, target - num)
                    curr.pop()
                # since list is sorted, we can break 
                # after we met candidate that is bigger than target
                else:
                    break
                    
        dp(0, target)
        
        return res