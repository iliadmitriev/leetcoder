class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [-1] * n
        
        def find(i):
            pos = i
            for j in range(m):
                new_pos = pos + grid[j][pos]
                if not(0 <= new_pos < n and grid[j][pos] == grid[j][new_pos]):
                    return -1
                pos = new_pos
            return pos

        
        for i in range(n):
            res[i] = find(i)
        return res