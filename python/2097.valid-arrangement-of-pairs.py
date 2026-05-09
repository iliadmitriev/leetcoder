from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        """Hierholzer's algorithm."""
        adj = defaultdict(list)
        order = defaultdict(int)
        for u, v in pairs:
            adj[u].append(v)
            order[v] += 1
            order[u] -= 1

        # if sum(order.values()) != 0:  # sanity check
        #     return []

        start = min(order.keys(), key=lambda k: order[k])

        curPath = [-1]
        cur = start
        circuit = []

        while curPath:

            if adj[cur]:
                curPath.append(cur)
                cur = adj[cur].pop()

            else:
                circuit.append(cur)
                cur = curPath.pop()

        res = []
        for i in range(len(circuit) - 2, -1, -1):
            res.append([circuit[i + 1], circuit[i]])

        return res

