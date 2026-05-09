from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        return [s := s + v for v in nums]
