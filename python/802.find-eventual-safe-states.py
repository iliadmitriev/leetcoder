from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        revEdges = [[] for _ in range(n)]
        safeNodes = [False] * n
        outDegres = [0] * n

        for u, nodes in enumerate(graph):
            for v in nodes:
                revEdges[v].append(u)
                outDegres[u] += 1

        queue = deque([i for i in range(n) if outDegres[i] == 0])

        while queue:
            node = queue.popleft()
            safeNodes[node] = True

            for nNode in revEdges[node]:
                outDegres[nNode] -= 1
                if outDegres[nNode] == 0:
                    queue.append(nNode)

        return [node for node, safety in enumerate(safeNodes) if safety]

