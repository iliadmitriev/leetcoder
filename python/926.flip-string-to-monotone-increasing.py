class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        010110
        000111 - 2
        011111 - 2
        left_ones - how many 1's we have encountered moving left to right
        also how many flips have to do to make
        """
        res = 0
        left_ones = 0
        for char in s:
            if char == '1':
                left_ones += 1
            else:
                res = min(res + 1, left_ones)
        return res