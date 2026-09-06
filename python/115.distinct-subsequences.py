class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 1: we use only the letters that met in the target
        tset = set(t)
        s = "".join(ch for ch in s if ch in tset)

        m, n = len(s), len(t)

        # 2: if given source is shorter than the target
        if m < n:
            return 0

        @cache
        def dfs(i: int, j: int) -> int:
            if j == n:
                return 1

            if i == m:
                return 0

            # 3: there is not enough symbols left to build the target
            if m - i < n - j:
                return 0

            res = 0

            # take (only if match)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)

            # skip
            res += dfs(i + 1, j)

            return res

        # return dfs(0, 0)

        dp = [0] * n + [1] # last base case
        for i in range(m - 1, -1, -1):
            start = max(0, i - m + n)
            end = min(n, i + 1)
            for j in range(start, end):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]

        return dp[0]
