class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        top, bottom, left, right = 0, m - 1, 0, n - 1

        res = []
        while top < bottom and left < right:
            for j in range(left, right):
                res.append(matrix[top][j])

            for i in range(top, bottom):
                res.append(matrix[i][right])

            for j in range(right, left, -1):
                res.append(matrix[bottom][j])
            
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                res.append(matrix[i][j])

        return res