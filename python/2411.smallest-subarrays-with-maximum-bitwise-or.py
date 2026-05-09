class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(n):
            j = i - 1
            v = nums[i]

            while j >= 0 and (v | nums[j]) != nums[j]:
                ans[j] = i - j + 1
                nums[j] |= v
                j -= 1

        return ans

