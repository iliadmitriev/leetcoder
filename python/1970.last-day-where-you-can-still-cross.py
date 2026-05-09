from collections import deque


class Solution:
    @staticmethod
    def multiSourceBFS(cells: list[list[int]], row: int, col: int, k: int) -> bool:
        """Multi source BFS from to matrix row to bottom."""
        mat = [[0] * col for _ in range(row)]
        end = row - 1

        # mark first k cells
        for i in range(k):
            r, c = cells[i]
            mat[r][c] = 1

        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        q = deque()

        # add first row to queue
        for c in range(col):
            if mat[0][c] != 0:
                continue
            mat[0][c] = 1
            q.append((0, c))

        while q:
            r, c = q.popleft()

            if r == end:
                return True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 > nr or nr >= row or 0 > nc or nc >= col:
                    continue

                if mat[nr][nc] != 0:
                    continue

                mat[nr][nc] = 1
                q.append((nr, nc))

        return False

    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        # convert to zero based
        for cell in cells:
            cell[0] -= 1
            cell[1] -= 1

        lo, hi = 0, len(cells)
        res = 0

        while lo < hi:
            mid = (lo + hi) // 2

            if self.multiSourceBFS(cells, row, col, mid):
                lo = mid + 1
                res = mid
            else:
                hi = mid

        return res

