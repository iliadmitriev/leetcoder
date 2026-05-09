class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        ramp = 0

        i, j = 0, 0
        n = len(nums)

        prefixMax = [0] * n
        curMax = nums[n - 1]

        for i in range(n - 1, -1, -1):
            curMax = max(curMax, nums[i])
            prefixMax[i] = curMax

        j = 0

        for i in range(n):
            if nums[i] > prefixMax[i]:
                continue

            while j < n and nums[i] <= prefixMax[j]:
                j += 1

            ramp = max(ramp, j - i - 1)

        return ramp

