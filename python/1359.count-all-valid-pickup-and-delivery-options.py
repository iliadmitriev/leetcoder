class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007

        res = 1
        for i in range(1, n + 1):
            valid_choises = i * (2 * i - 1)
            res *= valid_choises

        return res % MOD