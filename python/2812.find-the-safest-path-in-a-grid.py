

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 1 << 31
        dist = [[INF] * COLS for _ in range(ROWS)]

        q: deque[tuple[int, int]] = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 > nr or nr >= ROWS or 0 > nc or nc >= COLS:
                    continue

                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        hq = [(-dist[0][0], 0, 0)]  # distance, row, col
        visited = set([(0, 0)])

        while hq:
            d, r, c = heappop(hq)

            d = -d

            if r == ROWS - 1 and c == COLS - 1:
                return d

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 > nr or nr >= ROWS or 0 > nc or nc >= COLS:
                    continue

                if (nr, nc) in visited:
                    continue

                nd = min(d, dist[nr][nc])

                heappush(hq, (-nd, nr, nc))
                visited.add((nr, nc))

        return -1

