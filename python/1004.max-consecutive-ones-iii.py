class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i, j = 0, 0

        while j < n:

            k -= int(nums[j] == 0)

            if k < 0:
                k += int(nums[i] == 0)
                i += 1

            j += 1

        return j - i