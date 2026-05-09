import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        finish = (m - 1, n - 1)

        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0

        q = [(0, 0, 0, 0)]

        while q:
            d, s, r, c = heapq.heappop(q)

            if (r, c) == finish:
                return d

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                nd = max(d, moveTime[nr][nc]) + 1 + s
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(q, (nd, 1 - s, nr, nc))

        return -1

