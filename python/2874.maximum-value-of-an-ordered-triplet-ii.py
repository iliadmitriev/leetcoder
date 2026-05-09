class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        result = 0
        prefix, diff = 0, 0

        for num in nums:
            result = max(result, diff * num)
            prefix = max(prefix, num)
            diff = max(diff, prefix - num)

        return result

