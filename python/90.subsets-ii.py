from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        nums.sort()

        def backtrack(i: int, path: list[int]) -> None:
            res.append(path.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j - 1] == nums[j]:
                    continue

                path.append(nums[j])
                backtrack(j + 1, path)
                path.pop()

        backtrack(0, [])

        return res

