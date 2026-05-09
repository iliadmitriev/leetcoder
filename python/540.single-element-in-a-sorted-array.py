class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) >> 1
            mid -= mid & 1
            if mid + 1 < n and nums[mid] == nums[mid + 1]:
                left = mid + 2
            elif mid > 0 and nums[mid] == nums[mid - 1]:
                right = mid - 1
            else:
                return nums[mid]
