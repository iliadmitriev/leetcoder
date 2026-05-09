class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        zeros = nums.count(0)
        nums = [num for num in nums if num]

        cache = {}

        def dfs(i: int, value: int, nums: list[int], target: int) -> int:
            if i == len(nums):
                return int(value == target)

            if (i, value) in cache:
                return cache[(i, value)]

            res = dfs(i + 1, value + nums[i], nums, target)
            res += dfs(i + 1, value - nums[i], nums, target)

            cache[(i, value)] = res
            return res

        return dfs(0, 0, nums, target) * (1 << zeros)

