
import math

L = int(math.sqrt(100_000))
IS_PRIME = [True] * L
IS_PRIME[0] = False
IS_PRIME[1] = False

for k in range(2 * 2, L, 2):
    IS_PRIME[k] = False

for i in range(3, L, 2):
    for k in range(2 * i, L, i):
        IS_PRIME[k] = False

PRIMES = [i for i, n in enumerate(IS_PRIME) if n]


class Solution:
    @staticmethod
    def get_prime(num: int) -> int:
        """Returns smallest prime factor of num or 0."""
        for p in PRIMES:
            if num <= p:
                return 0

            if num % p == 0:
                return p
        return 0

    def sumFourDivisors(self, nums: list[int]) -> int:
        total = 0

        for num in nums:
            p = self.get_prime(num)

            if p == 0:
                continue

            q = num // p

            if p * p == q or (p != q and self.get_prime(q) == 0):
                total += 1 + p + q + num

        return total

