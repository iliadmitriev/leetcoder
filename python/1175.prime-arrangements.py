class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = int(1e9 + 7)

        def isPrime(n: int) -> int:
            if n < 2:
                return False

            if n == 2 or n == 3:
                return True

            if n % 2 == 0 or n % 3 == 0:
                return False

            i = 5

            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0 or n % (i + 4) == 0:
                    return False

                i += 6

            return True

        primes = 0
        notPrimes = 0

        for i in range(1, n + 1):
            if isPrime(i):
                primes += 1
            else:
                notPrimes += 1

        total = 1
        for i in range(2, primes + 1):
            total *= i
            total %= MOD

        for i in range(2, notPrimes + 1):
            total *= i
            total %= MOD

        return total

