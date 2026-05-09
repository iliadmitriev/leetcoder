import math


class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        d = math.floor(math.log10(n) / 3)
        t = pow(1000, d)
        first = True
        res = []

        while t:
            r, n = divmod(n, t)

            v = str(r)

            if first:
                first = False
            else:
                v = v.zfill(3)

            res.append(v)

            t //= 1000

        return ".".join(res)

