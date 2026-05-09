class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """Finds all possible placements of queens in chessboard.
        
        DFS with backtracking algorithm.
        
        Time: O(exp(n))
        Space: O(exp(n))
        
        Idea:
        
        i - is row
        j - is column
        
        Use 3 sets to store:
            1. set of used columns
            2. set of used diagonals (top left to bottom right)
               stored as difference i - j
               (0,0), (1,1), (2,2) on the same diagonal
               (1,0), (2,1), (3,2) on the same diagonal
            3. set of used back diagonals (bottom left to top right)
               stored as summ i + j
               (7,0), (1,6), (2,5) in the same diagonal
               
        Args:
            n (int): number of Queens
        
        """
        # result list
        res = []
        # used columns
        cols = set()
        # used diagonals
        diag = set()
        # used back diagonals
        back_diag = set()
        
        def solve(curr, r: int):
            """Recursively interate all possible placements for current row.
            
            Args:
                r (int): row
            """
            if r == n:
                res.append(curr)
                return
            
            # iterate possible columns
            for c in range(n):
                if c not in cols and c - r not in diag and c + r not in back_diag:
                    # add found column to solution
                    cols.add(c)
                    diag.add(c - r)
                    back_diag.add(c + r)
                    # try to find next column
                    solve(curr + ["." * (c) + "Q" + "." * (n - c - 1)], r + 1)
                    # remove column
                    cols.remove(c)
                    diag.remove(c - r)
                    back_diag.remove(c + r)

        solve([], 0)
        return res