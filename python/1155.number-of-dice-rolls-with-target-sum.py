MOD = 10**9 + 7

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        if target < n or target > n * k:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(target + 1)]
        dp[0][0] = 1

        for x in range(1, n + 1):
            for t in range(target, -1, -1):
                for i in range(1, k + 1):
                    if t >= i:
                        dp[t][x] += dp[t - i][x - 1] 
                    dp[t][x] %= MOD                    
                
        return dp[target][n]