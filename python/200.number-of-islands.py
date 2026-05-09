from collections import deque
from itertools import product
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        islands = 0

        for y, x in product(range(m), range(n)):
            if grid[y][x] == "0":
                continue

            islands += 1
            grid[y][x] = "0"
            q = deque([(y, x)])
            while q:
                y, x = q.popleft()
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == "1":
                        grid[ny][nx] = "0"
                        q.append((ny, nx))
        return islands

