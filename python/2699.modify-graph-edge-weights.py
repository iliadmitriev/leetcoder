import heapq


class Solution:

    def modifiedGraphEdges(
        self, n: int, edges: list[list[int]], source: int, destination: int, target: int
    ) -> list[list[int]]:
        INF = int(2e9)
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            if w != -1:
                adj[u].append((v, w))
                adj[v].append((u, w))

        shortestDistance = self.dijkstra(source, destination, adj)
        # if path to exist without using modifiable edges
        # and it's weight less than target it's impossible to build target path
        if shortestDistance < target:
            return []

        # if path to modifiable exists without using modifiable edges
        # and it's weight is equal to target
        # then we don't need to use modifiable edges (set them all to infinity)
        if shortestDistance == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF

            return edges

        for i, (u, v, w) in enumerate(edges):
            # skip static edges, we can't modify them
            if w > 0:
                continue

            # set modifiable edge to min == 1
            # and run Dijkstra again
            adj[u].append((v, 1))
            adj[v].append((u, 1))
            edges[i][2] = 1
            newDistance = self.dijkstra(source, destination, adj)
            # print("added", edges[i], "new distance", newDistance)
            # print(adj)

            # if found a path, then correct it's weight to match target and
            # set all other modifiable edges to INF and return result
            if newDistance <= target:
                edges[i][2] += target - newDistance

                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF

                return edges

        return []

    @staticmethod
    def dijkstra(
        source: int,
        destination: int,
        adj: list[list[int]],
    ) -> int:
        INF = int(2e9)
        minDist = [INF] * len(adj)
        minDist[source] = 0

        minHeap = [(0, source)]

        while minHeap:
            dist, u = heapq.heappop(minHeap)

            for v, w in adj[u]:
                if dist + w < minDist[v]:
                    minDist[v] = dist + w
                    heapq.heappush(minHeap, (minDist[v], v))

        return minDist[destination]
