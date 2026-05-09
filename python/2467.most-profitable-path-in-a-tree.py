from collections import deque


class Solution:
    def mostProfitablePath(
        self, edges: list[list[int]], bob: int, amount: list[int]
    ) -> int:
        n = len(amount)
        q = deque()
        tree = [[] for _ in range(n)]
        parent = [0] * n
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        q0 = deque([(0, 0)])
        adj = [[] for _ in range(n)]
        while q0:
            node, prev = q0.popleft()
            parent[node] = prev

            for v in tree[node]:
                if v == prev:
                    continue

                adj[node].append(v)
                q0.append((v, node))

        q.append((0, 0))
        profit = -int(1e9)
        while q:

            for _ in range(len(q)):
                cost, alice = q.popleft()

                curProfit = amount[alice]
                if alice == bob:
                    curProfit //= 2

                if not adj[alice]:
                    profit = max(profit, cost + curProfit)

                for v in adj[alice]:
                    if v == parent[alice]:
                        continue

                    q.append((cost + curProfit, v))

            amount[bob] = 0
            bob = parent[bob]

        return profit

