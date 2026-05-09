class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.weight = [-1] * n

    def find(self, x) -> tuple[int, int]:
        while x != self.parent[x]:
            self.weight[x] &= self.weight[self.parent[x]]
            self.weight[self.parent[x]] &= self.weight[x]

            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x, self.weight[x]

    def join(self, x1: int, x2: int, w: int):
        p1, w1 = self.find(x1)
        p2, w2 = self.find(x2)

        w &= w1 & w2

        self.parent[p1] = p2
        self.weight[p1] = w
        self.weight[p2] = w


class Solution:
    def minimumCost(
        self, n: int, edges: list[list[int]], query: list[list[int]]
    ) -> list[int]:
        results = [-1] * len(query)

        uf = UnionFind(n)
        for u, v, w in edges:
            if u != v:
                uf.join(u, v, w)

        for i, (u, v) in enumerate(query):
            if u == v:
                continue

            p1, w1 = uf.find(u)
            p2, w2 = uf.find(v)

            if p1 != p2:
                continue

            results[i] = w1 & w2

        return results

