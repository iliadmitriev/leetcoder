

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def dfs(node: int, edges: list[int]) -> list[int]:
            n = len(edges)
            dist = [-1] * n
            dist[node] = 0

            d = 0

            # while there is next node, and there is no cycle (next node is not visited)
            while edges[node] != -1 and dist[edges[node]] == -1:
                d += 1
                node = edges[node]
                dist[node] = d

            return dist

        dist1 = dfs(node1, edges)
        dist2 = dfs(node2, edges)

        minDist = len(edges)
        minNode = -1

        for node in range(len(dist1)):
            if dist1[node] == -1 or dist2[node] == -1:
                continue

            if max(dist1[node], dist2[node]) < minDist:
                minDist = max(dist1[node], dist2[node])
                minNode = node

        return minNode

