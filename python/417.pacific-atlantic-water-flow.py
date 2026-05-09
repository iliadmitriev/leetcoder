class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(sea: List[List[bool]], grid: List[List[int]], r: int, c: int, prev: int) -> None:
            m, n = len(grid), len(grid[0])
            
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            queue = deque([(r, c, prev)])
            sea[r][c] = True

            while queue:
                row, col, prev = queue.popleft()
                                    
                for dy, dx in dirs:
                    r, c = row + dy, col + dx
                    if 0 <= r < m and 0 <= c < n and not sea[r][c] and grid[r][c] >= grid[row][col]:
                        queue.append((r, c, grid[row][col]))
                        sea[r][c] = True
                        
        m, n = len(heights), len(heights[0])
        atlantic = [[False] * n for _ in range(m)]
        pacific = [[False] * n for _ in range(m)]
        
        # dfs starting from all of the four borders
        for j in range(n):
            if not pacific[0][j]:
                dfs(pacific, heights, 0, j, 0)
            if not atlantic[m - 1][j]:
                dfs(atlantic, heights, m - 1, j, 0)
        for i in range(m):
            if not pacific[i][0]:
                dfs(pacific, heights, i, 0, 0)
            if not atlantic[i][n - 1]:
                dfs(atlantic, heights, i, n - 1, 0)
                    
        # if cell is both reachable from atlantic and pacific
        # add it to the answer result
        res = []     
        for i in range(m):
            for j in range(n):
                if atlantic[i][j] and pacific[i][j]:
                    res.append((i, j))
        return res