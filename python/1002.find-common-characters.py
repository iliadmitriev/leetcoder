from typing import List


class Solution:
    def count(self, s: str) -> List[int]:
        res = [0] * 26
        for ch in s:
            res[ord(ch) - ord("a")] += 1

        return res

    def commonChars(self, words: List[str]) -> List[str]:
        res = self.count(words[0])
        for word in words[1:]:
            tmp = self.count(word)
            for i in range(26):
                res[i] = min(res[i], tmp[i])

        out = []
        for i in range(26):
            for _ in range(res[i]):
                out.append(chr(ord("a") + i))

        return out

