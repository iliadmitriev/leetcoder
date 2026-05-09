class Solution:
    def minEnd(self, n: int, x: int) -> int:
        mask = x
        i = 0  # bit position counter for mask
        n -= 1

        while n:
            if mask & 1 == 0:
                x |= (n & 1) << i
                n >>= 1

            i += 1
            mask >>= 1

        return x

