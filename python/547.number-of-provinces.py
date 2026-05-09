class UnionFind:
    def __init__(self, size: len):
        self.parent = list(range(size))

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False

    def components_count(self):
        return len({self.find(x) for x in self.parent})


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for u, v in product(range(n), range(n)):
            if isConnected[u][v]:
                uf.union(u, v)
        
        return uf.components_count()
        