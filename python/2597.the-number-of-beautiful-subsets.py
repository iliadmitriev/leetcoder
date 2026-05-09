from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def backtrack(i: int, subset: list[int]) -> int:
            if i >= n:
                return int(bool(subset))

            res = 0
            if (nums[i] - k) < 0 or (nums[i] - k) not in subset:
                subset.append(nums[i])
                res += backtrack(i + 1, subset)
                subset.pop()

            return res + backtrack(i + 1, subset)

        return backtrack(0, [])

