class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total = 0
        countNeg = 0
        minAbs = abs(matrix[0][0])
        zero = False

        for row in matrix:
            for item in row:
                if item < 0:
                    item = -item
                    countNeg += 1

                if item < minAbs:
                    minAbs = item

                if item == 0:
                    zero = True

                total += item

        if zero or countNeg % 2 == 0:
            return total

        return total - minAbs * 2

