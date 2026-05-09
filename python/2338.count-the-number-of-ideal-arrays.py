
from collections import defaultdict
from math import comb

MOD = 10**9 + 7


class Solution:
    def idealArrays(self, n: int, max_value: int) -> int:
        def getFactors(limit: int) -> list[list[int]]:
            """Factorize all numbers from 1 to limit.

            Return list of factor frequencies for each number.
            """
            # Precompute smallest prime factors (SPF) using sieve
            primes = [0] * (limit + 1)
            for i in range(2, limit + 1):
                if not primes[i]:
                    primes[i] = i

                for j in range(i * i, limit + 1, i):
                    if not primes[j]:
                        primes[j] = i

            factors = [[]] * 2
            for num in range(2, limit + 1):
                p = primes[num]
                v = num
                d = defaultdict(int)

                while v > 1 and v % p == 0:
                    d[p] += 1
                    v //= p
                    p = primes[v]

                factors.append(list(d.values()))

            return factors

        def getComb(n: int, k: int) -> int:
            """Get combinations of n things taken k at a time."""
            if k > n:
                return 0

            r = 1

            for d in range(k):
                r *= n - d
                r //= d + 1

            return r

        factors = getFactors(max_value)
        total = 0

        for num in range(1, max_value + 1):
            prod = 1

            for cnt in factors[num]:
                prod *= getComb(cnt + n - 1, cnt)
                prod %= MOD

            total += prod
            total %= MOD

        return total

