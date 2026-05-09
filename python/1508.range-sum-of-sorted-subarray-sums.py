class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        MOD = int(1e9 + 7)
        subSums: list[int] = []
        n = len(nums)

        for start in range(n):
            winSum = 0
            for i in range(start, n):
                winSum += nums[i]

                subSums.append(winSum)

        return sum(sorted(subSums)[left - 1: right]) % MOD

