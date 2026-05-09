class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        def check(intervals: list[tuple[int, int]]) -> bool:
            intervals.sort()
            count, right = 0, 0

            for a, b in intervals:
                if a >= right:
                    count += 1

                right = max(right, b)

                if count == 3:
                    return True

            return count >= 3

        X, Y = [], []
        for x1, y1, x2, y2 in rectangles:
            X.append((x1, x2))
            Y.append((y1, y2))

        return check(X) or check(Y)

