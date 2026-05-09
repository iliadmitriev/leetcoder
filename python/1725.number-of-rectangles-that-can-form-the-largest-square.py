class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:

        count, maxSquare = 0, 0

        for rect in rectangles:
            square = min(rect[0], rect[1])

            if square > maxSquare:
                maxSquare = square
                count = 1
            elif square == maxSquare:
                count += 1

        return count

