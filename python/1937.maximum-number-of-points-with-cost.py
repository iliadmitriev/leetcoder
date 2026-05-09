class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m, n = len(points), len(points[0])
        row = points[0].copy()

        for i in range(1, m):

            left = [0] * n
            left[0] = row[0]
            for j in range(1, n):
                left[j] = max(row[j], left[j - 1] - 1)

            right = [0] * n
            right[n - 1] = row[n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(row[j], right[j + 1] - 1)

            for j in range(n):
                row[j] = points[i][j] + max(left[j], right[j])

        return max(row)

