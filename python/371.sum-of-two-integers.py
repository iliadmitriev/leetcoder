class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        # put a to result as the statring value
        res = a & mask
        # init carry
        carry = 0

        # if b is not 0
        while b:
            # perform "addition" of a, b operands, and limit bits to 32
            res = (a ^ b) & mask
            # calculate carry, and limit bits to 32 (!in python left shift is not limited)
            carry = ((a & b) << 1) & mask
            # move result to a, move carry to b 
            a = res
            b = carry

        # check if 32-th bit is 1, wich means number is negative
        return ~(res ^ mask) if (res >> 31) & 1 else res