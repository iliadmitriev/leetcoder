from collections import deque


class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxComponentWeight = 0
        vis = [[False] * n for _ in range(m)]

        def bfs(
            start: tuple[int, int], visited: list[list[bool]], grid: list[list[int]]
        ) -> int:
            q = deque([start])
            visited[start[0]][start[1]] = True
            componentWeight = 0

            while q:
                row, col = q.popleft()
                componentWeight += grid[row][col]

                for nr, nc in [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ]:
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                        continue

                    if grid[nr][nc] == 0:
                        continue

                    q.append((nr, nc))
                    visited[nr][nc] = True

            return componentWeight

        for r in range(m):
            for c in range(n):
                if grid[r][c] and not vis[r][c]:
                    maxComponentWeight = max(maxComponentWeight, bfs((r, c), vis, grid))

        return maxComponentWeight

