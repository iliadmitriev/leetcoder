class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        @cache
        def dp(i, coins):
            if coins == 0 or i == n:
                return 0

            ret = dp(i + 1, coins)
            sum_coins = 0
            for curr_coin in range(min(len(piles[i]), coins)):
                sum_coins += piles[i][curr_coin]
                ret = max(ret, dp(i + 1, coins - curr_coin - 1) + sum_coins)
            return ret

        return dp(0, k)