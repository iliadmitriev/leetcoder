class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        i, j = 0, 0
        total, curSum = 0, 0

        for j in range(n):
            curSum += nums[j]

            while i <= j and curSum * (j - i + 1) >= k:
                curSum -= nums[i]
                i += 1

            total += j - i + 1

        return total

