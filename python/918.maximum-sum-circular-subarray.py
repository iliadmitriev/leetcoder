class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_subarray = -inf
        min_subarray = inf
        max_curr, min_curr = 0, 0
        total = 0
        for num in nums:
            total += num

            max_curr = max(num, num + max_curr)
            max_subarray = max(max_subarray, max_curr)

            min_curr = min(num, num + min_curr)
            min_subarray = min(min_subarray, min_curr)

        if max_subarray < 0:
            return max_subarray
        else:
            return max(max_subarray, total - min_subarray)