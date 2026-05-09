import itertools


class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        cur, prev = 1, 0
        maxLen = 0

        for n1, n2 in itertools.pairwise(nums):
            if n1 < n2:
                cur += 1
            else:
                prev = cur
                cur = 1

            maxLen = max(maxLen, min(prev, cur), cur // 2)

        return maxLen

