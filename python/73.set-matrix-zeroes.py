class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(m):
            if not rows[i]:
                continue

            for j in range(n):
                matrix[i][j] = 0

        for j in range(n):
            if not cols[j]:
                continue

            for i in range(m):
                matrix[i][j] = 0

