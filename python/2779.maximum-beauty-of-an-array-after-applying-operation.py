class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        maxLen = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen

