class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesRow, onesCol = [0] * m, [0] * n
        zerosRow, zerosCol = [0] * m, [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
                else:
                    zerosRow[i] += 1
                    zerosCol[j] += 1

        diff = [[onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j] for j in range(n)] for i in range(m)]
        return diff