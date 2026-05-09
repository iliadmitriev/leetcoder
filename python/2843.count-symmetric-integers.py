import math
from functools import cache


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        @cache
        def dsum(n: int) -> int:
            res = 0
            while n:
                res += n % 10
                n //= 10

            return res

        def sym(n: int) -> bool:
            size = int(math.log10(n)) + 1

            if size % 2 == 1:
                return False

            left, right = divmod(n, 10 ** (size // 2))

            return dsum(left) == dsum(right)

        return sum(sym(i) for i in range(low, high + 1))

