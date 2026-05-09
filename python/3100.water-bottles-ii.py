class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty, total = numBottles, numBottles

        while empty >= numExchange:
            empty -= numExchange
            empty += 1
            total += 1
            numExchange += 1

        return total

