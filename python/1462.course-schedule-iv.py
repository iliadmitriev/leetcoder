from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        m = len(queries)
        res = [False] * m
        adj = [[] for _ in range(numCourses)]

        for p in prerequisites:
            adj[p[0]].append(p[1])

        allPaths = defaultdict(set)

        def dfs(
            src: int, adj: list[list[int]], allPaths: dict[int, set[int]]
        ) -> set[int]:
            if src not in allPaths:
                for dst in adj[src]:
                    allPaths[src] |= dfs(dst, adj, allPaths)
                allPaths[src].add(src)

            return allPaths[src]

        for src in range(numCourses):
            dfs(src, adj, allPaths)

        for i, (u, v) in enumerate(queries):
            res[i] = v in allPaths[u]

        return res

