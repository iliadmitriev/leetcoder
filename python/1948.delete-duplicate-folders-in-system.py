import collections


class Node:
    __slots__ = ("children", "serial")

    def __init__(self):
        self.children = {}
        self.serial = ""

    def __getitem__(self, key):
        return self.children.setdefault(key, Node())

    def calc_serial(self, counter: dict):
        if not self.children:
            return

        serials = []

        for key, child in self.children.items():
            child.calc_serial(counter)

            serials.append(f"{key}({child.serial})")

        self.serial = "".join(sorted(serials))

        counter[self.serial] += 1


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, path: list[str]) -> None:
        node = self.root
        for p in path:
            node = node[p]

    def hash_serial(self):
        counter = collections.Counter()
        self.root.calc_serial(counter)

        return counter


class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        trie = Trie()

        for path in paths:
            trie.add(path)

        freq = trie.hash_serial()

        res, path = [], []

        def dfs(node: Node, freq: dict, path: list[str], res: list[list[str]]):
            if freq[node.serial] > 1:
                return

            if path:
                res.append(path[:])

            for key, child in node.children.items():
                path.append(key)
                dfs(child, freq, path, res)
                path.pop()

        dfs(trie.root, freq, path, res)

        return res

