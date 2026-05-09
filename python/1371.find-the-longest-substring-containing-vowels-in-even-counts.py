class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        countsMask: int = 0
        maskPos = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}

        maxLen = 0
        cache: dict[int, int] = {0: -1}

        for i in range(len(s)):
            if s[i] in maskPos:
                countsMask ^= 1 << maskPos[s[i]]

            if countsMask in cache:
                maxLen = max(maxLen, i - cache[countsMask])
            else:
                cache[countsMask] = i

        return maxLen

