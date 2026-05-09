class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for num in nums:
            ans |= num
        return ans << (n - 1)

