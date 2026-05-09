

class TrieNode:
    __slots__ = ("count", "children")

    def __init__(self) -> None:
        self.count = 0
        self.children: dict["str", "TrieNode"] = {}


class Trie:

    def __init__(self) -> None:
        self.__root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.__root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            node.count += 1

    def addWords(self, words: list[str]) -> None:
        for word in words:
            self.addWord(word)

    def getPrefixScore(self, word: str) -> int:
        score = 0
        node = self.__root

        for ch in word:
            if ch not in node.children:
                break

            node = node.children[ch]
            score += node.count

        return score


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:

        trie = Trie()
        trie.addWords(words)

        return [trie.getPrefixScore(word) for word in words]

