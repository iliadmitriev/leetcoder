class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(v):
            while v != parent[v]:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return parent[v]

        def union(u, v):
            parent_u, parent_v = find(u), find(v)

            if parent_u == parent_v:
                return

            parent[parent_u] = parent_v

        for u, v in edges:
            union(u, v)

        components = Counter(map(find, parent))

        return sum(size * (n - size) for size in components.values()) // 2

