from collections import defaultdict


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        rowAdj, colAdj = defaultdict(list), defaultdict(list)

        for u, v in stones:
            rowAdj[u].append(v)
            colAdj[v].append(u)

        visited = set()
        count = 0

        for u, v in stones:
            if (u, v) in visited:
                continue
            self.dfs(u, v, rowAdj, colAdj, visited)
            count += 1

        return len(stones) - count

    def dfs(
        self,
        u: int,
        v: int,
        rowAdj: defaultdict[int, list[int]],
        colAdj: defaultdict[int, list[int]],
        visited: set[int],
    ):
        visited.add((u, v))

        for dv in rowAdj[u]:
            if (u, dv) in visited:
                continue
            visited.add((u, dv))
            self.dfs(u, dv, rowAdj, colAdj, visited)

        for du in colAdj[v]:
            if (du, v) in visited:
                continue

            visited.add((du, v))
            self.dfs(du, v, rowAdj, colAdj, visited)

