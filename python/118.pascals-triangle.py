class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pas = [[] for _ in range(numRows)]

        for i in range(numRows):
            pas[i] = [1] * (i + 1)
            for j in range(1, i):
                pas[i][j] = pas[i - 1][j - 1] + pas[i - 1][j]

        return pas

