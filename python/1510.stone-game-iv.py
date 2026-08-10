class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        s = int(n ** 0.5)
        for i in range(n + 1):
            if dp[i]:
                continue # cache

            for k in range(1, s + 1):
                if i + k * k <= n:
                    dp[i + k * k] = True
                else:
                    break

        return dp[n]
        