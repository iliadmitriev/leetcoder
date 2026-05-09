from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left, right = 1, 1

        for i in range(n):

            res[i] *= left
            res[n - i - 1] *= right

            left *= nums[i]
            right *= nums[n - i - 1]

        return res

