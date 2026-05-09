from collections import deque


class Solution:
    def topoSort(self, n: int, edges: list[list[int]]) -> tuple[list[int], bool]:
        arr = [0] * n
        indegree = [0] * n
        adj: list[list[int]] = [[] for _ in range(n)]
        for _from, _to in edges:
            indegree[_to - 1] += 1
            adj[_from - 1].append(_to - 1)

        q: deque[int] = deque()
        j = 0

        for z in range(n):
            if indegree[z] == 0:
                q.append(z)

            while q:
                u = q.popleft()
                arr[u] = j
                indegree[u] = -1
                j += 1
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)

        if j != n:
            return [], False

        return arr, True

    def buildMatrix(
        self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]
    ) -> list[list[int]]:
        rowOrder, rowOk = self.topoSort(k, rowConditions)
        colOrder, colOk = self.topoSort(k, colConditions)

        if not rowOk or not colOk:
            return []

        mat = [[0] * k for _ in range(k)]
        for i, (r, c) in enumerate(zip(rowOrder, colOrder)):
            mat[r][c] = i + 1

        return mat

