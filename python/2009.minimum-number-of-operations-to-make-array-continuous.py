class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        res = 0

        left = 0
        for right, _ in enumerate(nums):
            if nums[right] - nums[left] >= length:
                left += 1
            window = right - left + 1
            res = max(res, window)

        return length - res