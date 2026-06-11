class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        # number of edges in tree is equal number of nodes - 1
        n = len(edges) + 1 # number of nodes
        MOD = int(1e9) + 7

        adj = [[] for _ in range(n)]
        for a, b, *_ in edges:
            # sort and shift from 1-base indexes to 0-base
            u, v = min(a, b) - 1, max(a, b) - 1
            adj[u].append(v) 

        def bfs_max_depth(start: int) -> int:
            q = deque([start])
            d = [-1] * n
            d[start] = 0
            while q:
                node = q.popleft()
                for child in adj[node]:
                    if d[child] != -1:
                        continue
                    
                    d[child] = d[node] + 1
                    q.append(child)
            
            return max(d)

        def dfs_max_depth(node: int, parent: int = -1) -> int:
            depth = 0

            for child in adj[node]:
                if child == parent:
                    continue
                
                depth = max(depth, 1 + dfs_max_depth(child, node))

            return depth
        
        k = bfs_max_depth(0)
        return pow(2, k - 1, MOD)