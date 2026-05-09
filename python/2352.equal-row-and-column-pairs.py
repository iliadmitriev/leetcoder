from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_cache = Counter(tuple(row) for row in grid)

        res = 0
        for col in range(n):
            column = tuple(grid[row][col] for row in range(n))
            res += row_cache[column]
        return res