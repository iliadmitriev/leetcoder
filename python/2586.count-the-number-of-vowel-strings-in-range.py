class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:

        def isVowel(c: str) -> bool:
            return c in "aeiou"

        return sum(
            isVowel(words[i][0]) and isVowel(words[i][-1])
            for i in range(left, right + 1)
        )

