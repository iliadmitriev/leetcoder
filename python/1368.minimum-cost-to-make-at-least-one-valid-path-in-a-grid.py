import heapq

STEPS = [(0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)]
Position = tuple[int, int]


class Solution:
    @staticmethod
    def step(pos: Position, grid: list[list[int]]):
        m, n = len(grid), len(grid[0])

        for dy, dx, p in STEPS:
            y, x = pos
            ny, nx = y + dy, x + dx

            if 0 <= nx < n and 0 <= ny < m:
                cost = 0 if p == grid[y][x] else 1
                yield (ny, nx), cost

    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start, end = (0, 0), (m - 1, n - 1)

        hq = [(0, start)]
        visited = {start: 0}
        INF = int(1e9)

        while hq:
            cost, node = heapq.heappop(hq)
            if node == end:
                return cost

            for newNode, addedCost in self.step(node, grid):
                if visited.get(newNode, INF) <= cost + addedCost:
                    continue

                heapq.heappush(hq, (cost + addedCost, newNode))
                visited[newNode] = cost + addedCost

        return -1

