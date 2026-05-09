class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        prefix = [0] * n

        for left, right in queries:
            prefix[left] += 1
            if right + 1 < n:
                prefix[right + 1] -= 1

        cur = 0
        for num, diff in zip(nums, prefix):
            cur += diff

            if cur < num:
                return False

        return True

