

class Solution:
    def flipRow(self, grid: List[List[int]], r: int) -> None:
        for c in range(len(grid[0])):
            grid[r][c] ^= 1

    def flipCol(self, grid: List[List[int]], c: int) -> None:
        for r in range(len(grid)):
            grid[r][c] ^= 1

    def countTotal(self, grid: List[List[int]]) -> int:
        score = 0
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                score += grid[r][c] << (n - c - 1)
        return score

    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            if grid[r][0] == 0:
                self.flipRow(grid, r)

        for c in range(COLS):
            col_ones = sum(grid[r][c] for r in range(ROWS))
            if col_ones < ROWS - col_ones:
                self.flipCol(grid, c)

        return self.countTotal(grid)

