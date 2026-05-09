class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        INF = 10**15
        prefixMin = [INF] * k
        prefixMin[-1] = 0

        cur = 0
        res = -INF

        for i, num in enumerate(nums):
            cur += num

            old = prefixMin[i % k]

            prefixMin[i % k] = min(cur, old)
            res = max(res, cur - old)

        return res

