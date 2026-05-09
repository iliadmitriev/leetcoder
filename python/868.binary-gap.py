class Solution:
    def binaryGap(self, n: int) -> int:
        # remove ending zeros
        while n & 1 == 0:
            n >>= 1

        longest = 0
        start = 0

        i = 0
        while n:
            if n & 1:
                longest = max(longest, i - start)
                start = i

            n >>= 1
            i += 1

        return longest

