import math


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        total = 0

        for num in nums:
            if math.floor(math.log10(num) + 1) % 2 == 0:
                total += 1

        return total

