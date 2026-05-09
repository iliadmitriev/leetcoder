from collections import defaultdict
from bisect import bisect_left

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # calculate all the text2 letters positions to dict
        d = defaultdict(list)
        for idx, char in enumerate(text2):
            d[char].append(idx)

        # result indexes
        res = []
        for char in text1:
            if char in d:
                for idx in reversed(d[char]):
                    i = bisect_left(res, idx)

                    if i == len(res):
                        res.append(idx)
                    else:
                        res[i] = idx

        return len(res)