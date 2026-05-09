class Solution:
    @staticmethod
    def get_primes(left: int, right: int) -> list[int]:
        dp = [True] * (right + 1)
        dp[0] = dp[1] = False

        for step in range(2, int(right**0.5) + 1):
            for i in range(2 * step, right + 1, step):
                dp[i] = False

        return [i for i in range(left, right + 1) if dp[i]]

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False

        if n <= 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False

            i += 6

        return True

    def closestPrimes(self, left: int, right: int) -> list[int]:

        res = [-1, -1]
        curMin = right - left + 1
        prev = -1

        for n in range(left, right + 1):
            if not self.is_prime(n):
                continue

            if prev == -1:
                prev = n
                continue

            if n - prev <= 2:
                return [prev, n]

            if n - prev < curMin:
                curMin = n - prev
                res = [prev, n]

            prev = n

        return res

