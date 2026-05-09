class Solution:
    def numSub(self, s: str) -> int:
        def count(n: int) -> int:
            return n * (n + 1) // 2

        cur = 0
        total = 0
        MOD = int(1e9 + 7)

        for ch in s:
            if ch == "1":
                cur += 1
            else:
                total += count(cur)
                total %= MOD
                cur = 0

        total += count(cur)
        total %= MOD

        return total

