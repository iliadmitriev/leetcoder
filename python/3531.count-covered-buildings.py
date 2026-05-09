
from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        covered = 0
        inf = int(1e9)
        n += 1

        x_max = defaultdict(lambda: -inf)  # y -> max x
        x_min = defaultdict(lambda: inf)  # y -> min x

        y_max = defaultdict(lambda: -inf)  # x -> max y
        y_min = defaultdict(lambda: inf)  # x -> min y

        for x, y in buildings:
            x_max[y] = max(x_max[y], x)
            x_min[y] = min(x_min[y], x)

            y_max[x] = max(y_max[x], y)
            y_min[x] = min(y_min[x], y)

        for x, y in buildings:
            if x_min[y] < x < x_max[y] and y_min[x] < y < y_max[x]:
                covered += 1

        return covered

