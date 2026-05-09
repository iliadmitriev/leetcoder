class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        window = 1
        prev = -1
        total = 0

        for price in prices:
            if prev - 1 == price:
                window += 1
            else:
                window = 1

            total += window

            prev = price

        return total

