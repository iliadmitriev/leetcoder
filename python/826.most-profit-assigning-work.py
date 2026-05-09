from collections import deque
from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        earning = deque(sorted(zip(difficulty, profit)))
        maxProfit = 0
        prevMax = 0

        for w in sorted(worker):
            while earning and w >= earning[0][0]:
                _, prev = earning.popleft()
                prevMax = max(prev, prevMax)

            maxProfit += prevMax

        return maxProfit

