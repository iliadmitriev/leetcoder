import itertools


class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        c = 1
        v = 0

        for prev, cur in itertools.pairwise(nums):
            if cur > prev:
                c += 1

            else:
                if (c >= k and v >= k) or (c >= 2 * k):
                    return True

                v = c
                c = 1

        if (c >= k and v >= k) or (c >= 2 * k):
            return True

        return False

