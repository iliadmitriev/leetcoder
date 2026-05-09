from bisect import bisect

LIMIT = 3

class TrieNode(object):
    __slots__ = ['child', 'words']
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.words = list()


class Trie(object):
    
    def __init__(self, words: List[str]):
        self.root = TrieNode()

        for word in words:
            self.insert(word)
            

    def insert(self, word: str):
        node = self.root
        for ch in word:
            node = node.child[ch]
            node.words = heapq.nsmallest(LIMIT, [word] + node.words)

            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tr = Trie(products)
        res = []
        node = tr.root
        for ch in searchWord:
            node = node.child[ch]
            res.append(node.words)
            
        return res