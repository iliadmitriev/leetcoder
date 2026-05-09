from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:

        words = Counter(s1.split() + s2.split())

        return [word for word, count in words.items() if count == 1]

