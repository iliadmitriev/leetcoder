class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        res = []
        prev = -1

        for i, group in enumerate(groups):
            if group != prev:
                res.append(words[i])
                prev = group

        return res

