import heapq
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self._size = n
        self._edges: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for u, v, cost in edges:
            self._edges[u].append((v, cost))

    def addEdge(self, edge: List[int]) -> None:
        self._edges[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        """dijkstra algorithm."""
        maxCost = 10**7
        path = [maxCost] * self._size
        path[node1] = 0
        hq = [(0, node1)]

        while hq:
            dist, node = heapq.heappop(hq)

            if node == node2:
                return dist

            for v, cost in self._edges[node]:
                alt = dist + cost
                if alt >= path[v]:
                    continue

                path[v] = alt
                heapq.heappush(hq, (alt, v))

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)