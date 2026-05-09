import collections
import heapq


class Solution:
    def processQueries(
        self, c: int, connections: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        adj = collections.defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        online = set()
        groups = {}
        min_heaps = collections.defaultdict(list)
        res = []

        def dfs(station, group_id):
            if station in online:
                return

            online.add(station)
            groups[station] = group_id
            h = min_heaps[group_id]
            heapq.heappush(h, station)

            for v in adj[station]:
                dfs(v, group_id)

        # build connected components
        for s in range(1, c + 1):
            dfs(s, s)

        for q_type, q_station in queries:
            if q_type == 1:
                if q_station in online:
                    res.append(q_station)
                    continue

                group_id = groups[q_station]
                h = min_heaps[group_id]

                while h and h[0] not in online:
                    heapq.heappop(h)

                if h:
                    res.append(h[0])
                else:
                    res.append(-1)

            elif q_type == 2:
                online.discard(q_station)

        return res

