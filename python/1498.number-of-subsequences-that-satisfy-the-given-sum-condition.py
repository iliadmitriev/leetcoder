

class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        total = 0

        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] <= target:
                total += pow(2, j - i, mod)
                i += 1
            else:
                j -= 1

        return total % mod

