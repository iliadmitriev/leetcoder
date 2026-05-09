class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # shape of grid
        m, n = len(grid), len(grid[0])
        # init queue with all land cells
        queue = deque([(y, x) for y in range(m) for x in range(n) if grid[y][x]])
        # init max distance (result)
        max_dist = 0
        # start BFS for all the land cells
        while queue:
            # get source cell from queue
            y0, x0 = queue.popleft()
            # step right, top, left, bottom from the source cell
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                y, x = y0 + dy, x0 + dx
                # if cell haven't been visited (is 0)
                if 0 <= y < m and 0 <= x < n and not grid[y][x]:
                    # cell distance is greater by one from the source cell
                    grid[y][x] = grid[y0][x0] + 1
                    # recalculate max distance
                    max_dist = max(max_dist, grid[y][x])
                    # put cell to the source cells queue
                    queue.append((y, x))
        
        return max_dist - 1