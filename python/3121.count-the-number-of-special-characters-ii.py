import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0

        for a, A in zip(string.ascii_lowercase, string.ascii_uppercase):
            if a in word and A in word and word.rfind(a) < word.find(A):
                count += 1

        return count
