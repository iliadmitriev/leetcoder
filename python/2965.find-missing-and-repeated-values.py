class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        count = [0] * (n**2 + 1)

        j = 1
        mix = 0
        repeated = 0

        for row in grid:
            for value in row:
                mix ^= value ^ j
                j += 1

                count[value] += 1
                if count[value] == 2:
                    repeated = value

        return [repeated, mix ^ repeated]

