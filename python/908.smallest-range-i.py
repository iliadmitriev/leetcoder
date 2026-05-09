class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        _min, _max = min(nums) + k, max(nums) - k

        return max(0, _max - _min)

