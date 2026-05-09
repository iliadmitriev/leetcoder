class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        exact = {}
        lower = {}
        vowel = {}

        def vowelize(word):
            res = []
            for ch in word:
                low = ch.lower()
                if low in "aeiou":
                    res.append("a")
                else:
                    res.append(low)

            return "".join(res)

        for word in wordlist:
            if word not in exact:
                exact[word] = word

            lowered = word.lower()
            if lowered not in lower:
                lower[lowered] = word

            vowelized = vowelize(word)
            if vowelized not in vowel:
                vowel[vowelized] = word

        def correct(word: str) -> str:
            if word in exact:
                return exact[word]

            lowered = word.lower()
            if lowered in lower:
                return lower[lowered]

            vowelized = vowelize(word)
            if vowelized in vowel:
                return vowel[vowelized]

            return ""

        return [correct(word) for word in queries]

