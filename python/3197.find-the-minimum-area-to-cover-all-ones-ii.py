

class Solution:
    def findSquare(
        self, grid: list[list[int]], a: tuple[int, int], b: tuple[int, int]
    ) -> int:
        if (a, b) in self.dp:
            return self.dp[a, b]

        total = 0
        left, right, top, bottom = b[1], a[1], b[0], a[0]

        for i in range(a[0], b[0]):
            for j in range(a[1], b[1]):
                if grid[i][j] == 1:
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    bottom = max(bottom, i)

        height = bottom - top + 1
        width = right - left + 1

        if height > 0 and width > 0:
            total = height * width

        self.dp[a, b] = total

        return total

    def minimumSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.dp = {}

        total = m * n

        # try all possible 3 horizontal splits with 2 cuts
        for i1 in range(1, m - 1):
            for i2 in range(i1 + 1, m):
                total = min(
                    total,
                    self.findSquare(grid, (0, 0), (i1, n))
                    + self.findSquare(grid, (i1, 0), (i2, n))
                    + self.findSquare(grid, (i2, 0), (m, n)),
                )

        # try all possible 3 vertical splits with 2 cuts
        for j1 in range(1, n - 1):
            for j2 in range(j1 + 1, n):
                total = min(
                    total,
                    self.findSquare(grid, (0, 0), (m, j1))
                    + self.findSquare(grid, (0, j1), (m, j2))
                    + self.findSquare(grid, (0, j2), (m, n)),
                )

        # try horizontal and then vertical split (in 3 parts)
        # and vertical and then horizontal split (in 3 parts)
        for i in range(1, m):
            for j in range(1, n):
                top = self.findSquare(grid, (0, 0), (i, n))
                bottomLeft = self.findSquare(grid, (i, 0), (m, j))
                bottomRight = self.findSquare(grid, (i, j), (m, n))

                bottom = self.findSquare(grid, (i, 0), (m, n))
                topLeft = self.findSquare(grid, (0, 0), (i, j))
                topRight = self.findSquare(grid, (0, j), (i, n))

                total = min(
                    total,
                    top + bottomLeft + bottomRight,
                    bottom + topLeft + topRight,
                )

                left = self.findSquare(grid, (0, 0), (m, j))
                rightTop = self.findSquare(grid, (0, j), (i, n))
                rightBottom = self.findSquare(grid, (i, j), (m, n))

                right = self.findSquare(grid, (0, j), (m, n))
                leftTop = self.findSquare(grid, (0, 0), (i, j))
                leftBottom = self.findSquare(grid, (i, 0), (m, j))

                total = min(
                    total,
                    left + rightTop + rightBottom,
                    right + leftTop + leftBottom,
                )

        return total

