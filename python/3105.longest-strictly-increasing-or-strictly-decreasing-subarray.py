class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc, dec = 1, 1
        logest = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dec += 1
                inc = 1
            elif nums[i] < nums[i - 1]:
                inc += 1
                dec = 1
            else:
                inc = dec = 1

            logest = max(logest, inc, dec)

        return logest

