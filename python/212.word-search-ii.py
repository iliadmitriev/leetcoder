class Trie:
    def __init__(self, words):
        T = lambda: defaultdict(T)
        self.root = T()

        for word in words:
            self.add_word(word)

    def add_word(self, word: str, node=None):
        if node is None:
            node = self.root
        for char in word:
            node = node[char]
        node['#'] = True
        return node

    def search(self, word: str, node=None):
        if node is None:
            node = self.root
        for char in word:
            if char not in node:
                return None
            node = node[char]
        return node

    def found(self, node=None) -> bool:
        return node is not None and '#' in node
 
    def remove_word(self, word: str):
        node = self.root
        # find the word by chars collecting path
        path = []
        for char in word:
            if char not in node:
                return
            path.append((node, char))
            node = node[char]
        # if word is found traverse backwards all the path 
        # and delete nodes if their size is equal 1
        if '#' in node:
            del node['#']
            for node, char in reversed(path):
                if len(node[char]) == 0:
                    del node[char]

    def print(self, node=None):
        if node is None:
            node = self.root
        if isinstance(node, bool):
            return True
        res = {}
        for char, child in node.items():
            res[char] = self.print(child)
        return res


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie of all the words
        trie = Trie(words)
        # print(trie.print())
        m, n = len(board), len(board[0])
        res = set()

        def steps(y, x):
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # four adjacent cells (dy, dx)
            for dy, dx in dirs:
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < m and 0 <= new_x < n:
                    yield new_y, new_x


        def dfs(i, j):
            seen = set()
            stack = [(i, j, 0, None, '', False)]  # (row, col, depth, trie node, backtrack)
            while stack:
                y, x, depth, node, word, back = stack.pop()

                if back:
                    seen.discard((y, x))
                
                else:

                    word += board[y][x]
                    stack.append((y, x, depth, node, word, True))
                    next_node = trie.search(board[y][x], node)

                    if next_node is None:
                        continue
                    if trie.found(next_node):
                        res.add(word)
                        trie.remove_word(word)

                    if depth == 10:
                        continue

                    seen.add((y, x))

                    for new_y, new_x in steps(y, x):
                        if (new_y, new_x) not in seen:
                            stack.append((new_y, new_x, depth + 1, next_node, word, False))

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        return res

