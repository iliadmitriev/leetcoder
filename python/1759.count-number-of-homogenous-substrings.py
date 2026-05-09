class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        MOD = 10**9 + 7
        for _, g in itertools.groupby(s):
            s = len(list(g))
            total = (total + s * (s + 1) // 2) % MOD
        return total