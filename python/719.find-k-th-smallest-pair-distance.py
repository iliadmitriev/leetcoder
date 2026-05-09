import bisect


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        lo, hi = 0, nums[n - 1] - nums[0] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.count_pairs2(nums, mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def count_pairs(self, nums: list[int], d: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 1):
            j = bisect.bisect_left(nums, nums[i] + d)
            count += j - i - 1
        return count

    def count_pairs2(self, nums: list[int], d: int) -> int:
        n = len(nums)
        count = 0
        left = 0
        for right in range(1, n):
            while left < right and nums[right] - nums[left] > d:
                left += 1

            count += right - left
        return count

