from functools import cache
from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        @cache
        def factorize(n: int) -> set[int]:
            res = set()
            while n % 2 == 0:
                res.add(2)
                n //= 2
            i = 3
            while i * i <= n:
                if n % i == 0:
                    res.add(i)
                    n //= i
                else:
                    i += 2
            if n > 1:
                res.add(n)
            return res

        primes = set()
        for num in set(nums):
            primes.update(factorize(num))

        return len(primes)

