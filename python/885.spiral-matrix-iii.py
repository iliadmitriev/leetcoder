class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        """Movements.
        right
        down
        left + 1
        top + 1
        """
        r, c = rStart, cStart
        coords: list[list[int]] = []
        cycle = 1  # changes every 2 steps
        dir = 0  # 0: right, 1: down, 2: left, 3: top; changes every step
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        i = 0  # counter

        while len(coords) < rows * cols:
            for _ in range(cycle):
                if 0 <= r < rows and 0 <= c < cols:
                    coords.append([r, c])
                r += dirs[dir][0]
                c += dirs[dir][1]

            dir = (dir + 1) % 4
            cycle += i % 2
            i += 1

        return coords

