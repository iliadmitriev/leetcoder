from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        # successor
        self.child =  defaultdict(TrieNode)
        # set of indexes for current node 
        self.words = set()
        
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx: int):
        """Insert word to trie.
        
        Args:
           word (str): word string
           idx (int): index of wor
        """
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
            curr.words.add(idx)

    def search(self, word: str) -> Set[int]:
        """Search for word (prefix) indexes.
        
        Args:
            word (str): prefix string
            
        Returns:
            (set of int): set of indexes found for given prefix
                          or an empty set otherwise
        """
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return set()
            curr = curr.child[ch]
        return curr.words

class WordFilter:

    def __init__(self, words: List[str]):
        self.pre = Trie()
        self.suf = Trie()
        # unique words dictionary with duplicates removed
        # use word as key and last index of word as value
        # words [a, a, a, b, b] --> memo {a:2, b:3}
        memo = dict(map(reversed, enumerate(words)))

        # add all unique words with index  to prefix trie
        # add all unique reversed words with index to suffix trie
        for word, idx in memo.items():
            self.pre.insert(word, idx)
            self.suf.insert(word[::-1], idx)

            
    def f(self, prefix: str, suffix: str) -> int:
        """Find index of latest word with prefix and suffix."""
        # search for prefix and suffix indexes
        pre = self.pre.search(prefix)
        suf = self.suf.search(suffix[::-1])
        # find prefix and suffix indexes intersection
        res = pre.intersection(suf)
        # if intersection is a empty set return -1
        # otherwise return maximum index
        return max(res) if res else -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)