
from typing import Iterator


class neighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])
        self.data: dict[int, tuple[int, int]] = {}
        for y, row in enumerate(grid):
            for x, v in enumerate(row):
                self.data[v] = (y, x)

    def nodeIter(
        self, start: tuple[int, int], nodes: list[tuple[int, int]]
    ) -> Iterator[int]:
        y, x = start
        for dy, dx in nodes:
            ny, nx = y + dy, x + dx
            if 0 <= ny < self.M and 0 <= nx < self.N:
                yield self.grid[ny][nx]

    def adjacentSum(self, value: int) -> int:
        if value not in self.data:
            return 0

        return sum(
            self.nodeIter(
                self.data[value],
                [(-1, 0), (0, 1), (1, 0), (0, -1)],
            ),
        )

    def diagonalSum(self, value: int) -> int:
        if value not in self.data:
            return 0

        return sum(
            self.nodeIter(
                self.data[value],
                [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            ),
        )

