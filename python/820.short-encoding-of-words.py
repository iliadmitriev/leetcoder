class TrieNode(object):
    __slots__ = ['child', 'height', 'end']
    
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.height = 0
        self.end = False
        
        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        height = 0
        for ch in word:
            node = node.child[ch]
            height += 1
            node.height = height
        node.end = True
        
    def count(self):
        res = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            
            if len(node.child) == 0 and node.end:
                res += node.height + 1
                continue
                
            for ch in node.child.keys():
                stack.append(node.child[ch])
                
        return res
            

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        tr = Trie()
        for word in words:
            tr.insert(word[::-1])
        return tr.count()