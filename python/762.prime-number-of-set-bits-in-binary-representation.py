class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        upper = []
        while right:
            upper.append(right & 1)
            right >>= 1
        upper = upper[::-1]

        lower = []
        while left or len(lower) < len(upper):
            lower.append(left & 1)
            left >>= 1
        lower = lower[::-1]

        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 31}
        memo = {}

        def dfs(i, tight_low, tight_high, set_bits):
            if i == len(upper):
                return 1 if set_bits in primes else 0

            state = (i, tight_low, tight_high, set_bits)
            if state in memo:
                return memo[state]

            start = lower[i] if tight_low else 0
            end = upper[i] if tight_high else 1
            ways = 0
            for bit in range(start, end + 1):
                ways += dfs(
                    i + 1,
                    tight_low and bit == lower[i],
                    tight_high and bit == upper[i],
                    set_bits + bit,
                )

            memo[state] = ways
            return ways

        return dfs(0, True, True, 0)
