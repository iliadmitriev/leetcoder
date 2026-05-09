class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        
        Idea:
        Run Loop:
        1) calculate diff between all adjacent elements
        2) check if difference and previous difference match, then increase count
            otherwise, reset count and set previous difference
        3) add count to result
        """
        cnt, res = 0, 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cnt += 1
                res += cnt
            else:
                cnt = 0
        
        return res
        