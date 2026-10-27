class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        def slope(y: int, x: int) -> int:
            return abs(m * y - n * x)

        grid = [["#"] * n for _ in range(m)]
        grid[0][0] = "."

        r, c = 0, 0

        while r < m - 1 or c < n - 1:
            if c == n - 1 or (r < m - 1 and slope(r + 1, c) <= slope(r, c + 1)):
                r += 1
            else:
                c += 1

            grid[r][c] = "."

        return ["".join(row) for row in grid]
