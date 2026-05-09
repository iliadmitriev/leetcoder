import collections

T = lambda: collections.defaultdict(T)
sentinel = "#"


class Trie:
    def __init__(self) -> None:
        self.root = T()

    def add(self, word: str) -> None:
        r = self.root
        for ch in word:
            r = r[ch]
        r[sentinel] = True

    def add_list(self, words: list[str]) -> None:
        for word in words:
            self.add(word)

    def lookup(self, word: str, stars: int = 0, i: int = 0, r=None) -> bool:
        if r is None:
            r = self.root

        if i == len(word):
            return sentinel in r

        ch = word[i]

        # step 1:
        # if match, try to take in case of success return
        if ch in r and self.lookup(word, stars, i + 1, r[ch]):
            return True

        # check if we have replacements left
        if stars == 0:
            return False

        # step 2:
        # no match (or in case of match without success from the previous step, also have to skip this letter)
        # iterate all the possible letters, except for matching one
        for child in r.values():
            if child == ch:  # this we have tried in previous step 1 (and no luck)
                continue

            if self.lookup(word, stars - 1, i + 1, child):
                return True

        # fallback
        return False


class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        t = Trie()
        t.add_list(dictionary)

        return [q for q in queries if t.lookup(q, 2)]
