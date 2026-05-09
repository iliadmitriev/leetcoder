class Solution:
    def maxScore(self, s: str) -> int:
        curScore, maxScore = 0, 0
        left, right = 0, s.count("1")

        for i in range(0, len(s) - 1):
            if s[i] == "0":
                left += 1
            else:
                right -= 1

            curScore = left + right
            maxScore = max(maxScore, curScore)

        return maxScore
