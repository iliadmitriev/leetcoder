class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n

        dp[n - 1] = 0  # base case

        for j in range(n - 1, -1, -1):
            if dp[j] < 0:  # not connected
                continue

            for i in range(j - 1, -1, -1):
                if abs(nums[i] - nums[j]) > target:
                    continue

                dp[i] = max(dp[i], dp[j] + 1)

        return dp[0]
