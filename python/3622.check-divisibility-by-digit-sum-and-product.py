class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # d, s, p = 0, 0, 1
        # x = n

        # while x:
        #     x, d = divmod(x, 10)
        #     p *= d
        #     s += d

        def digits(x):
            while x > 0:
                yield x % 10
                x //= 10

        s, p = functools.reduce(
            lambda acc, d: (acc[0] + d, acc[1] * d),
            digits(n),
            (0, 1),
        )

        return n % (s + p) == 0
