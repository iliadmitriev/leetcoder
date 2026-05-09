class Solution:
    def totalNQueens(self, n: int) -> int:
        """Finds number of way to locate n Queens.
        
        Time: O(n^2)
        Space: O(n)
        
        DFS with backtracking.
        ref # 51 https://leetcode.com/problems/n-queens/
        
        Args:
            n (int): Total number of Queens.
            
        Returns:
            (int): number of ways to locate n Queens on n * n chessboard. 
        
        """
        cols = set()
        fwd_diag = set()
        back_diag = set()
        
        def backtrack(r: int) -> int:
            """Calculates number of queens statring from row r.
            
            Args:
                r (int): row
                
            Returns:
                (int): number of rows starting from row r.
            
            """
            if r == n:
                return 1
            
            res = 0
            
            for c in range(n):
                if c not in cols \
                   and c - r not in fwd_diag \
                   and c + r not in back_diag:
                    cols.add(c)
                    fwd_diag.add(c - r)
                    back_diag.add(c + r)
                    
                    res += backtrack(r + 1)
                    
                    cols.remove(c)
                    fwd_diag.remove(c - r)
                    back_diag.remove(c + r)            
            
            return res
        
        return backtrack(0)
