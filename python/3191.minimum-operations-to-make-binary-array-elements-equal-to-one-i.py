class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ops = 0

        for i in range(len(nums) - 2):
            if nums[i] == 1:
                continue

            ops += 1
            for j in range(i, i + 3):
                nums[j] = 1 - nums[j]

        if nums[-2:] == [1, 1]:
            return ops

        return -1

