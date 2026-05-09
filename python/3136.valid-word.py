class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = set("aeiou")
        consonant = set("bcdfghjklmnpqrstvwxyz")

        def isVovel(c):
            return c.lower() in vowel

        def isConsonant(c):
            return c.lower() in consonant

        def isAlphaNum(c):
            return "a" <= c.lower() <= "z" or "0" <= c <= "9"

        hasVovel = False
        hasConsonant = False

        for c in word:
            if not hasVovel and isVovel(c):
                hasVovel = True

            if not hasConsonant and isConsonant(c):
                hasConsonant = True

            if not isAlphaNum(c):
                return False

        return hasVovel and hasConsonant

