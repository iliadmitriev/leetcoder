T = lambda: defaultdict(T)

class Trie:

    def __init__(self):
        self.root = T()
        self.SENTINEL = "#"

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node[char]
        node[self.SENTINEL] = True

    def _lookup(self, st: str) -> bool:
        node = self.root
        for char in st:
            if char in node:
                node = node[char]
            else:
                return None
        return node


    def search(self, word: str) -> bool:
        node = self._lookup(word)
        if not node:
            return False
        return self.SENTINEL in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self._lookup(prefix)
        if not node:
            return False
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)