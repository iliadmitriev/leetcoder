class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        maxLen = 0

        for word in strs:
            curLen = int(word) if word.isdigit() else len(word)

            maxLen = max(maxLen, curLen)

        return maxLen

