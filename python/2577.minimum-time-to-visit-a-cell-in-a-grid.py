import heapq


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 10**9

        start = (0, 0)
        finish = (m - 1, n - 1)

        hq: list[tuple[int, tuple[int, int]]] = [(0, start)]
        timer = [[INF] * n for _ in range(m)]
        timer[0][0] = 0

        while hq:

            time, node = heapq.heappop(hq)

            if node == finish:
                return time

            for dy, dx in DIR:
                y, x = node[0] + dy, node[1] + dx

                if y < 0 or y >= m or x < 0 or x >= n:
                    continue

                if time >= grid[y][x]:
                    new_time = time + 1
                else:
                    new_time = grid[y][x] + (time - grid[y][x] + 1) % 2

                if new_time < timer[y][x]:
                    heapq.heappush(hq, (new_time, (y, x)))
                    timer[y][x] = new_time

        return -1

