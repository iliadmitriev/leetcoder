

import collections


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        res = 0

        freq = collections.Counter(nums)
        for k in freq.keys():
            if k + 1 in freq:
                res = max(res, freq[k] + freq[k + 1])

        return res

