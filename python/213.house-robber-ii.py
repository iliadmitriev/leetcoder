class Solution:
    def rob(self, nums: List[int]) -> int:
        """Calculate maximum profit

        - Time: O(n)
        - Space: O(1) - for storing f(k-2) and f(k-1)

        * f(0) = nums[0]
        * f(1) = max(nums[0], nums[1])
        * f(2) = max(nums[2] + nums[0], nums[1])
        * ...
        * f(k) = max(f(k-2) + nums[k], f(k-1))

        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]

        def dp(arr: List[int]) -> int:
            profit, prev = 0, 0
            for num in arr:
                profit, prev = max(num + prev, profit), profit
            return profit
                    
        return max(dp(nums[1:]), dp(nums[:-1]))
