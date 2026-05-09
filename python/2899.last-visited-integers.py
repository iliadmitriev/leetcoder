from collections import deque


class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        ans, seen = [], deque()
        k = 0

        for i, v in enumerate(nums):
            if v > 0:
                seen.appendleft(v)
                k = 0
            else:

                if k < len(seen):
                    ans.append(seen[k])
                else:
                    ans.append(-1)

                k += 1

        return ans

