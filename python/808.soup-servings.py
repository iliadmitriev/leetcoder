import math


class Solution:
    def soupServings(self, n: int) -> float:
        """
        all amount in four operations are multiples of 25, so
        convert units ml to servings:
            
            1. serve 4 servings of A, 0 of B
            2. serve 3 of A, 1 of B
            3. serve 2 of A and 2 of B
            4. serve 1 of A, and 3 of B

        n <= 1e+9

        m = ceil(n / 25)

        m <= 4e+7

        eps = 1e-5 (precision)

        dp[i][j] - answer to the problem for i servings of A, 
                   and j servings of B at the beginning.

        if i == 0, j > 0, dp[0][j] - means that we ran out of A,
                but there is still some leftovers of B. (1)
        if i > 0, j == 0, dp[i][0] - means B is depleted, and
                still A is avalable. (0)
        if i == 0, j == 0, dp[0][0] - means ran out of both A and B
                            (1/2)
        State transfer (recurrence):

        if i > 0, j > 0:

            dp[i][j] = ( dp[max(0, i - 4)][j] 
                          + dp[max(0, i - 3)][j - 1] 
                          + dp[max(0, i - 2)][max(0, j - 2)] 
                          + dp[i - 1][max(0, j - 3)] ) / 4

        Time, Space: O(m ** 2)
        """
        if n >= 4500:
            return 1.0
        
        cache = {}

        def dp(i, j) -> float:
            if (i, j) in cache:
                return cache[(i, j)]

            if i == 0 and j == 0:
                res = 0.5
            elif i == 0:
                res = 1.0
            elif j == 0:
                res = 0.0
            else:
                res = (
                    dp(max(0, i - 100), j)
                    + dp(max(0, i - 75), max(0, j - 25))
                    + dp(max(0, i - 50), max(0, j - 50))
                    + dp(max(0, i - 25), max(0, j - 75))
                ) / 4.0
            
            cache[(i, j)] = res
            return res


        return dp(n, n)
