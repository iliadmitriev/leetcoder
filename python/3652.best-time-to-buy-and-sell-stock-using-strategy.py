class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        base = sum(s * p for s, p in zip(strategy, prices))

        n = len(strategy)
        h = k // 2

        old = sum(s * p for s, p in zip(strategy[:k], prices[:k]))
        second = sum(p for p in prices[h:k])

        maxYield = max(0, second - old)

        for r in range(k, n):
            l = r - k + 1

            old += prices[r] * strategy[r] - prices[l - 1] * strategy[l - 1]
            second += prices[r]
            second -= prices[l - 1 + h]
            maxYield = max(maxYield, second - old)

        return base + maxYield

