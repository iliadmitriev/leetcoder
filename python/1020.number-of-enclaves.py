from collections import deque
from itertools import product
from typing import List, Set, Tuple, Iterator


Position = Tuple[int, int]


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def step(pos: Position, vis: Set[Position]) -> Iterator[Position]:
            phase = (-1, 0, 1, 0, -1)
            for i in range(4):
                row, col = pos[0] + phase[i], pos[1] + phase[i + 1]
                if 0 <= row < m and 0 <= col < n and grid[row][col] == 1 and (row, col) not in vis:
                    yield row, col

        def check_boundary(pos: Position) -> bool:
            row, col = pos
            return row == 0 or row == m - 1 or col == 0 or col == n - 1

        def bfs(start: Position, vis: Set[Position]) -> int:
            queue = deque([start])
            vis.add(start)
            count, reset = 0, False
            while queue:
                pos = queue.popleft()
                if check_boundary(pos):
                    reset = True
                count += 1
                for next_pos in step(pos, vis):
                    queue.append(next_pos)
                    vis.add(next_pos)
            return 0 if reset else count

        visited = set()
        enclaves = 0
        for row, col in product(range(m), range(n)):
            pos = (row, col)
            if grid[row][col] == 1 and pos not in visited:
                enclaves += bfs(pos, visited)

        return enclaves
