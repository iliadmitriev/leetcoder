class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        first = max(nums)

        return k * first + k * (k - 1) // 2

