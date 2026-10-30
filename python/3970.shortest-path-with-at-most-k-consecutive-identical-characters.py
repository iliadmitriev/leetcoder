import heapq as hq


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        path = [[inf] * (k + 1) for _ in range(n)]
        path[0][1] = 0

        h = [(0, 0, 1)]  # {path weight, node, repeating characters current streak}

        while h:
            dist, node, streak = hq.heappop(h)

            if dist > path[node][streak]:
                continue

            if node == n - 1:
                return dist

            for nnode, w in g[node]:
                nstreak = streak + 1 if labels[node] == labels[nnode] else 1
                if nstreak > k:
                    continue

                ndist = dist + w
                if ndist >= path[nnode][nstreak]:
                    continue

                path[nnode][nstreak] = ndist
                hq.heappush(h, (ndist, nnode, nstreak))

        return -1
