from collections import deque
from typing import List


class Solution:

    def dfs(
        self, land: list[list[int]], i: int, j: int, visited: list[list[bool]]
    ) -> tuple[int, int]:
        q: deque[tuple[int, int]] = deque()
        q.append((i, j))
        visited[i][j] = True

        while q:

            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in [(0, 1), (1, 0)]:
                    y, x = i + di, j + dj
                    if (
                        y < 0
                        or y >= len(land)
                        or x < 0
                        or x >= len(land[0])
                        or visited[y][x]
                        or land[y][x] == 0
                    ):
                        continue
                    visited[y][x] = True
                    q.append((y, x))

        return i, j

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res: list[list[int]] = []
        m, n = len(land), len(land[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and not visited[i][j]:
                    ni, nj = self.dfs(land, i, j, visited)
                    res.append([i, j, ni, nj])

        return res

