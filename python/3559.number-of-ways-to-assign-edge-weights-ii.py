class BinaryLiftTree:
    __slots__ = (
        "size",
        "log_size",
        "depth",
        "adj",
        "up",
    )

    def __init__(self, size: int) -> None:
        self.size = size
        log_size = size.bit_length()
        self.log_size = log_size
        self.depth = [-1] * size
        self.adj = [[] for _ in range(size)]
        self.up = [[-1] * log_size for _ in range(size)]

    def add_edge(self, u: int, v: int) -> None:
        if u > v:
            u, v = v, u

        self.adj[u].append(v)

    def preprocess(self, start: int) -> None:
        # init root from start, without parent(-1), with depth of 0
        self._dfs(start, -1, 0)

    def _dfs(self, u: int, p: int, d: int) -> None:
        self.depth[u] = d  # set node depth
        self.up[u][0] = p  # set base parent

        for j in range(1, self.log_size):
            if self.up[u][j - 1] != -1:
                prev = self.up[u][j - 1]
                self.up[u][j] = self.up[prev][j - 1]
            else:
                break  # reached the root node

        # iterate all neigbours
        for v in self.adj[u]:
            if v == p:  # skip parent node
                continue

            self._dfs(v, u, d + 1)  # go to adjacect node v from u with depth + 1

    def kth_ancestor(self, u: int, k: int) -> int:
        for j in range(self.log_size):
            if (k >> j) & 1:
                u = self.up[u][j]

                if u == -1:
                    break

        return u

    def lca(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        u = self.kth_ancestor(u, self.depth[u] - self.depth[v])

        # now u and v on the same level
        # case 1: they equal
        if u == v:
            return u

        # case 2: not equal, then lift up
        for j in range(self.log_size - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        return self.up[u][0]

    def get_distance(self, u: int, v: int) -> int:
        common = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[common]


class Solution:
    def assignEdgeWeights(
        self, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:

        MOD = int(1e9) + 7
        n = len(edges) + 1
        bt = BinaryLiftTree(n)

        for u, v, *_ in edges:
            bt.add_edge(u - 1, v - 1)

        bt.preprocess(0)  # root = 0

        res = [0] * len(queries)
        for i, (u, v, *_) in enumerate(queries):
            dist = bt.get_distance(u - 1, v - 1)
            if dist > 0:
                res[i] = pow(2, dist - 1, MOD)

        return res
