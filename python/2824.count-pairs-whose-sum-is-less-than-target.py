class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        count = 0
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] < target:
                count += j - i
                i += 1
            else:
                j -= 1

        return count

