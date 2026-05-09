import collections

T = lambda: collections.defaultdict(lambda: T())  # noqa: E731


class Trie:
    def __init__(self):
        self.trie = T()

    def add(self, word: str) -> bool:
        trie = self.trie
        for c in word.split("/"):
            if "#" in trie:
                return False

            trie = trie[c]
        trie["#"] = T()

        return True


class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        trie = Trie()
        ans = []
        for f in sorted(folder, key=len):
            if trie.add(f):
                ans.append(f)
        return ans

