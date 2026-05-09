class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def line(p1, p2):
            x0, y0 = p1
            x1, y1 = p2
            if (x1 - x0):
                m = (y1 - y0) / (x1 - x0)
                b = y1 - m * x1
                return (m, b)
            else:
                return (x0,)

        data = {}
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                eq = line(points[i], points[j])
                if eq in data:
                    data[eq].update([tuple(points[i]), tuple(points[j])])
                else:
                    data[eq] = set([tuple(points[i]), tuple(points[j])])

        return max(map(len,data.values()))