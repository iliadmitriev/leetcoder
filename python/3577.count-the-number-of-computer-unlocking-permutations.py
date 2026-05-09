

class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        lowest = complexity[0]

        if any(c <= lowest for c in complexity[1:]):
            return 0

        MOD = int(1e9) + 7

        def fact(n: int, mod: int) -> int:
            """modular factorial."""
            res = 1

            for i in range(1, n + 1):
                res = (res * i) % mod

            return res

        return fact(len(complexity) - 1, MOD)

