
import heapq


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        m, n = len(grid), len(grid[0])
        k = len(queries)
        res = [0] * k
        count = 0
        q = [(grid[0][0], 0, 0)]
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True

        for i, query in sorted(enumerate(queries), key=lambda x: x[1]):
            while q and query > q[0][0]:
                _, r, c = heapq.heappop(q)
                count += 1

                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if vis[nr][nc]:
                        continue

                    vis[nr][nc] = True
                    heapq.heappush(q, (grid[nr][nc], nr, nc))

            res[i] = count

        return res

