class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        [1, 1, 2, 2, 9, 9, 9] k = 5
        [1:2 2:2 9:3] k=14

          1*2 1*2, 7*2 7*3

        [1,1,2,2,9,9,9] 14
          0 1 1 7 7 7

        """
        nums.sort()
        n = len(nums)
        l = 0
        res = 0
        budget = k

        for r in range(n):
            budget += nums[r]
            # if overall budget is not enougth
            # to increase all values up to the rightmost value of sliding window
            # move left pointer
            if not budget >= nums[r] * (r - l + 1):
                budget -= nums[l]
                l += 1

            res = max(res, r - l + 1)
        
        return res