class UnionFind:
    __slots__ = ("parent",)

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def join(self, x: int, y: int) -> bool:
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return False
        self.parent[par_x] = par_y
        return True


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)
        redundant = edges[0]

        uf = UnionFind(N + 1)

        for u, v in edges:
            if not uf.join(u, v):
                redundant = [u, v]

        return redundant

