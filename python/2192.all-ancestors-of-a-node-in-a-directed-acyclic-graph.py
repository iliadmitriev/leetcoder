from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors: list[list[int]] = [[] for _ in range(n)]

        adj: list[list[int]] = [[] for _ in range(n)]
        for _from, _to in edges:
            adj[_from].append(_to)

        def dfs(node: int, start: int) -> None:
            for child in adj[node]:
                # prevent node `start` from being already added
                # from a diffrent path
                if ancestors[child] and ancestors[child][-1] == start:
                    continue

                ancestors[child].append(start)
                dfs(child, start)

        for i in range(n):
            dfs(i, i)

        return ancestors

