class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * (len(nums) + 2)

        for i in range(len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[len(nums) - 1]