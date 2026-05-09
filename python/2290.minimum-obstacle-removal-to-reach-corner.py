from collections import deque


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**9
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0

        hq = deque([(0, 0)])  # row, col

        while hq:

            y, x = hq.popleft()

            if y == m - 1 and x == n - 1:
                return dist[y][x]

            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = y + dy, x + dx

                if ny < 0 or ny >= m or nx < 0 or nx >= n:
                    continue

                if dist[ny][nx] <= dist[y][x] + grid[ny][nx]:
                    continue

                dist[ny][nx] = dist[y][x] + grid[ny][nx]
                if grid[ny][nx] == 0:
                    hq.appendleft((ny, nx))
                else:
                    hq.append((ny, nx))

        return -1

