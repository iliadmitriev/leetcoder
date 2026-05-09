class Solution:

    def rot90(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                # swap values counterclockwise
                # save to temp bottom left corner
                tmp = matrix[n - 1 - j][i]
                # move value from bottom right corver to bottom right
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # move value from top right to bottom right
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # move value from top left to top right
                matrix[j][n - 1 - i] = matrix[i][j]
                # set top left value from saved bottom left
                matrix[i][j] = tmp
                
    def check(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        n = len(a)
        for i in range(n):
            for j in range(n):
                if a[i][j] != b[i][j]:
                    return False
        return True
    
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # check if 0 deg rotation is a match
        if self.check(mat, target):
            return True
        
        # check if 90 deg rotation is a match
        self.rot90(mat)
        if self.check(mat, target):
            return True

        # check if 180 deg rotation is a match
        self.rot90(mat)
        if self.check(mat, target):
            return True

        # check if 270 deg rotation is a match
        self.rot90(mat)
        if self.check(mat, target):
            return True

        # finally return false
        return False