class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:

        maxRowCount = 0
        maxRows: list[int] = [0, 0]

        for i, row in enumerate(mat):
            curCount = sum(row)
            if maxRowCount < curCount:
                maxRowCount = curCount
                maxRows = [i, curCount]

        return maxRows

