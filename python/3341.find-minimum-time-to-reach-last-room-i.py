import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        hq = []

        time = [[float("inf")] * n for _ in range(m)]
        time[0][0] = 0
        heapq.heappush(hq, (0, 0, 0))

        while hq:
            t, r, c = heapq.heappop(hq)

            if r == m - 1 and c == n - 1:
                return t

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                nt = max(t, moveTime[nr][nc]) + 1
                if nt < time[nr][nc]:
                    time[nr][nc] = nt
                    heapq.heappush(hq, (nt, nr, nc))

        return -1

