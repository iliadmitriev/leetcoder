class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        # trType: 
        #  0 - None
        #  1 - normal
        #  -1 - short

        @cache
        def dp(i: int, done: int, trType: int, running: bool) -> int:
            if done >= k or i >= n:
                return 0 if not running else float("-inf")

            # skip i - th day

            profit = dp(i + 1, done, trType, running)

            if running:

                if trType == 1: # normal
                    # try to sell this day
                    sell = prices[i] + dp(i + 1, done + 1, 0, False)
                    profit = max(profit, sell)

                elif trType == -1: # short
                    # try to buy this day
                    buy = -prices[i] + dp(i + 1, done + 1, 0, False)
                    profit = max(profit, buy)

            else:

                # try run normal: 1
                buy = -prices[i] + dp(i + 1, done, 1, True)
                profit = max(profit, buy)

                # or try run short: -1
                sell = prices[i] + dp(i + 1, done, -1, True)
                profit = max(profit, sell)

            return profit

        res = dp(0, 0, 0, False)
        dp.cache_clear()
        return res



            