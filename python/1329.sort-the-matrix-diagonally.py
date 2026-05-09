class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Time: O(m * max(m, n) * log(max(m, n)))
        Space: O(m * n)
        """
        # dict of lists
        diag = defaultdict(list)
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                diag[i - j].append(mat[i][j])
        
        for k, v in diag.items():
            v.sort(reverse=True)
                
                
        for i in range(m):
            for j in range(n):
                mat[i][j] = diag[i - j].pop()
                
        return mat