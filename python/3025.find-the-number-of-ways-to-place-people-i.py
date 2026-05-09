class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        n = len(points)

        for i in range(n):
            _, top = points[i]
            btm = float("-inf")

            for j in range(i + 1, n):
                if btm < points[j][1] <= top:
                    count += 1
                    btm = points[j][1]

                    if btm == top:
                        break

        return count

