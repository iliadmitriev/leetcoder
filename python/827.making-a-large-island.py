class UF:
    __slots__ = ["rows", "cols", "par", "rank"]

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        size = rows * cols
        self.par = list(range(size))
        self.rank = [0] * size

    def set_rank(self, grid: list[list[int]]) -> None:
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                self.rank[self.from_pos((y, x))] = val

    def from_pos(self, point: tuple[int, int]) -> int:
        y, x = point
        return y * self.cols + x

    def find(self, point: tuple[int, int]) -> int:
        pos = self.from_pos(point)

        while pos != self.par[pos]:
            self.par[pos] = self.par[self.par[pos]]
            pos = self.par[pos]

        return self.par[pos]

    def join(self, point1: tuple[int, int], point2: tuple[int, int]):
        par1, par2 = self.find(point1), self.find(point2)

        if par1 == par2:
            return

        if self.rank[par1] > self.rank[par2]:
            par1, par2 = par2, par1

        self.par[par1] = par2
        self.rank[par2] += self.rank[par1]
        self.rank[par1] = 0

    def size(self, point: tuple[int, int]) -> int:
        par = self.find(point)
        return self.rank[par]


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        """
        1. component sizes
        2. connect 2 up to 4 (as a bridge)
        3. increase any component by 1
        """

        m, n = len(grid), len(grid[0])
        maxSize = 0
        uf = UF(m, n)

        uf.set_rank(grid)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        uf.join((r, c), (nr, nc))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    maxSize = max(maxSize, uf.size((r, c)))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:

                    sizes = dict()

                    for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                            sizes[uf.find((nr, nc))] = uf.size((nr, nc))

                    maxSize = max(maxSize, sum(sizes.values()) + 1)

        return maxSize

