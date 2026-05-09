class Solution:
    def max2d(self, grid: List[List[int]], r: int, c: int) -> int:
        res = grid[r][c]
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                res = max(res, grid[i][j])

        return res

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = n - 2
        res = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                res[i][j] = self.max2d(grid, i, j)

        return res

