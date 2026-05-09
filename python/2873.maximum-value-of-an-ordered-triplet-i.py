class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], nums[i])

        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], nums[i])

        for i in range(1, n - 1):
            result = max(result, (prefix[i - 1] - nums[i]) * suffix[i + 1])

        return result

