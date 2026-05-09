class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        counter = 0

        for i in range(len(nums)):
            if nums[i] < k:
                counter += 1

        return counter

