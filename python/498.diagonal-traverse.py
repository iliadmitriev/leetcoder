class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        finish = (m - 1, n - 1)
        y, x = 1, -1
        step = 1
        res = []
        while (y, x) != finish:

            y, x = y - step, x + step

            if not 0 <= y < m or not 0 <= x < n:
                if x >= n:
                    y += 2
                elif y >= m:
                    x += 2
                step = -step

            y, x = min(max(0, y), m - 1), min(max(0, x), n - 1)
            res.append(mat[y][x])

        return res
