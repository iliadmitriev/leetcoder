class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:

        cur = 0
        res = [False] * len(nums)

        for i in range(len(nums)):
            cur = (cur * 2 + nums[i]) % 5
            res[i] = cur == 0

        return res

