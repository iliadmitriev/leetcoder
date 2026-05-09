class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False

        def factorize(n: int) -> list[int]:
            fac = set()

            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    n //= i
                    fac.add(i)
                    fac.add(n)

            return sorted(fac, reverse=True)

        dp = [False] * (n + 1)
        dp[0] = True
        dp[2] = True

        for i in range(3, n + 1):
            for x in factorize(i):
                if not dp[i - x]:
                    dp[i] = True
                    break

        return dp[n]

