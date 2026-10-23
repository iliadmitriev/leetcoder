class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        
        res = -1

        for i, num in enumerate(nums):
            if i == num:
                continue

            res &= num

        if res == -1:
            return 0

        return res
        