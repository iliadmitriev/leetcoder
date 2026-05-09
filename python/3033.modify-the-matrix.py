class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])

        maxCol = [-1] * n

        def getMaxCol(j: int) -> int:
            if maxCol[j] != -1:
                return maxCol[j]

            for i in range(m):
                maxCol[j] = max(maxCol[j], matrix[i][j])

            return maxCol[j]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = getMaxCol(j)

        return matrix

