class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        lo, hi = 0, n - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1

        return lo
