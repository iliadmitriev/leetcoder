class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c = [0] * 3
        for s in stones:
            c[s % 3] += 1

        if c[0] % 2 == 0:
            return c[1] >= 1 and c[2] >= 1

        return c[1] - c[2] > 2 or c[2] - c[1] > 2