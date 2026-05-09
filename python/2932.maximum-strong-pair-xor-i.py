class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()

        res = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] > nums[i] * 2:
                    break
                res = max(res, nums[i] ^ nums[j])

        return res

