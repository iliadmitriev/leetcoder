class Solution:
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self):
        self.time = 0

    def isValidLand(self, grid: list[list[int]], r: int, c: int) -> bool:
        m, n = len(grid), len(grid[0])
        return 0 <= r < m and 0 <= c < n and grid[r][c] == 1

    def articulationPointsDFS(
        self,
        grid: list[list[int]],
        r: int,
        c: int,
        disc: list[list[int]],
        low: list[list[int]],
        parent: tuple[int, int] | None = None,
    ) -> bool:
        """Check if island has any articulation points."""
        disc[r][c] = low[r][c] = self.time
        self.time += 1
        children = 0
        hasArticulation = False

        for dr, dc in self.DIRS:
            nr, nc = r + dr, c + dc
            if not self.isValidLand(grid, nr, nc):
                continue
            if disc[nr][nc] == -1:
                children += 1
                if self.articulationPointsDFS(grid, nr, nc, disc, low, (r, c)):
                    hasArticulation = True

                low[r][c] = min(low[r][c], low[nr][nc])

                if disc[r][c] <= low[nr][nc] and parent is not None:
                    hasArticulation = True

            elif parent != (nr, nc):
                low[r][c] = min(low[r][c], disc[nr][nc])

        if parent is None and children > 1:
            hasArticulation = True

        return hasArticulation

    def minDays(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])
        island = 0
        land = 0
        hasArticulation = False

        disc = [[-1] * n for _ in range(m)]
        low = [[-1] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                land += 1

                if disc[r][c] == -1:
                    island += 1
                    res = self.articulationPointsDFS(grid, r, c, disc, low)
                    hasArticulation = res or hasArticulation

                # optimize earlier return
                if island > 1:
                    return 0

        if island != 1:
            return 0
        elif land == 1 or hasArticulation:
            return 1

        return 2

