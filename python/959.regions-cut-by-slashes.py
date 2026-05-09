from collections import deque


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        upscale = [[0] * n * 3 for _ in range(m * 3)]  # upscaled grid by 3
        islands = 0

        def bfs(y: int, x: int) -> None:
            q = deque([(y, x)])
            upscale[y][x] = 1

            while q:
                y, x = q.popleft()
                for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < m * 3 and 0 <= nx < n * 3 and upscale[ny][nx] == 0:
                        q.append((ny, nx))
                        upscale[ny][nx] = 1

        # fill cells for
        # "\\" - [011; 101; 110], "/" [110;101;011], " " [000;000;000]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == " ":
                    continue
                elif grid[i][j] == "\\":
                    for k in range(3):
                        upscale[i * 3 + k][j * 3 + k] = 1
                elif grid[i][j] == "/":
                    for k in range(3):
                        upscale[i * 3 + k][j * 3 + 2 - k] = 1

        # bfs from each not visited cell, counting islands
        for i in range(m * 3):
            for j in range(n * 3):
                if upscale[i][j] == 1:
                    continue

                bfs(i, j)
                islands += 1

        return islands

