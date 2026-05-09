class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:

        n = len(nums)
        length, max_length = 1, 1

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                length += 1
            else:
                length = 1

            max_length = max(max_length, length)

        return max_length

