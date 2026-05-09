class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        maxRepeat = 0
        dp = [0] * (n + 1)

        for i in range(m, n + 1):
            if sequence[i - m : i] == word:
                dp[i] = dp[i - m] + 1
                maxRepeat = max(maxRepeat, dp[i])

        return maxRepeat

