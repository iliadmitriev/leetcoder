class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s[1:] + s[:-1]
        if s in t:
            return True

        return False