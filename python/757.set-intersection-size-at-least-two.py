class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        cnt = 0

        intervals.sort(key=lambda x: (x[1], -x[0]))
        p1, p2 = -1, -1

        for a, b in intervals:
            if p2 < a:
                cnt += 2
                p1, p2 = b - 1, b

            elif p1 < a:
                cnt += 1
                p1, p2 = p2, b

        return cnt

