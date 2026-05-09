class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                l = max(0, j - 1)
                r = min(n, j + 2)
                matrix[i][j] += min(matrix[i - 1][l:r])

        return min(matrix[-1])