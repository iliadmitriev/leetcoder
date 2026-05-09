class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        if m != n:
            return False

        for i in range(m):
            for j in range(n):
                if (i == j) or (n - i - 1 == j):
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False

        return True

