class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        i, j = 0, 0

        while i < m and j < n:
            matrix[i][j] = min(rowSum[i], colSum[j])
            if rowSum[i] == colSum[j]:
                i += 1
                j += 1
            elif rowSum[i] > colSum[j]:
                rowSum[i] -= colSum[j]
                j += 1
            else:
                colSum[j] -= rowSum[i]
                i += 1

        return matrix

