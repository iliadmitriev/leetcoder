class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        vmax = [nums[0]] * n
        for i in range(1, n):
            vmax[i] = max(vmax[i - 1], nums[i])

        vmin = [nums[n - 1]] * n
        for i in range(n - 2, -1, -1):
            vmin[i] = min(vmin[i + 1], nums[i])

        for i in range(len(nums)):
            if vmax[i] - vmin[i] <= k:
                return i

        return -1
        