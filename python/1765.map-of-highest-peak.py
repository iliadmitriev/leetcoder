from collections import deque


class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        m, n = len(isWater), len(isWater[0])
        res = [[-1] * n for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 0:
                    continue

                q.append((i, j))
                res[i][j] = 0

        while q:
            r, c = q.popleft()

            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if nc < 0 or nc == n or nr < 0 or nr == m or res[nr][nc] >= 0:
                    continue

                res[nr][nc] = res[r][c] + 1
                q.append((nr, nc))

        return res

