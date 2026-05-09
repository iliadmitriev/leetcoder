class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Tarjan algorithm
        finding bridges in unidirected graph
        Time: O(V + E)
        Space: O(E)
        """
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
            
        low = [None] * n
        
        bridges = []
        
        def dfs(u: int = 0, parent: int = -1, time = 1) -> None:
            """
            deep first search algorithm
            
            Args:
                v: current node
                parent: parent node
            """
            if low[u]:
                return
            
            low[u] = time
            
            # iterate all neighbours
            for v in adj[u]:
                if v == parent:
                    continue
                dfs(v, u, time + 1)
                if low[v] == time + 1:
                    bridges.append([u, v])
                else:
                    low[u] = min(low[u], low[v])
        
        dfs()
        return bridges