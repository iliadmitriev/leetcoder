class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n

        res[0] = nums[0]
        for i in range(n):
            res[i] = nums[nums[i]]

        return res

