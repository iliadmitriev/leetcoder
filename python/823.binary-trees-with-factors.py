MOD = 10**9 + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()

        # base case: all numbers are the trees with one root node by themself
        dp = {k: 1 for k in arr}

        for num1 in arr:
            for num2 in arr:
                num3, rem = divmod(num1, num2)

                if num3 == 0:
                    break

                if rem == 0 and num3 in dp:
                    dp[num1] += dp[num2] * dp[num3]
                    dp[num1] %= MOD

        return sum(dp.values()) % MOD