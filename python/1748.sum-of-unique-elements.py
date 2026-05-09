from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        count = Counter(nums)

        return sum(x for x in nums if count[x] == 1)

