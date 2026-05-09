class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """BFS."""
        m, n = len(grid), len(grid[0])
        
        if k >= m + n - 2: 
            return m + n - 2

        cache = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def neighbors(y, x):
            for dy, dx in dirs:
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < m and 0 <= new_x < n:
                    yield new_y, new_x

        queue = deque([(0, 0, k, 0)])
        
        while queue:
            y, x, left, step = queue.popleft()
            
            # check we have moves left
            if (y, x, left) in cache or left < 0:
                continue
                
            # check if it's a final
            if (y, x) == (m - 1, n - 1):
                return step

            cache.add((y, x, left))            
            for new_y, new_x in neighbors(y, x):
                queue.append((new_y, new_x, left - grid[y][x], step + 1))
                         
        return -1
            