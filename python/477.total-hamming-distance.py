from itertools import combinations

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        # iterate all 32 bit positions
        for current_bits in zip(*map('{:032b}'.format, nums)):
            # get count of 1's from current tuple of bits
            count = current_bits.count('1')
            # if for current bit position all bits are equal to 1 for all numbers,
            # then count == n, and n - count == 0
            # and if all bits are equal to 0 for all numbers,
            # then count == 0 
            # so this contributes 0 differences to final result
            res += count * (n - count)
        return res