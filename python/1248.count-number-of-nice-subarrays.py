from collections import deque
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        q: deque[int] = deque()
        prev = -1

        for i in range(len(nums)):
            if nums[i] % 2:
                q.append(i)

            if len(q) > k:
                prev = q.popleft()

            if len(q) == k:
                count += q[0] - prev

        return count

