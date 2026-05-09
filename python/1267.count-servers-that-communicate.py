from collections import defaultdict, deque


class Solution:
    @staticmethod
    def _bfs(start, visited, adjRow, adjCol):
        components = 0
        q = deque([start])
        visited.add(start)
        while q:
            row, col = q.popleft()
            components += 1

            for ncol in adjRow[row]:
                if ncol == col or (row, ncol) in visited:
                    continue

                visited.add((row, ncol))
                q.append((row, ncol))

            for nrow in adjCol[col]:
                if nrow == row or (nrow, col) in visited:
                    continue

                visited.add((nrow, col))
                q.append((nrow, col))

        return components

    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        servers = []
        adjRow = defaultdict(set)
        adjCol = defaultdict(set)
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                servers.append((i, j))
                adjRow[i].add(j)

        for j in range(n):
            for i in range(m):
                if grid[i][j] == 0:
                    continue

                adjCol[j].add(i)

        visited = set()
        for server in servers:
            if server in visited:
                continue

            components = self._bfs(server, visited, adjRow, adjCol)

            if components > 1:
                count += components

        return count

