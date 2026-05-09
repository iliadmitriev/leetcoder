class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        parents = [-1] * n
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        queue = deque([(0, -1)])
        while queue:
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                parents[node] = parent
                for next_ in adj[node]:
                    if next_ != parent:
                        queue.append((next_, node))

        swaps = sum(1 for u, v in connections if parents[u] != v)
        return swaps
                
            