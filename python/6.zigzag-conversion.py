class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = [[] for _ in range(numRows)]
        down = True
        row = 0

        for char in s:
            # add char to current row
            res[row].append(char)
            # add or subtract 1 depending on direction: down +1, up -1
            row += 1 if down else -1
            # switch direction if reached first or last row (0 or numRows - 1)
            if row == 0 or row == numRows - 1:
                down = not down

        return ''.join(map(''.join, res))

