class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)

        res = 0
        for i in range(len(grid[0])):
            res += max([grid[j][i] for j in range(len(grid))])

        return res

