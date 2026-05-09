class Solution:
    def countGoodNumbers(self, n: int) -> int:
        k, m = n // 2, n - n // 2
        mod = 10**9 + 7
        res = pow(5, m, mod) * pow(4, k, mod) % mod

        return res

