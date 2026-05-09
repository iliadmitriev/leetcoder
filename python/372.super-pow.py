class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        def pow(base: int, exp: int) -> int:
            base %= MOD

            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                exp //= 2
                base = (base * base) % MOD
            return result

        if a == 1:
            return 1

        return pow(a, int(''.join(map(str,b))))