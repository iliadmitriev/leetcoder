class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Finds longes increasing path in given matrix.
        
        Brute force:
            Time: O(m * n * 4 ^ (m * n))
            Space: O(1)
        
        Memoization:
            Time: O(m * n)
            Space: O(m * n)
            
        Args:
            matrix (List of lists): given matrix m * n (m, n >= 1)
        
        Return:
            (int): length of longest increasing path
        
        """
        # rows
        m = len(matrix)
        # cols
        n = len(matrix[0])
        
        # directions [up, left, down, right]
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        # matrix for cache
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i: int, j: int, prev: int = -1) -> int:
            """Finds length of max increasing path in matrix starting from given cell.
            
            Args:
                i, j (int): row and column of starting cell
                
            Returns:
                (int): 
            """
            if 0 > i or i >= m or 0 > j or j >= n or prev >= matrix[i][j]:
                return 0
                        
            if dp[i][j] != -1:
                return dp[i][j]
            
            for di, dj in dirs:
                dp[i][j] = max(dp[i][j], dfs(i + di, j + dj, matrix[i][j]) + 1)
                        
            return dp[i][j]
        
                
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
                
        return res