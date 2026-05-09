

class Trie:
    def __init__(self):
        self.root = self._init()

    def _init(self) -> list:
        return [None] * 26

    def lookup(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")

            if node[idx] is None:
                return False

            node = node[idx]

        return True

    def add_words(self, word: str) -> None:
        """Add all words starting from every letter in the word."""
        for i in range(len(word)):
            self._add(word[i:])

    def _add(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")

            if node[idx] is None:
                node[idx] = self._init()

            node = node[idx]


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        res = []

        words.sort(key=len, reverse=True)
        trie = Trie()

        for w in words:
            if trie.lookup(w):
                res.append(w)

            trie.add_words(w)

        return res

