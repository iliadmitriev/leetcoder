from itertools import count


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        # calculate number of loops of spiral
        loops = n // 2
        # start counter from 1
        counter = count(1)

        for l in range(loops):
            
            # fill top row from left to right-1 (whole row except for the last rightmost cell)
            for i in range(l, n - l - 1):
                res[l][i] = next(counter)

            # right column from top to bottom-1 (whole column except for the last most bottom cell)
            for i in range(l, n - l - 1):
                res[i][n - l - 1] = next(counter)

            # bottom row from right to left-1 (whole row except for the last leftmost cell)
            for i in range(n - l - 1, l, -1):
                res[n - l - 1][i] = next(counter)

            # left column from bottom to top-1 (whole column except for the last most bottom cell)
            for i in range(n - l - 1, l, -1):
                res[i][l] = next(counter)

        # if number of columns is odd
        # the last cell at the middle of spiral will be left unfilled
        # finally fill the middle
        if n % 2:
            res[n // 2][n // 2] = next(counter)

        return res