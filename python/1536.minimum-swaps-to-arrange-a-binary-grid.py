
from typing import List


class Solution:
    def trailing_zeros(self, row: list[int]) -> int:
        n = len(row)
        for i in range(len(row) - 1, -1, -1):
            if row[i] == 1:
                return n - i - 1
        return n - 1

    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = [self.trailing_zeros(row) for row in grid]
        print(rows)

        swap = 0
        j = 0
        for i in range(n):
            j = i

            while j < n and rows[j] < n - i - 1:
                j += 1

            if j == n:
                return -1

            swap += j - i

            while j > 0:
                rows[j] = rows[j - 1]
                j -= 1

        return swap

