class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = 101, 101
        for price in prices:
            if min1 > price:
                min1, min2 = price, min1
            elif min2 > price:
                min2 = price

        if min1 + min2 <= money:
            return money - (min1 + min2)

        return money