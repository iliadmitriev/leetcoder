class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        minAvg = float("inf")
        n = len(nums)
        nums.sort()

        for i in range(n // 2):
            minAvg = min(minAvg, (nums[i] + nums[n - i - 1]) / 2)

        return minAvg

