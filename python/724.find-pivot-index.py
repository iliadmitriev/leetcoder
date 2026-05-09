class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums[i] for i in range(1, len(nums)))

        if left == right:
            return 0

        for i in range(1, len(nums)):
            left += nums[i - 1]
            right -= nums[i]

            if left == right:
                return i

        return -1
        