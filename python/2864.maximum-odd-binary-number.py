class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        n = len(s)

        res = '1' * (ones - 1) + '0' * (n - ones) + '1'

        return res