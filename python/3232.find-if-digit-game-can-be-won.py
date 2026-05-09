class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        single = sum(v for v in nums if v < 10)
        double = sum(v for v in nums if v >= 10)

        return single < double or single > double

