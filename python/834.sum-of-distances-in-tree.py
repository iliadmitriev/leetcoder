from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """Count sum of distances in a tree for all nodes.

        sum[i] = sum[j] - count[i, j] + count[j, i]
        count[i, j] = n - count[j, i]
        """

        res: list[int] = [0] * n

        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count: list[int] = [1] * n
        stack: list[tuple[int, int, bool]] = [(0, -1, False)]
        while stack:
            node, prev, done = stack.pop()
            if done:
                if prev == -1:
                    continue
                count[prev] += count[node]
                res[prev] += res[node] + count[node]
            else:
                stack.append((node, prev, True))
                for child in adj[node]:
                    if child == prev:
                        continue
                    stack.append((child, node, False))

        stack.append((0, -1, True))
        while stack:
            node, prev, _ = stack.pop()

            for child in adj[node]:
                if child == prev:
                    continue
                res[child] = res[node] - count[child] + n - count[child]
                stack.append((child, node, True))

        return res

