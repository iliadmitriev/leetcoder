import collections


class Solution:
    def buildAdjacencyList(self, edges: list[list[int]]) -> list[list[int]]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        return adj

    def dfsEvenLevelNodesCount(
        self, adj: list[list[int]], node: int, parent: int = -1, even: bool = True
    ) -> int:
        count = 0

        if even:
            count += 1

        for child in adj[node]:
            if child == parent:
                continue

            count += self.dfsEvenLevelNodesCount(adj, child, node, not even)

        return count

    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> list[int]:
        adj1 = self.buildAdjacencyList(edges1)
        adj2 = self.buildAdjacencyList(edges2)

        even1 = self.dfsEvenLevelNodesCount(adj1, 0)
        odd1 = len(adj1) - even1

        even2 = self.dfsEvenLevelNodesCount(adj2, 0)
        maxNodes2 = max(even2, len(adj2) - even2)

        counts = [even1 + maxNodes2, odd1 + maxNodes2]

        res = [-1] * len(adj1)  # -1 not visited yet
        q = collections.deque([0])
        level = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res[node] = counts[level]

                for child in adj1[node]:
                    if res[child] != -1:
                        continue
                    q.append(child)

            level = 1 - level

        return res

