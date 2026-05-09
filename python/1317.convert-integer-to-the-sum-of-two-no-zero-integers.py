class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        a, b = 0, 0
        p = 1  # power

        while n:
            n, r = divmod(n, 10)

            if r >= 2 or n == 0:
                a += p * (r - 1)
                b += p * (1)
            else:
                n -= 1
                r += 10
                a += p * (r - 9)
                b += p * (9)

            p *= 10

        return [a, b]

