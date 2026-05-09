class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        priceWithDiscount = prices.copy()
        stack = []

        for i, price in enumerate(prices):
            while stack and priceWithDiscount[stack[-1]] >= price:
                priceWithDiscount[stack.pop()] -= price
            stack.append(i)

        return priceWithDiscount

