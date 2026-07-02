import heapq

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        sides = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        finish = m - 1, n - 1


        health -= grid[0][0]
        hq = [(-health, (0, 0))]

        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True
        
        while hq:
            health, pos = heapq.heappop(hq)
            health = -health

            if pos == finish:
                return True

            for dr, dc in sides:
                nr, nc = pos[0] + dr, pos[1] + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                new_health = health - grid[nr][nc]
                if new_health <= 0:
                    continue

                if vis[nr][nc]:
                    continue
                
                vis[nr][nc] = True
                heapq.heappush(hq, (-new_health, (nr, nc)))

        return False

        