class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        n = len(nums)
        child, dp = [-1] * n, [0] * n

        nums.sort()
        i_max = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        child[i] = j

                if dp[i] > dp[i_max]:
                    i_max = i

        ans = []
        i = i_max
        while i != -1:
            ans.append(nums[i])
            i = child[i]

        return ans

