import collections


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        slopes = collections.defaultdict(list)
        mid = collections.defaultdict(list)  # for parallelograms
        INF = 10**9

        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2

                if x1 == x2:
                    k = INF
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx

                m_key = x1 + x2, y1 + y2

                slopes[k].append(b)
                mid[m_key].append(k)

        # totoal trapezoids calculated:
        # trapezoids = (total parallel pairs) - (collinear) - (parallelograms)
        ans = 0

        for bs in slopes.values():
            if len(bs) < 2:
                continue

            cnt = collections.Counter(bs).values()

            total = 0
            for c in cnt:
                ans += total * c
                total += c

        for ks in mid.values():
            if len(ks) < 2:
                continue

            cnt = collections.Counter(ks).values()

            total = 0
            for c in cnt:
                ans -= total * c
                total += c

        return ans

