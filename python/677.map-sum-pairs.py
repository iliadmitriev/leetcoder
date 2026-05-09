class TrieNodeSum:
    """A Trie node"""

    def __init__(self, ch: Optional[str]) -> None:
        self.ch: Optional[str] = ch
        self.count: int = 0
        self.children: dict[str, 'TrieNodeSum'] = {}
        self.sum = 0

    @staticmethod
    def pprint(node: 'TrieNodeSum', prefix: str = '', children_prefix: str = ''):
        """ Pretty print tree posix style

            1
            ├── 2
            │   ├── 4
            │   └── 5
            └── 3
                ├── 6
                └── 7

        :param node: node to start from
        :param prefix: prefix for whole tree (default='')
        :param children_prefix: prefix for children (default='')
        :return: None
        """
        if not node:
            return
        print(prefix, end='')
        print(node.ch, node.count)
        size = len(node.children)
        for i, child in enumerate(node.children):
            if i == size - 1:
                TrieNodeSum.pprint(node.children[child], children_prefix + '└── ', children_prefix + '    ')
            else:
                TrieNodeSum.pprint(node.children[child], children_prefix + '├── ', children_prefix + '│   ')


class MapSum:
    def __init__(self) -> None:
        self.root = TrieNodeSum(ch=None)
        self.map_keys = {}

    def insert(self, key, val):
        """Insert key to tree

         Time: O(k) k is length of key

         Space: O(n) n - number of elements in trie

        :param key:
        :param val:
        :return:
        """
        delta = val - self.map_keys.get(key, 0)
        self.map_keys[key] = val
        cur = self.root
        cur.sum += delta
        for char in key:
            cur.children.setdefault(char, TrieNodeSum(char))
            cur = cur.children[char]
            cur.sum += delta

    def sum(self, prefix: str) -> int:
        """Gets sum of all words starting with `prefix` from a trie

         Time: O(k) k is length of key
         
         Space: O(1)

        :param prefix: given prefix to find
        :return: True if words with prefix are found
        """
        curr = self.root
        for ch in prefix:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return 0
        return curr.sum



