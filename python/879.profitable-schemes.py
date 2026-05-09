class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7 # primary divisor

        dp = [[0] * (n + 1) for i in range(minProfit + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(i + p, minProfit)][j + g] += dp[i][j]
                    dp[min(i + p, minProfit)][j + g] %= mod
        return sum(dp[minProfit]) % mod
        
        # I. Aproach
        # dp[i][m][p]
        # i - current crime
        # m - number of people left
        # p - current profit (max minProfit)
        # dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]

        # base case
        # if we have reached last crime len(group) (no matter how much we have chosen m)
        # for a reached minProfit, there is one way
        # for m in range(n + 1):
        #     dp[len(group)][m][minProfit] = 1

        # for i in range(len(group) - 1, -1, -1): # i - current crime
        #     g, pr = group[i], profit[i] # g-people needed and p-profit
        #     for m in range(n + 1): # current members
        #         for p in range(minProfit + 1):
        #             dp[i][m][p] = dp[i + 1][m][p]
        #             if g + m <= n:
        #                 dp[i][m][p] += dp[i + 1][g + m][min(minProfit, p + pr)]
        #             dp[i][m][p] %= mod

        # return dp[0][0][0]

        # II. Aproach
        # i - current index, n - number of people left,
        # p - current profit
        # @cache
        # def dp(i, g, p):
        #     if i == len(group):
        #         return int(p >= minProfit)

        #     # if cache[i][g][p] != -1:
        #     #     return cache[i][n][p]

        #     res = dp(i + 1, g, p)
        #     if g + group[i] <= n:
        #         res += dp(i + 1, g + group[i], min(minProfit, p + profit[i]))

        #     # cache[i][g][p] = res % mod
        #     return res % mod

        # return dp(0, 0, 0)