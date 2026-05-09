class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """Memoization.

        Time: m * n * maxMove
        Space: m * n * maxMove
        """

        @cache
        def path(row: int, col: int, moves_left: int) -> int:
            if row == m or col == n or row < 0 or col < 0:
                return 1
            if moves_left == 0:
                return 0
            
            return (
                path(row + 1, col, moves_left - 1) 
                + path(row - 1, col, moves_left - 1)
                + path(row, col + 1, moves_left - 1)
                + path(row, col - 1, moves_left - 1)
            )
    
        res = path(startRow, startColumn, maxMove) % (10**9 + 7)
        path.cache_clear()
        return res