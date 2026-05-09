class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        longest = 0
        n = len(nums)
        left = 0
        zeroes = 0

        for right in range(n):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1

                left += 1

            longest = max(longest, right - left)

        return longest

