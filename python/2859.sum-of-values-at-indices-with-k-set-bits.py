class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total = 0

        def bit_count(n: int) -> int:
            return bin(n).count("1")

        for i, num in enumerate(nums):
            if bit_count(i) == k:
                total += num

        return total

