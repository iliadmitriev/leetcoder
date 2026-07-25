class Solution:
    def maxProduct(self, n: int) -> int:
        d1, d2 = 0, 0

        while n:
            n, d = divmod(n, 10)

            if d >= d1:
                d1, d2 = d, d1
            elif d >= d2:
                d2 = d

        return d1 * d2
