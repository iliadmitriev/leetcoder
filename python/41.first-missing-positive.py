from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # worst case: smallest positive number in
        # the list of n positive consecutive elements is n + 1
        # [1,2,3,4] -> 5
        # result is bounded between 1 and n + 1

        # get rid of negative numbers
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # mark existing elements as negative
        for i in range(len(nums)):
            num = abs(nums[i])

            if 1 <= num <= len(nums):
                if nums[num - 1] > 0:
                    nums[num - 1] *= -1
                elif nums[num - 1] == 0:
                    nums[num - 1] = -len(nums) - 1

        # run numbers from 1 to len(nums) inclusively
        # and find the first number than does not appear in the list
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1

