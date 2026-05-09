class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def join(self, x: int, y: int) -> bool:
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return False

        if self.rank[par_x] > self.rank[par_y]:
            par_x, par_y = par_y, par_x

        self.parent[par_x] = par_y
        self.rank[par_y] += self.rank[par_x]
        self.rank[par_x] = 0
        self.components -= 1

        return True


def idx(n: int, r: int, c: int):
    return r * n + c


class Solution:
    @staticmethod
    def _cross(
        row: int, col: int, m: int, n: int, uf: UnionFind, grid: list[int]
    ) -> None:
        target = m * n
        for r in range(row - 1, -1, -1):
            if grid[idx(n, r, col)] == 1:
                break
            uf.join(idx(n, r, col), target)

        for r in range(row + 1, m):
            if grid[idx(n, r, col)] == 1:
                break
            uf.join(idx(n, r, col), target)

        for c in range(col - 1, -1, -1):
            if grid[idx(n, row, c)] == 1:
                break
            uf.join(idx(n, row, c), target)

        for c in range(col + 1, n):
            if grid[idx(n, row, c)] == 1:
                break
            uf.join(idx(n, row, c), target)

    def countUnguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        grid = [0] * (m * n)

        uf = UnionFind(m * n + 1)
        for r, c in walls:
            grid[idx(n, r, c)] = 1
            uf.components -= 1

        for r, c in guards:
            grid[idx(n, r, c)] = 1
            uf.components -= 1

        for r, c in guards:
            self._cross(r, c, m, n, uf, grid)

        return uf.components - 1

