from collections import deque
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = 0
        que: deque[int] = deque()
        inv = 0
        n = len(nums)

        for i in range(len(nums)):
            if que and que[0] == i - k:
                inv = 1 - inv
                que.popleft()

            if inv == nums[i]:
                if i + k > n:
                    return -1

                flips += 1
                inv = 1 - inv
                que.append(i)

        return flips

