class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        f = 1
        f_1 = 1
        f_2 = 1
        f_3 = 0

        for _ in range(n - 1):
            f = (2 * f_1 + f_3) % MOD
            f_3 = f_2
            f_2 = f_1
            f_1 = f

        return f

