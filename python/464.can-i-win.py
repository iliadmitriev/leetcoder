class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        Time: O(n * 2^n)
        Space: O(2^n)
        n = maxChoosableInteger
        
        """
        if desiredTotal == 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        
        cache = [0] * ((1 << maxChoosableInteger + 1) - 1)

        def dfs(used: int, target: int) -> bool:
            if cache[used] != 0: # 0: None
                return cache[used] == 1 # 1: True, -1: False 

            if target <= 0:
                cache[used] = -1
                return False
            
            for i in range(1, maxChoosableInteger + 1):
                mask = 1 << i
                if not used & mask:
                    if not dfs(used ^ mask, target - i):
                        cache[used] = 1
                        return True
            
            cache[used] = -1
            return False
        
        return dfs(0, desiredTotal)
