from collections import deque


class Solution:
    @staticmethod
    def bfs(start, adj, groups):
        curGroup = 0
        q = deque([start])
        groups[start] = curGroup

        while q:
            curGroup += 1

            for _ in range(len(q)):
                node = q.popleft()

                for nnode in adj[node]:
                    if groups[nnode] == -1:
                        q.append(nnode)
                        groups[nnode] = curGroup
                    elif (
                        groups[nnode] == groups[node] - 1
                        or groups[nnode] == groups[node] + 1
                    ):
                        pass
                    else:
                        return -1

        return curGroup

    @staticmethod
    def bfs_bipartite(
        node: int,
        colors: list[int],
        adj: list[list[int]],
    ) -> tuple[bool, list[int]]:
        component = []

        colors[node] = 1
        q = deque([node])

        while q:
            node = q.popleft()
            component.append(node)

            for nnode in adj[node]:
                if colors[nnode] == 0:
                    q.append(nnode)
                    colors[nnode] = -colors[node]
                elif colors[nnode] == colors[node]:
                    return False, []

        return True, component

    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        components = []
        maxGroups = 0
        groups = [-1] * n
        colors = [0] * n

        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        for node in range(n):
            if colors[node] != 0:
                continue

            res, component = self.bfs_bipartite(node, colors, adj)

            if not res:
                return -1

            components.append(component)

        for component in components:

            curComponentMax = -1

            for start in component:
                for node in component:
                    groups[node] = -1

                curNodeMax = self.bfs(start, adj, groups)
                curComponentMax = max(curComponentMax, curNodeMax)

            if curComponentMax == -1:
                return -1

            maxGroups += curComponentMax

        return maxGroups

