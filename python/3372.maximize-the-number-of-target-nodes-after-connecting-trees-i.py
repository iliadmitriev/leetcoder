class Solution:
    def buildAdjList(self, edges: list[list[int]]):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj

    def dfs(self, node: int, parent: int, depth: int, adj: list[list[int]]) -> int:
        if depth < 0:
            return 0

        count = 1
        for neighbor in adj[node]:
            if neighbor == parent:
                continue

            count += self.dfs(neighbor, node, depth - 1, adj)

        return count

    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]], k: int
    ) -> list[int]:
        adj1 = self.buildAdjList(edges1)

        if k < 2:
            return [self.dfs(i, -1, k, adj1) + k for i in range(len(adj1))]

        adj2 = self.buildAdjList(edges2)
        max2 = max(self.dfs(i, -1, k - 1, adj2) for i in range(len(adj2)))

        return [self.dfs(i, -1, k, adj1) + max2 for i in range(len(adj1))]

