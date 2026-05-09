class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() \
               or word.islower() \
               or (word[0:1].isupper() and word[1:].islower()) 