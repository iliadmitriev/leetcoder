class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = max(nums[i], f[i] * nums[i], g[i] * nums[i])
            g[i + 1] = min(nums[i], g[i] * nums[i], f[i] * nums[i])
        return max(f)
