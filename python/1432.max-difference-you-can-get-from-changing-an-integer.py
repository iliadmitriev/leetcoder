class Solution:
    def maxDiff(self, num: int) -> int:
        value = []

        while num:
            value.append(num % 10)
            num //= 10

        a_exc = next(iter(v for v in value[::-1] if v < 9), 9)
        a_can = 9

        b_exc = value[-1]  # source candidate for exchange
        b_can = 1  # target candidate for exchange (default change to 1)

        if b_exc == 1:
            b_exc = next(iter(v for v in value[::-1] if v > 1), 9)
            b_can = 0

        a = 0
        b = 0

        while value:
            v = value.pop()
            a *= 10
            b *= 10

            a += a_can if v == a_exc else v
            b += b_can if v == b_exc else v

        return a - b

