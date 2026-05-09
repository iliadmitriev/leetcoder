class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        row = triangle[-1].copy()
        
        for i in range(n - 2, -1, -1):
            for j in range(0, i + 1):
                row[j] = triangle[i][j] + min(row[j], row[j + 1])
        
        return row[0]