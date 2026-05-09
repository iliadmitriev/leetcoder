class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top < bottom:
            center = (top + bottom) // 2 + 1
            if target < matrix[center][0]:
                bottom = center - 1
            else:
                top = center

        while left < right:
            mid = (left + right) // 2
            if target > matrix[top][mid]:
                left = mid + 1
            else:
                right = mid

        return target == matrix[top][left]