class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        total = 0

        cur = -1
        curLen = 0

        for i in range(len(nums)):
            if cur != nums[i]:
                curLen += 1
            else:
                curLen = 1

            total += curLen
            cur = nums[i]

        return total

