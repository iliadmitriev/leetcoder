class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:

        def findRook(board: list[list[str]], fig: str):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == fig:
                        return i, j
            assert False, "Rook not found"

        rookRow, rookCol = findRook(board, "R")
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        for dr, dc in dirs:
            r, c = rookRow, rookCol
            while (
                r >= 0
                and c >= 0
                and r < len(board)
                and c < len(board[0])
                and board[r][c] != "B"
            ):
                if board[r][c] == "p":
                    res += 1
                    break
                r, c = r + dr, c + dc

        return res

