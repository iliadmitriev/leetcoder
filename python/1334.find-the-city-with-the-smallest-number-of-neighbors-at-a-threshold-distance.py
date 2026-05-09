from heapq import heappop, heappush


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for _from, _to, _weight in edges:
            adj[_from].append((_to, _weight))
            adj[_to].append((_from, _weight))

        def dijkstra(
            src: int, thresh: int, n: int, adj: list[list[tuple[int, int]]]
        ) -> int:
            dist = [float("inf")] * n
            dist[src] = 0
            heap = [(0, src)]

            while heap:
                w, u = heappop(heap)
                if w > thresh:
                    continue

                for v, _w in adj[u]:

                    if dist[v] <= w + _w:
                        continue

                    heappush(heap, (w + _w, v))
                    dist[v] = w + _w

            dist[src] = float("inf")
            return sum(d <= thresh for d in dist)

        target, minCnt = -1, float("inf")
        for start in range(n):
            dist = dijkstra(start, distanceThreshold, n, adj)
            if dist <= minCnt:
                target, minCnt = start, dist

        return target

