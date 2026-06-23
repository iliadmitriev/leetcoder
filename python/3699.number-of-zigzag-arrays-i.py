class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = int(1e9) + 7

        m = r - l + 1
        dp0, dp1 = [1] * m, [1] * m
        sum0, sum1 = [0] * (m + 1), [0] * (m + 1)

        for i in range(1, n):
            for j in range(m):
                sum0[j + 1] = (sum0[j] + dp0[j]) % MOD
                sum1[j + 1] = (sum1[j] + dp1[j]) % MOD

            for j in range(m):
                dp0[j] = (sum1[m] - sum1[j + 1]) % MOD
                dp1[j] = sum0[j]

        ans0 = sum(dp0) % MOD
        ans1 = sum(dp1) % MOD

        return (ans0 + ans1) % MOD
