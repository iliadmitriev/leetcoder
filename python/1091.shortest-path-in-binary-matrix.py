import heapq as hq
from itertools import product
from collections import deque, defaultdict
from typing import Set, List, Tuple, Iterator


Position = Tuple[int, int]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        BFS approach
        
        Time: O(m * n)
        Space: O(m * n)
        
        """
        m, n = len(grid), len(grid[0])
        start, end = (0, 0), (m - 1, n - 1)
                
        # (-1, -1), (-1, 0), ....
        dirs = list(product([-1, 0, 1], repeat=2))
        dirs.remove((0, 0))

        def step(pos: Position, grid: List[List[int]]) -> Iterator[Position]:
            for dy, dx in dirs:
                y, x = pos[0] + dy, pos[1] + dx
                if 0 <= y < m and 0 <= x < n and not grid[y][x]:
                    yield y, x


        # init all vertices distance as +infinity
        distances = defaultdict(lambda: float("inf"))
        
        # queue of (row, col)
        queue = []

        # heauristic function: (how much step left to the end)
        # max(m, n), when x is start,
        # 1, when x is end
        h = lambda x: max(m - x[0], n - x[1])
        
        # first step
        if not grid[0][0] and not grid[-1][-1]:
            distances[start] = 1
            queue.append([h(start), start])
        
        while queue:
            _, pos = hq.heappop(queue)
            distance = distances[pos]
            
            if pos == end:
                return distance
            
            for next_pos in step(pos, grid):
                if distance + 1 < distances[next_pos]:
                    distances[next_pos] = distance + 1
                    hq.heappush(queue, (distance + h(next_pos), next_pos))
                    
        return -1