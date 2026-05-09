class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= (m * n)
        
        flat = tuple(grid[i][j] for i in range(m) for j in range(n))
        flat = flat[-k:] + flat[:-k]
        
        grid = [[flat[i * n + j] for j in range(n)] for i in range(m)]
            
        return grid