from itertools import product

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time: O(m * n)
        Space: O(m * n)
        """
        m, n = len(board), len(board[0])
        
        for i in range(m):
            row = set()
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        return False

        for j in range(n):
            col = set()
            for i in range(m):
                if board[i][j] != '.':
                    if board[i][j] not in col:
                        col.add(board[i][j])
                    else:
                        return False
        
        for i, j in product(range(m // 3), range(n // 3)):
            square = set()
            for y in range(3 * i, 3 * i + 3):
                for x in range(3 * j, 3 * j + 3):
                    if board[y][x] != '.':
                        if board[y][x] not in square:
                            square.add(board[y][x])
                        else:
                            return False
                            
        return True
        