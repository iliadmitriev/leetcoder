class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        for i, num in enumerate(nums, start=1):
            res += num**2 * (n % i == 0)

        return res

