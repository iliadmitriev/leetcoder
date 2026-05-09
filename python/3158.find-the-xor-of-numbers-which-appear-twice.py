

class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:

        res = 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                res ^= nums[i]

        return res

