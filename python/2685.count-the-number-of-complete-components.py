class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.edges = [0] * n
        self.vertices = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def join(self, x1, x2):
        if x1 == x2:
            return

        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            self.edges[p1] += 1
            return

        self.edges[p2] += self.edges[p1] + 1
        self.vertices[p2] += self.vertices[p1]
        self.parent[p1] = p2

    def get_components(self):
        comp = {}
        for u in range(len(self.parent)):
            p = self.find(u)
            comp[p] = (self.edges[p], self.vertices[p])

        return comp


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)

        for u, v in edges:
            uf.join(u, v)

        count = 0
        for c, m in uf.get_components().values():
            if c == m * (m - 1) // 2:
                count += 1

        return count

