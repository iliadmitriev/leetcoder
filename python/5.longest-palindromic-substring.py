class Solution:
    def longestPalindrome(self, s: str) -> str:
        cen = 0  # center of palindrome
        n = len(s)
        longest = 0
        pal = ""

        while cen < n:
            i, j = cen, cen
            # shift center if odd
            while j + 1 < n and s[i] == s[j + 1]:
                j += 1
                cen += 1

            while i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
                j += 1
                i -= 1

            if longest < j - i + 1:
                longest = j - i + 1
                pal = s[i : j + 1]

            cen += 1

        return pal
