from itertools import accumulate
import sys

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """Sliding window.
        
        Idea:
        find target as total sum of array minus x (sum to be removed from array)
        search for target (for total max length sum to be left in then array)
        sliding window with two pointers:
        * right pointer increases current sum
        * left pointer decreases current sum (if it's bigger than target)
        
        Kadane's algorithm
        
        Time: O(n)
        Space: O(1)
        
        Algorithm:
        1. Calculate largest sum to find as difference of total sum and x
        2. If target is less than 0 then it's impossible to collect x even removing all items from array
        3. If target is 0 then return lenght of array (to collect x all items from array need to be removed)
        4. Accumulate array number:
            + if current sum became greater than target
                move leftmost pointer and decrease current sum
                until it becomes less than target or 0 (when pointers are equal)
            + if current sum is equal to target
        """
        
        current_sum = 0
        # target sum to be left in array
        target = sum(nums) - x

        if target < 0:
            return -1

        n = len(nums)
        if target == 0:
            return n
        
        left = 0
        res = sys.maxsize
        
        for right, num in enumerate(nums):
            # accumutale current sum
            current_sum += num
            
            # if current sum became greater than target
            # move leftmost pointer and decrease current sum
            # until it becomes less than target or 0 (when pointers are equal)
            while left <= right and current_sum > target:
                current_sum -= nums[left]
                left += 1

            # if current sum is equal to target 
            # calculate result
            if current_sum == target:
                res = min(res, n - (right - left + 1))

        return -1 if res == sys.maxsize else res