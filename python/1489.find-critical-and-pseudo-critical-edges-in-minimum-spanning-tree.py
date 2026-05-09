class UnionFind:
    def __init__(self, n: int):
        self._par = list(range(n))
        self._rank = [1] * n

    def find(self, x: int) -> int:
        while x != self._par[x]:
            self._par[x] = self._par[self._par[x]]
            x = self._par[x]
        return x

    def union(self, x1: int, x2: int) -> bool:
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False

        if self._rank[p1] > self._rank[p2]:
            p1, p2 = p2, p1

        self._par[p1] = p2
        self._rank[p2] += self._rank[p1]
        self._rank[p1] = 0

        return True
    

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # convert edges to sorted edges with original index i
        edges = sorted(
            ((u, v, w, i) for i, (u, v, w) in enumerate(edges)),
            key=lambda edge: edge[2] 
        )

        critical, pseudo = [], []

        for u1, v1, w1, i in edges:
            uf_base = UnionFind(n)
            uf_curr = UnionFind(n)

            # force current candidate edge to be a part of MST
            uf_base.union(u1, v1)
            weight_base = w1

            weight_curr = 0
            
            for u2, v2, w2, j in edges:

                if i == j:
                    continue

                if uf_base.union(v2, u2):
                    weight_base += w2

                if uf_curr.union(v2, u2):
                    weight_curr += w2
            
            # if total weight of current MST is greater or graph is disconnected
            # (unable to create MST without current i-th edge)
            # then candiate edge is critical
            if weight_curr > weight_base or uf_curr.union(v1, u1):
                critical.append(i)
            # if we be able to build MST with the same weight
            # then candiate edge is pseudo critical
            elif weight_base == weight_curr:
                pseudo.append(i)

        return [critical, pseudo]