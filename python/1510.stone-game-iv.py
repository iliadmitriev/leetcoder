class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        Idea:
        
        - dfs(remainder) - recurrent function, which returns 
         if the current player with current remaining stones can loose.
        - it iterates from 1 to sqrt(remainder),
        trying to get if there is any chance of opponent to have loosing strategy
        if there is we return our strategy as winning (True)
        otherwise return False
        
        """
        
        @lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return False
            
            return any(not dfs(remain - j * j) for j in range(int(remain**0.5), 0, -1))
    
        return dfs(n)