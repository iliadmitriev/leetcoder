class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res, tmp = [], []
        for i in range(rowIndex + 1):
            tmp = [0] * (i + 1)
            tmp[0] = tmp[i] = 1
            for j in range(1, i):
                tmp[j] = res[j - 1] + res[j]
            res = tmp
            
        return res