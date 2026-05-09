class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        total = 0

        for i in range(1, len(nums) - 1):
            if 2 * (nums[i - 1] + nums[i + 1]) == nums[i]:
                total += 1

        return total

