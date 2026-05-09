class Solution:
    @staticmethod
    def build_adj(edges: list[list[int]], k: int) -> list[list[int]]:
        adj = [[] for _ in range(k)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    @staticmethod
    def dfsDiameter(node, parent, adj) -> tuple[int, int]:
        max_d = 0
        max_path1 = 0
        max_path2 = 0

        for child in adj[node]:
            if child == parent:
                continue

            child_d, child_path = Solution.dfsDiameter(child, node, adj)
            max_d = max(max_d, child_d)

            if child_path >= max_path1:
                max_path2 = max_path1
                max_path1 = child_path
            elif child_path > max_path2:
                max_path2 = child_path

        max_d = max(
            max_d,
            max_path1 + max_path2,
        )

        return (max_d, 1 + max(max_path1, max_path2))

    def minimumDiameterAfterMerge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int:
        n, m = len(edges1) + 1, len(edges2) + 1
        adj1, adj2 = self.build_adj(edges1, n), self.build_adj(edges2, m)

        d1, _ = self.dfsDiameter(0, -1, adj1)
        d2, _ = self.dfsDiameter(0, -1, adj2)

        return max(
            d1,
            d2,
            1 + d1 // 2 + d1 % 2 + d2 // 2 + d2 % 2,
        )

