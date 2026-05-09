from collections import defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        count = defaultdict(int)
        for row in matrix:
            count[tuple(str(e == row[0]) for e in row)] += 1

        return max(count.values())

