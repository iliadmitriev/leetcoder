import collections


class Solution:
    def countCollisions(self, directions: str) -> int:
        to_num = {"L": -1, "R": 1, "S": 0}
        collisions = 0

        q = collections.deque()

        for d in directions:
            dd = to_num[d]

            while q and q[-1] > dd:
                vv = q.pop()

                collisions += vv - dd
                dd = 0

            q.append(dd)

        return collisions

