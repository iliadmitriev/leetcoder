class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        vmax = nums[0]  # single value only (running max prefix)
        vmin = [nums[n - 1]] * n

        for i in range(n - 2, -1, -1):
            vmin[i] = min(vmin[i + 1], nums[i])

        for i, v in enumerate(nums):
            vmax = max(vmax, v)

            if vmax - vmin[i] <= k:
                return i

        return -1
