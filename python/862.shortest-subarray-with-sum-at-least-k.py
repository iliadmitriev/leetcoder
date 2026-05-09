
from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        cur = 0
        res = len(nums) + 1

        st = deque([(0, -1)])

        for i, num in enumerate(nums):
            cur += num

            while st and st[-1][0] >= cur:
                _ = st.pop()

            st.append((cur, i))

            while st and cur - st[0][0] >= k:
                res = min(res, i - st.popleft()[1])

        if res > len(nums):
            res = -1

        return res

