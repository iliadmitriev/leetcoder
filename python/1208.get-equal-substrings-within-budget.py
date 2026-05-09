class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        i = 0

        maxSub = 0
        curCost = 0

        for j in range(n):
            curCost += abs(ord(s[j]) - ord(t[j]))

            while curCost > maxCost and i < n:
                curCost -= abs(ord(s[i]) - ord(t[i]))
                i += 1

            maxSub = max(maxSub, j - i + 1)

        return maxSub

