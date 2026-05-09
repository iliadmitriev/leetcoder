class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        maxItem, minItem = max(nums), min(nums)
        for num in nums:
            if minItem < num < maxItem:
                return num

        return -1

