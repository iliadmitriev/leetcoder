class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        i = 0

        while num:
            if not num & 1:
                complement |= 1 << i

            num >>= 1
            i += 1

        return complement

