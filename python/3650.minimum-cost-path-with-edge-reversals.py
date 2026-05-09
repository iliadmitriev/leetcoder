class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        h = []  # min heap of weight, node
        weights = [-1] * n  # path weight of node to get from 0 (-1 is infinity)
        adj = [[] for _ in range(n)]  # adjacency lists of nodes node -> child, weight
        start, end = 0, n - 1

        for _from, _to, weight in edges:
            adj[_from].append((_to, weight))
            adj[_to].append((_from, 2 * weight))

        # set start node weight of 0
        weights[start] = 0
        heapq.heappush(h, (0, start))

        while h:
            weight, node = heapq.heappop(h)

            if weights[node] != -1 and weights[node] < weight:
                continue

            if node == end:
                return weight

            for child, edge_weight in adj[node]:
                child_weight = weight + edge_weight

                if weights[child] == -1 or weights[child] > child_weight:
                    weights[child] = child_weight
                    heapq.heappush(h, (child_weight, child))

        return weights[end]
