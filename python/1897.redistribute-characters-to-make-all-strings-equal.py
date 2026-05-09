class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        n = len(words)
        for word in words:
            counter.update(word)

        return reduce(lambda res, x: res + (x % n), counter.values(), 0) == 0