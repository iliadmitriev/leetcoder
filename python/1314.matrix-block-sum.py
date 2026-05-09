class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        
        1) build integral matrix
        2) init zero result matrix
        3) calculate result matrix using integral matrix
        
        """
        
        # m - number of rows (y)
        # n - number of columns (x)
        m, n = len(mat), len(mat[0])
        if n==1 and m==1:
            return mat
        
        # build integral matrix
        """
        a b c         a      a+b        a+b+c
        d e f   =>   d+a    d+e+a+b   d+e+f+a+b+c
        g h i       g+d+a   ......
        
        
        """
        in_mat = [[0] * n for _ in range(m)]
        for i in range(m):
            row = 0
            for j in range(n):
                row += mat[i][j]
                in_mat[i][j] = row
                
                if i > 0:
                    in_mat[i][j] += in_mat[i - 1][j]
                    
        # init result            
        res = [[0] * n for _ in range(m)]
        
        # build result using integral matrix
        for i in range(m):
            for j in range(n):
                
                y_min, y_max = max(0, i - k), min(m - 1, i + k)
                x_min, x_max = max(0, j - k), min(n - 1, j + k)
                
                res[i][j] = in_mat[y_max][x_max]
                
                if y_min > 0:
                    res[i][j] -= in_mat[y_min - 1][x_max]
                    
                if x_min > 0:
                    res[i][j] -= in_mat[y_max][x_min - 1]
                    
                if y_min > 0 and x_min > 0:
                    res[i][j] += in_mat[y_min - 1][x_min - 1]
                    
        return res