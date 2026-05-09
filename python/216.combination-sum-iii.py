class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def dfs(num, count, total, comb):
            if total == 0 and count == 0:
                res.append(comb)
                return
            
            if total == 0 or count == 0 or num > 9:
                return
            
            if total >= num and count > 0:

                dfs(num + 1, count - 1, total - num, comb + [num])
                dfs(num + 1, count, total, comb)
        
        
        dfs(1, k, n, [])
        
        return res