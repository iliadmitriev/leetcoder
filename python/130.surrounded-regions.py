class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Time: O(m * n)
        Space: O(m * n)
        """
        def mark(cells: List[Tuple], glyph: str, brd: List[List[str]]) -> None:
            """Set glyph to all coordinates in cells"""
            for y, x in cells:
                brd[y][x] = glyph
                
        def find_island(i: int, j: int, vis: List[List[str]], brd: List[List[str]]) -> List[Tuple]:
            """Find island from (i, j) cells."""
            queue = [(i, j)]
            vis[i][j] = True
            res = []
            while queue:
                y, x = queue.pop()
                res.append((y, x))
                for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                    y_pos, x_pos = y + dy, x + dx
                    if 0 <= y_pos < m and 0 <= x_pos < n and not vis[y_pos][x_pos] and brd[y_pos][x_pos] == 'O':
                        vis[y_pos][x_pos] = True
                        queue.append((y_pos, x_pos))
            return res
                        
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        
        # 1. find all 'O' islands adjacent to board limits
        #    and mark all 'O's as '-' 
        #         left and right board limits
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O' and (i, j) not in visited:
                    cells = find_island(i, j, visited, board)
                    mark(cells, '-', board)
        #         top and bottom limits
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    cells = find_island(i, j, visited, board)
                    mark(cells, '-', board)
        
        # switch all '-' to 'O's and 'O's to 'X's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'