class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1

        while n:
            n, r = divmod(n, 10)

            s += r
            p *= r

        return p - s

