class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        res: list[int] = []

        for i in range(m):
            minRow = matrix[i][0]
            minIdx = 0
            for j in range(1, n):
                if matrix[i][j] < minRow:
                    minRow = matrix[i][j]
                    minIdx = j

            for r in range(m):
                if matrix[r][minIdx] > minRow:
                    break
            else:
                res.append(minRow)

        return res

