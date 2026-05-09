class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        minA, minB = nums[1], nums[2]
        if minA > minB:
            minA, minB = minB, minA

        for i in range(3, len(nums)):
            if nums[i] < minA:
                minB = minA
                minA = nums[i]
            elif nums[i] == minA or nums[i] < minB:
                minB = nums[i]

        return nums[0] + minA + minB

