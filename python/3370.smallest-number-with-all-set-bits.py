class Solution:
    def smallestNumber(self, n: int) -> int:
        len_n = n.bit_length()
        return (1 << len_n) - 1

