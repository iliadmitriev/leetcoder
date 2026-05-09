class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # cumulative matrix
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]

        
        res = 0
        for row in matrix:
            row.sort(reverse=True)
            for i, v in enumerate(row):
                if v == 0:
                    break

                res = max(res, v * (i + 1))

        return res