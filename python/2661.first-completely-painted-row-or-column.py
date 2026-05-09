class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])

        row = [0] * (m * n + 1)
        col = [0] * (m * n + 1)
        rowCount = [n] * m
        colCount = [m] * n

        for i in range(m):
            for j in range(n):
                row[mat[i][j]] = i
                col[mat[i][j]] = j

        for idx, value in enumerate(arr):
            rowCount[row[value]] -= 1
            colCount[col[value]] -= 1

            if rowCount[row[value]] == 0 or colCount[col[value]] == 0:
                return idx

        return -1

