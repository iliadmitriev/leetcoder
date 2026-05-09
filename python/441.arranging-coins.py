class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor(-0.5 + math.sqrt(0.25 + 2 * n))
