class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            res ^= nums[i] ^ i
        return res ^ n

