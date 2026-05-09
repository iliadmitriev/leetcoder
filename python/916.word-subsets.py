from collections import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        def getFreq(word: str) -> list[int]:
            f = [0] * 26
            for ch in word:
                f[ord(ch) - ord("a")] += 1
            return f

        def isSubset(f1: list[int], f2: list[int]) -> bool:
            for i in range(26):
                if f1[i] < f2[i]:
                    return False
            return True

        freq2 = [0] * 26
        for w in set(words2):
            for ch, cnt in Counter(w).items():
                idx = ord(ch) - ord("a")
                freq2[idx] = max(freq2[idx], cnt)

        res = []
        for w in words1:
            f = getFreq(w)
            if isSubset(f, freq2):
                res.append(w)

        return res

