from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res: list[list[int]] = [[]]

        for num in nums:
            res += [r + [num] for r in res]

        return res

