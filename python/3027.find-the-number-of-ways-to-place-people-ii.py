class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        n = len(points)
        count = 0

        for i in range(n):
            maxY = points[i][1]
            minY = -float("inf")

            for j in range(i + 1, n):
                if minY < points[j][1] <= maxY:
                    count += 1
                    minY = points[j][1]

                if maxY == minY:
                    break

        return count

