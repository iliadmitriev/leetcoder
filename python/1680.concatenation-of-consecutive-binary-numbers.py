class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = int(1e9) + 7
        v = 0

        for i in range(1, n + 1):
            v = (v << i.bit_length() | i) % MOD

        return v
        