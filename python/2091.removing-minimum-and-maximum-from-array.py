class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        m, M = nums[0], nums[0]
        l, r = 0, 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] < m:
                l = i
                m = nums[i]

            if nums[i] > M:
                r = i
                M = nums[i]

        if l > r:
            l, r = r, l
        
        return min(l + 1 + n - r, r + 1, n - l)
        