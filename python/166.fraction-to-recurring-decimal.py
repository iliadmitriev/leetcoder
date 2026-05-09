class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        cache = {}
        res = []

        # sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        res.append(str(numerator // denominator))
        numerator = numerator % denominator
        numerator *= 10

        if numerator == 0:
            return "".join(res)

        res.append(".")

        while numerator != 0 and numerator not in cache:
            cache[numerator] = len(res)
            res.append(str(numerator // denominator))
            numerator = numerator % denominator
            numerator *= 10

        if numerator in cache:
            i = cache[numerator]
            res.insert(i, "(")
            res.append(")")

        return "".join(res)

