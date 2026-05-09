class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        dp(n, k) - numbers of arrays with k inverse pairs given n elements

        n - how many numbers left
        k - how many pairs is needed

        k == 0 - base case (no pairs needed, we gathered needed pairs), count 1.
                 we can create only one array with 0 inverse pairs (sorted array)
        n <= 1 - base case (no more numbers left to gather pairs, one number can't make pair), count 0
        """
        MOD = 10**9 + 7
        
        # # """O(n^2 * k)"""
        # dp = [[0] * (k + 1) for _ in range(n + 1)]
        # dp[0][0] = 1

        # for i in range(1, n + 1):
        #     for j in range(0, k + 1):
        #         for pairs in range(i):
        #             if j - pairs < 0:
        #                 continue

        #             dp[i][j] = (dp[i][j] + dp[i - 1][j - pairs]) % MOD

        # return dp[n][k]
        
        # @cache
        # def dp(n: int, k: int) -> int:
        #     """O(n^2 * k)"""
        #     if k == 0:
        #         return 1

        #     if n == 1:
        #         return 0

        #     res = 0
        #     for i in range(n):
        #         if k - i >= 0:
        #             res = (res + dp(n - 1, k - i)) % MOD

        #     return res
        # return dp(n, k)


        # """O(n * k)"""
        prev = [0] * (k + 1)
        prev[0] = 1

        for i in range(1, n + 1):
            cur = [0] * (k + 1)
            window = 0
            for j in range(0, k + 1):
                if j - i >= 0:
                    window -= prev[j - i]
                window = (window + prev[j]) % MOD
                cur[j] = window

            prev = cur

        return cur[k]