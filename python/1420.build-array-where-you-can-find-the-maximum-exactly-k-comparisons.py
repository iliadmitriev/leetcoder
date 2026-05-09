class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """Dynamic Programing.

        dp(i, curMax, remain)

            i - current position [0, n]
            curMax - current maximum value [0, m]
            remain - number of maximums have to add to make array valid [k, 0]

        Start:
        
            dp(0, 0, k)
        
        Base:

            when i reached n
            if remain is 0, all maximums are generated => return 1
            return 0 otherwise (<0 - theres is not enough max values, >0 - there is extra maximum)

        Transition:

            * case 1: don't place maximum (place integer less than or equal to current maximum)
                dp(i, curMax, remain) = dp(i + 1, curMax, remain) * numOfCombiantions
                numOfCombiantions = (curMax - 1 + 1)

            * case 2: place maximum, from number of combinations: [curMax + 1; m]

        """
        MOD = 10**9 + 7

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        # set base case: remain == 0, i == n
        for curMax in range(m, -1, -1):
            dp[n][curMax][0] = 1
        
        for i in range(n - 1, -1, -1):
            for curMax in range(m, -1, -1):
                for remain in range(k + 1):
                    # optimize
                    if (m - curMax) < remain:
                        continue

                    # case 1: don't place max 
                    res = dp[i + 1][curMax][remain] * curMax % MOD


                    # case 2: place all possible max
                    if remain > 0:
                        for j in range(curMax + 1, m + 1):
                            res = (res + dp[i + 1][j][remain - 1]) % MOD

                    dp[i][curMax][remain] = res

        return dp[0][0][k]