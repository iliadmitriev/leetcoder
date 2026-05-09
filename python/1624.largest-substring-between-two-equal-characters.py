class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cache = {}
        res = -1
        for r, ch in enumerate(s):
            if ch in cache:
                res = max(res, r - cache[ch] - 1)
            else:
                cache[ch] = r
        return res