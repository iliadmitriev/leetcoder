import math


class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:

        m, n = len(grid), len(grid[0])
        columns = [0] * n

        for j in range(n):
            columns[j] = max(map(len, (str(grid[i][j]) for i in range(m))))

        return columns

