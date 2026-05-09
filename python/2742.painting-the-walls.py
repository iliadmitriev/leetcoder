class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        dp = [[inf] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0


        for i in range(n - 1, -1, -1):
            for left in range(1, n + 1):
                dp[i][left] = min(
                    cost[i] + dp[i + 1][max(0, left - 1 - time[i])],
                    dp[i + 1][left]
                )

        return dp[0][n]
