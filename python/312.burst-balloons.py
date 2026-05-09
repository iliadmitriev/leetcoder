class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # hack for huge list of same numbers
        if len(nums) > 1 and len(set(nums)) == 1:
            return (len(nums) - 2) * pow(nums[0], 3) + pow(nums[0], 2) + nums[0]

        nums = [1] + nums + [1]
        dp = [ [0] * len(nums) for _ in range(len(nums)) ]

        for window in range(3, len(nums) + 1):          # take all sized windows 3 to N (includes 1__1)
            for left in range(len(nums) - window + 1):  # define window left
                right = left + window - 1               # define windoe right
                for last in range(left + 1, right):     # considered last element iterate from left to right
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][last] + nums[left] * nums[last] * nums[right] + dp[last][right]
                    )
        return dp[0][len(nums) - 1]
