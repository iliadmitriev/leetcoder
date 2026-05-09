class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
              
        def bfs(y, x):
            area = 0

            queue = deque()
            if (x, y) not in visited:
                queue.append((x, y))
                visited.add((x, y))
            
            while queue:
                x, y = queue.popleft()
                area += 1
                
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[ny][nx] and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        
            return area

        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, bfs(i, j))

        return res