class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        pos = 1

        m, n = len(sentence), len(searchWord)

        i, j = 0, 0

        while i < m:

            j = 0
            while j < n and i < m and sentence[i] == searchWord[j]:
                i += 1
                j += 1

            if j == n:
                return pos

            while i < m and sentence[i] != " ":
                i += 1

            i += 1
            pos += 1

        return -1

