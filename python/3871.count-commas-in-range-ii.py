class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        e = 1000  # exponent 1e3, 1e6, 1e9, 1e12 ...
        p = 1  #  p (power), count of commas for exponent, 1,2,3,4...

        while e <= n:
            x = min(n + 1, e * 1000) # next exponent or the limit n (+1 inclusive)
            res += (x - e) * p

            e *= 1000
            p += 1

        return res
