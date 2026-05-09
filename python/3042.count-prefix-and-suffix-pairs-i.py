class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixSuffixPair(words[i], words[j]):
                    count += 1

        return count

    @staticmethod
    def isPrefixSuffixPair(w1: str, w2: str) -> bool:
        return w2.startswith(w1) and w2.endswith(w1)

