class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        dx, dy = 0, 1  # face north direction
        farest = 0

        obst = set(map(tuple, obstacles))

        for cmd in commands:
            match cmd:
                case -1:
                    dx, dy = dy, -dx # cw
                case -2:
                    dx, dy = -dy, dx # ccw
                case _:
                    for _ in range(cmd):
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in obst:
                            break

                        x, y = nx, ny

            farest = max(farest, x * x + y * y)

        return farest
