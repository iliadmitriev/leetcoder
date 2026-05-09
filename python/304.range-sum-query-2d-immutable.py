class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """Initializes NumMatrix class.
        
        Builds integrational matrix.
        
        Each cell of integrational matrix is a sum of all cells
        located between top left corner and this cell.
        
        Args:
            matrix: m * n sized matrix
        """
        m = len(matrix)
        n = len(matrix[0])
        
        self.in_mat = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.in_mat[i][j] = self.in_mat[i - 1][j] + self.in_mat[i][j - 1] - self.in_mat[i - 1][j - 1] + matrix[i - 1][j - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Returns sum of all cells located in the rectangle.
        
        Calculates sum of all cells located in the rectangle 
        with upper left corner and lower right corner.
        
        Args:
            row1 (int): upper left corner row
            col1 (int): upper left corner column
            row2 (int): lower right corner row
            col2 (int): lower right corner column
            
        Returns:
            (int): sum of all cells located in the rectangle.
        """
        return self.in_mat[row2 + 1][col2 + 1] - self.in_mat[row2 + 1][col1] - self.in_mat[row1][col2 + 1] + self.in_mat[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)