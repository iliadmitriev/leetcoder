class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        longest = 0
        count = 0
        prev = -1

        for num in nums:
            if num == prev:
                count += 1
                if count > longest:
                    longest = count
            elif num > prev:
                prev = num
                count = 1
                longest = 1
            else:
                count = 0

        return longest

