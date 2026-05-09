import heapq
from collections import defaultdict


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj: defaultdict[int, list[tuple[int, float]]] = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            adj[u].append((v, p))
            adj[v].append((u, p))

        hq = [(-1.0, start_node)]
        prob = [0.0] * n
        prob[start_node] = 1.0

        while hq:
            p, u = heapq.heappop(hq)

            if prob[u] < -p:
                continue

            for v, pp in adj[u]:
                if prob[v] < -p * pp:
                    prob[v] = -p * pp
                    heapq.heappush(hq, (p * pp, v))

        return prob[end_node]

