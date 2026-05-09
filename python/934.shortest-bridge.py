from collections import deque
from itertools import product
from typing import Tuple, Iterator


Point = Tuple[int, int]


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def land(pos: Point) -> bool:
            return grid[pos[0]][pos[1]] == 1

        def step(pos: Point, vis: Set[Point]) -> Iterator[Point]:
            phase = (-1, 0, 1, 0, -1)
            for i in range(4):
                row, col = pos[0] + phase[i], pos[1] + phase[i + 1]
                if 0 <= row < m and 0 <= col < n and (row, col) not in vis:
                    yield row, col

        def dfs(start: Point) -> Set[Point]:
            vis = set([start])
            stack = [start]
            while stack:
                pos = stack.pop()
                for next_pos in step(pos, vis):
                    if land(next_pos):
                        stack.append(next_pos)
                        vis.add(next_pos)
            return vis

        def bfs(vis: Set[Point]) -> int:
            queue = deque(zip(vis, repeat(0)))
            
            while queue:
                pos, value = queue.popleft()
                for next_pos in step(pos, vis):
                    if land(next_pos):
                        return value
                    else:
                        queue.append((next_pos, value + 1))
                        vis.add(next_pos)

            return -1

        pos = next(filter(land, product(range(m), range(n))))

        vis = dfs(pos)

        return bfs(vis)