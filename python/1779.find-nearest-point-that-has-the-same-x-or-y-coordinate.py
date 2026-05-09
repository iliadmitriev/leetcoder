class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:

        def dist(p: list[int]) -> int:
            return abs(p[0] - x) + abs(p[1] - y)

        min_dist = 10**5
        idx = -1

        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                curDist = dist(p)
                if curDist < min_dist:
                    idx = i
                    min_dist = curDist

        return idx

