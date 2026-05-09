import bisect


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        shift = 0
        ops = 0
        nums.sort()
        start = bisect.bisect_left(nums, 1)

        for i in range(start, len(nums)):
            if nums[i] - shift > 0:
                shift = nums[i]
                ops += 1

        return ops

