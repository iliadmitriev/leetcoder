from itertools import accumulate


class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:

        return sum(pos == 0 for pos in accumulate(nums))

