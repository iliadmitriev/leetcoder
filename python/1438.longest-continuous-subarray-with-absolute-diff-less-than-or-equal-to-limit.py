import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_q: list[tuple[int, int]] = []
        max_q: list[tuple[int, int]] = []
        longest = 0

        left = 0
        for right, num in enumerate(nums):
            heapq.heappush(min_q, (num, right))
            heapq.heappush(max_q, (-num, right))

            while -max_q[0][0] - min_q[0][0] > limit:
                left = min(min_q[0][1], max_q[0][1]) + 1

                while min_q[0][1] < left:
                    heapq.heappop(min_q)
                while max_q[0][1] < left:
                    heapq.heappop(max_q)

            longest = max(longest, right - left + 1)

        return longest

