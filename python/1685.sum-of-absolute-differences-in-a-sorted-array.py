from itertools import accumulate


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
            suffix[n - i] = suffix[n - i + 1] + nums[n - i]

        for i in range(n):
            res[i] = i * nums[i] - prefix[i] + suffix[i] - (n - i) * nums[i]

        return res