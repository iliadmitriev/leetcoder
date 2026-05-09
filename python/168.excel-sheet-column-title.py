class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            columnNumber, rem = divmod(columnNumber, 26)
            res.append(chr(ord('A') + rem))

        return ''.join(reversed(res))