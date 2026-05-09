class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def diff(p1, p2) -> int:
            return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

        res = 0
        for i in range(1, len(points)):
            res += diff(points[i - 1], points[i])

        return res