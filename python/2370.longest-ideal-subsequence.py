class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        if k >= 25:
            return len(s)

        n = len(s)
        dp = [0] * (26)

        for i in range(n):
            cur = ord(s[i]) - 97
            dp[cur] = 1 + max(
                dp[prev] for prev in range(max(0, cur - k), min(cur + k, 25) + 1)
            )

        return max(dp)

