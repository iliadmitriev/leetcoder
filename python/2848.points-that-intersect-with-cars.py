class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        nums.sort()

        holes = 0
        minInt = nums[0][0]
        maxInt = nums[0][1]

        for i in range(1, len(nums)):
            if maxInt < nums[i][0]:
                holes += nums[i][0] - maxInt - 1

            maxInt = max(maxInt, nums[i][1])

        return maxInt - minInt + 1 - holes

