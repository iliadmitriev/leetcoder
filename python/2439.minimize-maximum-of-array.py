class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result, current_sum = 0, 0
        for i, num in enumerate(nums):
            current_sum += num
            result = max(result, (current_sum + i) // (i + 1))
        return result