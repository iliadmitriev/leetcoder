from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_y == root_x:
            return False
            
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        return True


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # build adjacency lists
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # build map unique value -> list of vertices which have this value
        value_idxs = defaultdict(list)
        for i, val in enumerate(vals):
            value_idxs[val].append(i)
        
        res = 0
        uf = UnionFind(len(vals))
        # iterate all unique values, starting from the smallest one to the greatest
        for val in sorted(value_idxs.keys()):
            # for a single value we have to get all ot it's the vertices (vertices with current value)
            for i in value_idxs[val]:
                # union all neighbors of i, with values less than i
                for nei in adj[i]:
                    if vals[nei] <= vals[i]:
                        uf.union(nei, i)

            # for each disjoint set (designated with val), how many values does it contains?
            count = defaultdict(int)
            for i in value_idxs[val]:
                root = uf.find(i)
                # each new n-th vertex adds n to count of good paths
                # i.e. 1, 1+1, 2+1, 3+1 => 10
                count[root] += 1
                res += count[root]

        return res