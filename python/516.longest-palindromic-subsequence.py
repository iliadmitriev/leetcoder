from functools import cache
import string


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def longest_palindrome(s: str) -> int:
            if not s:
                return 0
            
            longest = 1

            for letter in string.ascii_lowercase:
                left, right = s.find(letter), s.rfind(letter)
                if left != right:
                    longest = max(
                        longest, 
                        longest_palindrome(s[left + 1: right]) + 2
                    )
            
            return longest

        return longest_palindrome(s)