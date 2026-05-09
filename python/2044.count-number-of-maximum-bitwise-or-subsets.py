class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        maxVal = 0  # max or subset

        for num in nums:
            maxVal |= num

        def bt(i: int, mask: int) -> int:
            if i == len(nums):
                if mask == maxVal:
                    return 1
                return 0

            return bt(i + 1, mask | nums[i]) + bt(i + 1, mask)

        return bt(0, 0)

