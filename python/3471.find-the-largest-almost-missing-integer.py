class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)

        c = Counter(nums)

        if k == 1:
            return max((nums[i] for i in range(n) if c[nums[i]] == 1), default=-1)

        c1 = nums[0]
        c2 = nums[-1]

        if c1 == c2:
            return -1

        if c[c1] == 1 and c[c2] == 1:
            return max(c1, c2)

        if c[c1] == 1:
            return c1

        if c[c2] == 1:
            return c2

        return -1    