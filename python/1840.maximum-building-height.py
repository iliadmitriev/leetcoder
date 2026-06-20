import itertools


class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        top_height = 0
        r = [[1, 0]] + sorted(restrictions)

        # if there is no restriction on the last building
        # set it to max possible value "inf" (n - 1)
        if r[-1][0] < n:
            r.append([n, n - 1])

        k = len(r)

        # eq I slope: y - y0 = m(x - x),
        # where m = {1,-1} for left A and rigth B slope
        # slope A) y - y1 = 1 * (x - x1)
        # slope B) y - y2 = -1 * (x - x2)
        # A - B
        # => y - y1 - y + y2 = x - x1 + x - x2
        # => y2 - y1 + x1 + x2 = 2 * x
        # x = (y2 - y1 + x1 + x2) // 2
        # A + B
        # y + y - y1 - y2 = -x1 - x2
        # y = (y1 + y2 - x1 + x2) // 2

        def solve(x1, y1, x2, y2) -> int:
            # x = (y2 - y1 + x1 + x2) // 2
            y = (y1 + y2 - x1 + x2) // 2
            return y

        # eq II: dy <= dx
        # |y2 - y1| <= |x2 - x1| (drop left abs, it's less)
        # y2 - y1 <= |x2 - x1|
        # y2 <= y1 + |x2 - x1|

        def cap(x1, y1, x2, y2) -> int:
            return min(y2, y1 + abs(x2 - x1))

        for i in range(1, k):
            r[i][1] = cap(*r[i - 1], *r[i])  # order matters!

        for i in range(k - 2, -1, -1):
            r[i][1] = cap(*r[i + 1], *r[i])  # order matters!

        for (x1, y1), (x2, y2) in itertools.pairwise(r):
            y = solve(x1, y1, x2, y2)
            top_height = max(top_height, y)

        return top_height
