class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node: int, parent: int = -1) -> tuple[int, int]:
            total = values[node]
            maxComp = 0

            for child in adj[node]:
                if parent == child:
                    continue

                comp, add = dfs(child, node)
                total += add
                maxComp += comp

            maxComp += total % k == 0
            return maxComp, total

        maxComponents, _ = dfs(0, -1)
        return maxComponents

