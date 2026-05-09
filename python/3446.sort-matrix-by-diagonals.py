from collections import defaultdict


class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        buf = defaultdict(list)
        for i in range(n):
            for j in range(n):
                buf[i - j].append(grid[i][j])

        for key, diag in buf.items():
            diag.sort(reverse=key < 0)

        for i in range(n):
            for j in range(n):
                grid[i][j] = buf[i - j].pop()

        return grid

