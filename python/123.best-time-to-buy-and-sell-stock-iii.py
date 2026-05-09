class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        n - number of days
        k = 2 (max number of transactions)

        dp[i][j] = max{ dp[i][j - 1] , prices[j] - prices [m] + dp[i - 1][m] }

        dp - total max profit of i transactions and j days
        dp[i][j - 1] - case without performing a transaction, max profix stays the same as profix on previous day (j - 1)
        dp[i - 1][m] - max profit with previos transaction (i - 1) on buying day not greater than m
        
        i - transactions performed
        j - day number starting from 0
        m - 0 <= m < j - all possible buying days preceding day j
        
        days j |  0   1   2   3   4   5   6   7
        ---------------------------------------
        prices |  2   5   7   1   4   3   1   3
        ---------------------------------------
             0 |  0   0   0   0   0   0   0   0
        i    1 |  0   3   5   5   5   5   5   5
        tr   2 |  0   3   5   5   8   8   8   8
             3 |  0   3   5   5   8   8   8  10

        dp[*][0] = 0, because you can't have profit if there is only one day passed 
                      you need at least two days to close transaction

        dp[0][*]: all zeroes, because to have any profit, you need to perform more than 0 transactions
               (if you have preformed 0 transactions you can't have any profit)
        dp[1]: 0 
               max(0, 5 - min(2) + 0) = 3
               max(3, 7 - min(2, 5) + 0) = 5
               max(5, 1 - min(2, 5, 7) + 0) = 5        
               max(5, 1 - min(2, 5, 7, 1) + 0) = 5        
               max(5, 1 - min(2, 5, 7, 1, 4) + 0) = 5
               max(5, 1 - min(2, 5, 7, 1, 4, 3) + 0) = 5
               max(5, 1 - min(2, 5, 7, 1, 4, 3, 1) + 0) = 5
               max(5, 1 - min(2, 5, 7, 1, 4, 3, 1, 3) + 0) = 5
               
        dp[2]: 0
               max(0, 5 - min(2) + 0) = 3
               max(3, 7 - min(2, 5) + 0) = 5
               max(5, 1 - min(2, 5, 7) + 0) = 5
               max(5, 4 - min(2, 5, 7, 1) + 5) = 8
               max(8, 3 - min(2, 5, 7, 1, 4) + 5) = 8
               max(8, 1 - min(2, 5, 7, 1, 4, 3) + 5) = 8
               max(8, 3 - min(2, 5, 7, 1, 4, 3, 1) + 5) = 8

        dp[3]: 0
               max(0, 5 - min(2) + 0) = 3
               max(3, 7 - min(2, 5) + 0) = 5
               max(5, 1 - min(2, 5, 7) + 0) = 5
               max(5, 4 - min(2, 5, 7, 1) + 5) = 8
               max(8, 3 - min(2, 5, 7, 1, 4) + 5) = 8
               max(8, 1 - min(2, 5, 7, 1, 4, 3) + 5) = 8
               max(8, 3 - min(2, 5, 7, 1, 4, 3, 1) + 8) = 10
               
               
        Optimization
        ------------
        
        Idea: when calcualting min(2, 5, 7, 1, 4, 3, 1) - best buying price, you have to perform n operations for
              iterating previous prices.
              We can do it in constant time, caching this calculated minimum plus value of profit of previous transactions.
              
              modify recurrence formula, intorduce new variable max_diff:
              
              dp[i][j] = max{ dp[i][j - 1] , prices[j] + max_diff | max_diff = max(max_diff, dp[i - 1][j] - prices[j]) }


        dp[3]: 0
               max_diff = max(0 - 2) = -2       max(0, 5 + -2) = 3
               max_diff = max(-2, 3 - 5) = -2   max(3, 7 + -2) = 5
               max_diff = max(-2, 5 - 7) = -2   max(5, 1 + -2) = 5
               max_diff = max(-2, 5 - 1) =  4   max(5, 4 + 4) = 8
               max_diff = max( 4, 8 - 4) =  4   max(8, 3 + 4) = 8
               max_diff = max( 4, 8 - 3) =  5   max(8, 1 + 5) = 8
               max_diff = max( 5, 8 - 1) =  7   max(8, 3 + 7) = 10

        """
        n, k = len(prices), 2
        dp = [[0] * (n) for _ in range(k + 1)]
        max_diff = 0
        
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(
                    dp[i][j - 1],
                    prices[j] + max_diff
                )
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        
        return dp[k][n - 1]