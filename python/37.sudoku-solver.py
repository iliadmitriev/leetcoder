class Solution:

    def check(self, board: List[List[str]], y: int, x: int, char: str) -> bool:
        """Check if char can be put into the board at position (y, x)."""
        for i in range(9):
            if board[y][i] == char or board[i][x] == char:
                return False
        m = y // 3
        n = x // 3
        for i in range(m * 3, m * 3 + 3):
            for j in range(n * 3, n * 3 + 3):
                if board[i][j] == char:
                    return False
        return True

    def find_next_empty(self, board: List[List[str]]):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    yield i, j


    def dfs(self, board: List[List[str]], k: int):        

        if k == len(self.empty_cells):
            return True

        y0, x0 =  self.empty_cells[k]

        res = False
        for ch in range(1,10):
            char = chr(48 + ch)
            if self.check(board, y0, x0, char):
                board[y0][x0] = char
                if self.dfs(board, k + 1):
                    return True
                board[y0][x0] = '.'


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.empty_cells = list(self.find_next_empty(board))
        self.dfs(board, 0)
