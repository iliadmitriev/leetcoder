import bisect
import collections


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        limit = len(nums)

        nums.sort()

        cnt = collections.Counter(nums)

        mmin = nums[0]
        mmax = nums[-1]
        maxFreq = 0

        for num in range(mmin, mmax + 1):
            right = bisect.bisect_right(nums, num + k)
            left = bisect.bisect_left(nums, num - k)

            total = right - left - cnt[num]

            maxFreq = max(maxFreq, cnt[num] + min(numOperations, total))

            if maxFreq == limit:
                return limit

        return maxFreq

