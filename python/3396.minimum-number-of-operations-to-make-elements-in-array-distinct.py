class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count = [0] * 101
        n = len(nums)

        for i in range(n - 1, -1, -1):
            count[nums[i]] += 1
            if count[nums[i]] == 2:
                return i // 3 + 1

        return 0

