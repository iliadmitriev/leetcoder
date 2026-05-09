class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        value = list(accumulate(stoneValue, initial=0))

        for pos in range(n, -1, -1):
            dp[pos] = max(
                (value[min(n, pos + step)] - value[pos] - dp[min(pos + step, n)] for step in (1, 2, 3)),
                default=0
            )
            
        res = dp[0]
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"
