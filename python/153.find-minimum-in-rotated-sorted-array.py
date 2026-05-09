class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[hi] > nums[mid]:
                hi = mid
            elif nums[hi] < nums[mid]:
                lo = mid + 1

        return nums[lo]