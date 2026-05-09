

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = set(jewels)
        return sum(1 for s in stones if s in jew)

