class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max1, max2 = nums[0], nums[1]
        max1_idx = 0

        if max1 < max2:
            max1, max2 = max2, max1
            max1_idx = 1

        for i in range(2, len(nums)):
            if max1 < nums[i]:
                max1, max2 = nums[i], max1
                max1_idx = i
            elif max2 < nums[i]:
                max2 = nums[i]

        if max1 >= max2 * 2:
            return max1_idx

        return -1

