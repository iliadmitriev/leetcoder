class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:

        n = len(grid)
        xy = yz = xz = 0

        for i in range(n):
            xy += sum(grid[i][j] > 0 for j in range(n))
            yz += max(grid[j][i] for j in range(n))
            xz += max(grid[i][j] for j in range(n))

        return xy + yz + xz

