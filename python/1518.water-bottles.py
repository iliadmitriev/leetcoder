class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        emptyBottles = 0
        while numBottles > 0:
            res += numBottles
            numBottles, emptyBottles = divmod(numBottles + emptyBottles, numExchange)

        return res

