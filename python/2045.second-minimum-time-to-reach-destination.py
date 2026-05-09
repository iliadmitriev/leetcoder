
from collections import deque


class Solution:
    def secondMinimum(
        self, n: int, edges: list[list[int]], time: int, change: int
    ) -> int:

        def step(w: int, t: int, c: int) -> int:
            p = w // c % 2
            e = p * (w // c + 1) * c + (1 - p) * w
            return e + t

        adj: list[list[int]] = [[] * n for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        q = deque([0])
        vis: list[list[int]] = [
            [] for _ in range(n)
        ]  # vertex -> first time, second time
        total = 0
        res = -1

        while q:
            for _ in range(len(q)):
                u = q.popleft()

                if u == n - 1:
                    if res != -1:
                        return total
                    res = total

                for v in adj[u]:
                    # if it's a first time or a second distinct time
                    if len(vis[v]) == 0 or (len(vis[v]) == 1 and vis[v][0] < total):
                        vis[v].append(total)
                        q.append(v)

            total = step(total, time, change)

        return total

