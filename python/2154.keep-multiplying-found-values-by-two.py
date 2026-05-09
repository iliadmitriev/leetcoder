class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums.sort()

        for num in nums:
            if num == original:
                original *= 2

        return original

