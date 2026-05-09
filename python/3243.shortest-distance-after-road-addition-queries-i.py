from collections import deque


class Solution:
    @staticmethod
    def bfsShortestPath(adj: list[list[int]], dist: list[int], start: int = 0):
        finish = len(dist) - 1
        q = deque([start])

        while q:
            node = q.popleft()

            if node == finish:
                return

            for child in adj[node]:
                if dist[child] <= dist[node] + 1:
                    continue

                dist[child] = dist[node] + 1
                q.append(child)

    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[i - 1].append(i)

        dist = list(range(n))

        answer = []
        for u, v in queries:
            adj[u].append(v)

            if dist[v] > dist[u] + 1:
                self.bfsShortestPath(adj, dist, u)

            answer.append(dist[n - 1])

        return answer

