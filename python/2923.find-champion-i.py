class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:

        return next(
            (i for i in range(len(grid)) if sum(grid[i]) == len(grid[i]) - 1), 0
        )
