import operator
from functools import reduce

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        xor = 0

        # find `xor` - both numbers repeated and missing
        for i, n in enumerate(nums, 1):
            xor ^= i ^ n

        # get the rightmost different bit for both repeated and missing
        # there should be such bit (the numbers is different)
        rightmost = xor & ~(xor - 1)

        # xor0, xor1 - repeated and missing number separated by rightmost different bit
        # can't tell definatelly which of xor0, xor1 is missing and lost
        xor0, xor1 = 0, 0
        for i, n in enumerate(nums, 1):
            if n & rightmost:
                xor1 ^= n
            else:
                xor0 ^= n

            if i & rightmost:
                xor1 ^= i
            else:
                xor0 ^= i

        # if xor0 - is repeated number (present in original set)
        # then xor1 - is missing
        if xor0 in nums:
            return [xor0, xor1]
        return [xor1, xor0]

