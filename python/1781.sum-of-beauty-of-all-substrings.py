from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for l in range(len(s) - 2):
            for r in range(l + 3, len(s) + 1):
                z = Counter(s[l:r])
                res += max(z.values()) - min(z.values())
        return res