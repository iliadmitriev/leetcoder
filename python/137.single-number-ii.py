class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        ones_mask, twos_mask = ~ones, ~twos

        for num in nums:

            ones ^= num
            ones &= twos_mask
            ones_mask = ~ones

            twos ^= num
            twos &= ones_mask
            twos_mask = ~twos

        return ones