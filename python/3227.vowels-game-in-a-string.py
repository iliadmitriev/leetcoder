class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # key observation:
        # is Alice can loose only if there is no vowel in given string
        vowels = "aeiou"
        for ch in s:
            if ch in vowels:
                return True
        return False

