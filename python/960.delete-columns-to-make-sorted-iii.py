class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        COLS = len(strs[0])

        dp = [1] * COLS

        for i in range(1, COLS):
            for j in range(i):
                order = True
                for row in strs:
                    if row[j] > row[i]:
                        order = False
                        break

                if order:
                    dp[i] = max(dp[i], dp[j] + 1)

        return COLS - max(dp)

