class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        mul = 1
        
        for i in range(n // 2):
            res += nums[n - i - 1] * mul
            res += nums[i] * mul

            mul *= n - i - 1
            mul //= i + 1

            res %= 10
        
        # middle element is number of elements is odd
        if n % 2:
            res += nums[n // 2] * mul

        return res % 10
        