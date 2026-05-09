from collections import defaultdict, deque
from operator import getitem
from functools import reduce


T = lambda: defaultdict(T)

class WordDictionary:

    def __init__(self):
        self.root = T()
        self.SENTINEL = '#'

    def addWord(self, word: str) -> None:
        node = self.root
        node = reduce(getitem, word, node)
        node[self.SENTINEL] = {}

    def search(self, word: str) -> bool:
        queue = deque([self.root])
        n = len(word)
        pos = 0

        while queue:
            if pos == n:
                return any(self.SENTINEL in node for node in queue)

            char = word[pos]
            for _ in range(len(queue)):
                node = queue.popleft()
                if char in node:
                    queue.append(node[char])
                elif char == '.':
                    queue.extend(node.values())
            pos += 1
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)