from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        entrance = tuple(entrance)
        queue = deque([(*entrance, 0)])
        visited = set([entrance])

        def walk(y, x):
            dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for dy, dx in dirs:
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < m and 0 <= new_x < n:
                    yield new_y, new_x

        while queue:

            y, x, step = queue.popleft()
            # check if reached a border
            if entrance !=  (y, x) and (y == 0 or y == m - 1 or x == 0 or x == n - 1):
                return step

            for new_y, new_x in walk(y, x):
                if maze[new_y][new_x] == '.' and (new_y, new_x) not in visited:
                    queue.append((new_y, new_x, step + 1))
                    visited.add((new_y, new_x))
                
        return -1

