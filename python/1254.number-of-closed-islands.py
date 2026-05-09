from itertools import product
from queue import deque
from typing import Tuple, Set, List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        Position = Tuple[int, int]
        def step(pos: Position, vis: Set[Position]) -> Position:
            phase = (-1, 0, 1, 0, -1)
            for i in range(4):
                row, col = pos[0] + phase[i], pos[1] + phase[i + 1]
                if 0 <= row < m and 0 <= col < n \
                        and grid[row][col] == 0 and (row, col) not in vis:
                    yield row, col

        def bfs(pos: Position, vis: Set[Position]) -> bool:
            border = False
            vis.add(pos)
            queue = deque([pos])
            while queue:
                pos = queue.popleft()
                if pos[0] == 0 or pos[0] == m - 1 or pos[1] == 0 or pos[1] == n - 1:
                    border = True
                for next_pos in step(pos, visited):
                    vis.add(next_pos)
                    queue.append(next_pos)

            return not border

        visited = set()
        res = 0
        for pos in product(range(m), range(n)):
            if grid[pos[0]][pos[1]] == 0 and pos not in visited:
                res += bfs(pos, visited)

        return res

        

