class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        area = 0
        for i in range(rows):
            for j in range(cols):

                # 4 tiles for 1 unit of height to cover vertically
                # 2 tile for top and bottom if # cubes > 0
                area += 4 * grid[i][j] + 2 * (grid[i][j] > 0)

                # discard 2 tiles for attachment of two cube columns horiz.
                if i > 0:
                    area -= min(grid[i][j], grid[i - 1][j]) * 2

                # discard 2 tiles for attachment of two cube columns vertically
                if j > 0:
                    area -= min(grid[i][j], grid[i][j - 1]) * 2

        return area

