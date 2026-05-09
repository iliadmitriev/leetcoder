import math
import operator
from collections import Counter, defaultdict
from functools import reduce


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        facs = [math.factorial(i) for i in range(n + 1)]

        def fac(x):
            return facs[x]

        # def dp(n: int, k: int, value: list[int], hm: dict[int, int]):
        #     res = 0
        #     if len(value) == n:
        #         d = reduce(lambda x, y: x * 10 + y, value)
        #         if d % k == 0:
        #             total = int(
        #                 fac(n) / reduce(lambda x, y: x * y, map(fac, hm.values()))
        #             )
        #
        #             withLeading = int(
        #                 fac(n - 1)
        #                 / reduce(
        #                     lambda x, y: x * y,
        #                     map(
        #                         fac, (v - int(i == 0 and v > 0) for i, v in hm.items())
        #                     ),
        #                 )
        #             )
        #
        #             res += total - withLeading
        #             print(d, dict(hm), total, withLeading, res)
        #
        #     elif len(value) <= n // 2 + n % 2 - 1:
        #         for i in range(len(value) == 0, 10):
        #             value.append(i)
        #             hm[i] += 1
        #             res += dp(n, k, value, hm)
        #             hm[i] -= 1
        #             value.pop()
        #
        #     else:
        #         i = value[n - len(value) - 1]
        #         value.append(i)
        #         hm[i] += 1
        #         res += dp(n, k, value, hm)
        #         hm[i] -= 1
        #         value.pop()
        #
        #     return res
        #
        # hm = defaultdict(int)
        # return dp(n, k, [], hm)

        base = 10 ** ((n - 1) // 2)
        cut = n % 2
        cache = set()

        for half in range(base, base * 10):
            palindrome = str(half)
            palindrome += palindrome[::-1][cut:]

            if int(palindrome) % k != 0:
                continue

            cache.add("".join(sorted(palindrome)))

        res = 0

        for h in cache:
            cnt = Counter(h)

            res += int(fac(n) / reduce(operator.mul, map(fac, cnt.values())))

            if cnt["0"] > 0:
                cnt["0"] -= 1
                res -= int(fac(n - 1) / reduce(operator.mul, map(fac, cnt.values())))

        return res

