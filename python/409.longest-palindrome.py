from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        mid = 0
        res = 0

        for _, c in freq.items():
            res += c - c % 2
            mid |= c % 2

        return res + mid

