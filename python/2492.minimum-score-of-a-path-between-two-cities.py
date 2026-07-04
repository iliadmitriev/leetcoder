INF = float("inf")


class UF:
    def __init__(self, cap: int) -> None:
        self.par = list(range(cap))
        self.min_edge = [INF] * cap

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x

    def join(self, x:int, y: int, w: int) -> None:
        parx, pary = self.find(x), self.find(y)

        min_edge = min(self.min_edge[parx], self.min_edge[pary], w)
        self.min_edge[parx] = min_edge
        self.par[pary] = parx

    def comp_min_edge(self, x: int) -> int:
        parx = self.find(x)
        return self.min_edge[parx]


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        uf = UF(n)
        
        for a, b, w in roads:
            uf.join(a - 1, b - 1, w)

        return uf.comp_min_edge(n - 1)
        