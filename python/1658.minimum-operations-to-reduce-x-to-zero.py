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
        target = sum(nums) - x

        # optimization #1
        if target < 0:
            return -1

        # optimization #2
        if target == 0:
            return len(nums)

        count = 0
        total = 0
        left = 0
        res = float("inf")

        for right in range(len(nums)):
            # increase cout and total from right border
            total += nums[right]
            count += 1
            
            # reduce count and total from left border
            while left <= right and total > target:
                total -= nums[left]
                count -= 1
                left += 1

            if total == target:
                length = len(nums) - (right - left + 1)
                res = min(res, length)

        return -1 if res == float("inf") else res
