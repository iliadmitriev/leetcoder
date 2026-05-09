

import bisect
import collections


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        nums.sort()

        cnt = collections.Counter(nums)
        max_freq = 0

        for i, num in enumerate(nums):
            left = bisect.bisect_left(nums, num - k)
            right = bisect.bisect_right(nums, num + k)

            # first candidate
            window = right - left - cnt[num]
            candidate1 = cnt[num] + min(window, numOperations)

            # second candidate
            nxt = bisect.bisect_right(nums, num + 2 * k)
            nums_next = nxt - i
            candidate2 = min(nums_next, numOperations)

            max_freq = max(max_freq, candidate1, candidate2)

        return max_freq

