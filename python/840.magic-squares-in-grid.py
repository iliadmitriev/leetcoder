class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        count = 0

        def isMagic(y: int, x: int) -> bool:
            s: set[int] = set()
            target = 15
            diag1, diag2 = 0, 0

            for dy in range(3):
                for dx in range(3):
                    if grid[y + dy][x + dx] > 9:
                        return False
                    s.add(grid[y + dy][x + dx])

            if len(s) != 9:
                return False

            for d in range(3):
                diag1 += grid[y + d][x + d]
                diag2 += grid[y + d][x + 2 - d]

            if diag1 != target or diag2 != target:
                return False

            for d1 in range(3):
                sumRow, sumCol = 0, 0
                for d2 in range(3):
                    sumRow += grid[y + d1][x + d2]
                    sumCol += grid[y + d2][x + d1]

                if sumRow != target or sumCol != target:
                    return False

            return True

        for i in range(m - 2):
            for j in range(n - 2):
                if isMagic(i, j):
                    count += 1

        return count

