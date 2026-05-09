class Solution:
    def coloredCells(self, n: int) -> int:
        n -= 1
        k = 1
        step = 4

        while n:
            n -= 1
            k += step
            step += 4

        return k

