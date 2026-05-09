class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, 0
        
        while row >= 0 and col < len(matrix[0]):
            res = matrix[row][col]
            
            if res > target:
                row -= 1
            elif res < target:
                col += 1
            else:
                return True
            
        return False