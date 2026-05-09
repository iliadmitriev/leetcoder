class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        # accumulate all columns within rows
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = matrix[i - 1][j - 1] + prefix[i][j - 1]
        
        count = 0
        for c1 in range(1, n + 1):
            for c2 in range(c1, n + 1):                
                memo = defaultdict(int)
                memo[0] = 1
                curr = 0
                for r in range(1, m + 1):
                    curr += prefix[r][c2] - prefix[r][c1 - 1]
                    if (curr - target) in memo:
                        count += memo[curr - target]
                    memo[curr] += 1
                    
        return count