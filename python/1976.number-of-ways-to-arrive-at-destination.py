import heapq
from collections import defaultdict


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = int(1e9) + 7
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        q = [(0, 0)]
        weight = [float("inf")] * n
        count = [0] * n

        count[0] = 1
        weight[0] = 0

        while q:
            nodeWeight, node = heapq.heappop(q)

            for nei, w in graph[node]:
                if weight[nei] > nodeWeight + w:
                    weight[nei] = nodeWeight + w
                    count[nei] = count[node]
                    heapq.heappush(q, (weight[nei], nei))
                elif weight[nei] == nodeWeight + w:
                    count[nei] += count[node]
                    count[nei] %= MOD

        return count[n - 1]

