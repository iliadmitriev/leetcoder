from functools import lru_cache


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        @lru_cache
        def dfs(i: int) -> int:
            if i >= len(questions):
                return 0

            # leave
            res = dfs(i + 1)

            # take
            res = max(res, questions[i][0] + dfs(i + questions[i][1] + 1))

            return res

        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if i + questions[i][1] + 1 < n:
                dp[i] = max(dp[i + 1], questions[i][0] + dp[i + questions[i][1] + 1])
            else:
                dp[i] = max(dp[i + 1], questions[i][0])

        return dp[0]

