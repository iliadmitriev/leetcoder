class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = int(1e9) + 7
        n = len(s)
        BASE = ord("a")
        
        last = [0] * 26
        dp = 1

        for i, ch in enumerate(s):
            prev = dp
            dp *= 2
            
            j = ord(ch) - BASE
            dp -= last[j]
            last[j] = prev

            dp %= MOD

        return (dp - 1 + MOD) % MOD