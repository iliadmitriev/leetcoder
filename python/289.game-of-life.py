from itertools import product

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        Idea:
        * use second LSB (least significant bit) to store next round state
        * shift right after all calculations
        """
        # number of rows
        m = len(board)
        # number of columns
        n = len(board[0])
        
        # generate tuples (di, dj)
        # 8 possible directions
        dirs = list(product((-1, 0, 1), repeat=2))
        dirs.remove((0, 0))
        
        # iterate row, column
        for i, j in product(range(m), range(n)):
            # get if column live
            live = board[i][j] & 1
            # calcualte number of neighbours in all 8 directions
            neighbours = 0
            for di, dj in dirs:
                if 0 <= (i + di) < m and 0 <= (j + dj) < n:
                    neighbours += board[i + di][j + dj] & 1
            
            # if there is 3 neighbours
            # or cell is alive and has 2 neighbours
            if neighbours == 3 or (live and neighbours == 2):
                # set it live
                board[i][j] |= 2
                
        for i, j in product(range(m), range(n)):
            board[i][j] >>= 1
        