class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        n = len(nums)

        count = 0

        i, j = 0, 1

        for k in range(2, n):
            if nums[j] == nums[k]:
                continue

            if nums[i] < nums[j] > nums[k]:
                count += 1

            elif nums[i] > nums[j] < nums[k]:
                count += 1

            i = j
            j = k

        return count

