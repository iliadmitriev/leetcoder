

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)

        code: dict[str, list[int]] = {}
        for i, r in enumerate(ring):
            code.setdefault(r, []).append(i)

        dp = [[10**9] * (n + 1) for _ in range(m + 1)]
        for j in range(n):
            dp[m][j] = 0

        # bottom up approach
        for i in range(m - 1, -1, -1):
            codes = range(n) if i == 0 else code[key[i - 1]]
            for k in codes:
                for j in code[key[i]]:
                    step = 1 + min(abs(k - j), n - abs(k - j))
                    dp[i][k] = min(dp[i][k], step + dp[i + 1][j])

        return dp[0][0]

