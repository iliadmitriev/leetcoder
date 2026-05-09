class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        mask = (1 << 32) - 1
        left = 0
        maxLen = 1

        for right in range(len(nums)):
            mask ^= nums[right]

            while mask & nums[right]:
                mask ^= nums[left]
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen

