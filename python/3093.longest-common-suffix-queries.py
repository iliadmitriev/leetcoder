import sys


class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = sys.maxsize
        self.size = sys.maxsize

    def update(self, idx: int, size: int) -> None:
        if size < self.size:
            self.idx = idx
            self.size = size

    def child(self, ch: str) -> "TrieNode":
        if not self.children.get(ch):
            self.children[ch] = TrieNode()

        return self.children[ch]

    def check(self, ch: str) -> bool:
        return bool(self.children.get(ch))

    def get_index(self) -> int:
        return self.idx


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.data: list[str] = []

    def extend(self, new_data: list[str]) -> None:
        n = len(self.data)
        self.data.extend(new_data)

        for i in range(n, len(self.data)):
            self.insert(i, self.data[i])

    def insert(self, index: int, word: str) -> None:
        node = self.root
        size = len(word)

        for ch in word:
            node.update(index, size)
            node = node.child(ch)

        node.update(index, size)

    def find(self, word: str) -> int:
        node = self.root

        for ch in word:
            if not node.check(ch):
                break

            node = node.child(ch)

        return node.get_index()


class Solution:
    def stringIndices(
        self, wordsContainer: list[str], wordsQuery: list[str]
    ) -> list[int]:
        n = len(wordsQuery)
        wordsResponse = [-1] * n

        t = Trie()
        for i, word in enumerate(wordsContainer):
            t.insert(i, word[::-1])

        for i, word in enumerate(wordsQuery):
            wordsResponse[i] = t.find(word[::-1])

        return wordsResponse
