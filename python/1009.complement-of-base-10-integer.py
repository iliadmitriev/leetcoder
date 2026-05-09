class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return ((1 << max(n, 1).bit_length()) - 1) ^ n