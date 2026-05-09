from functools import reduce


class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:

        DIRS = {
            "RIGHT": (0, 1),
            "LEFT": (0, -1),
            "UP": (-1, 0),
            "DOWN": (1, 0),
        }

        r, c = reduce(
            lambda acc, step: (acc[0] + DIRS[step][0], acc[1] + DIRS[step][1]),
            commands,
            (0, 0),
        )

        return r * n + c

