class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxWords = 0

        def countWords(s: str) -> int:
            words = 0
            for c in s:
                if c == " ":
                    words += 1
            return words + 1

        for sentence in sentences:
            maxWords = max(maxWords, countWords(sentence))

        return maxWords

