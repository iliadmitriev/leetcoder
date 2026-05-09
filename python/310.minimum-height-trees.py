from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """Get minimum height trees roots.

        Idea:
            1. build adjacency lists for vertices
            2. get all leaves
            3. start bfs from leaves with order level traversal
            4. if only 2 or less vertices left, return them
        """
        if n <= 2:
            return list(range(n))

        adj: list[set[int]] = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            tmp = []
            for leaf in leaves:
                for nxt in adj[leaf]:
                    adj[nxt].remove(leaf)
                    if len(adj[nxt]) == 1:
                        tmp.append(nxt)
            leaves = tmp

        return leaves

