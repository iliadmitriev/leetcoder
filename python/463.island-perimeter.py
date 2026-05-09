
from itertools import product
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for y, x in product(range(m), range(n)):
            if grid[y][x] == 0:
                continue

            res += 4
            if y > 0 and grid[y - 1][x] == 1:
                res -= 2
            if x > 0 and grid[y][x - 1] == 1:
                res -= 2

        return res

