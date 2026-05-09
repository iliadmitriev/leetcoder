from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        set1: dict[str, int] = Counter(words1)
        set2: dict[str, int] = Counter(words2)

        res = 0

        for w in set1.keys():
            if w in set2 and set1[w] == 1 and set2[w] == 1:
                res += 1
                set1[w] = 0
                set2[w] = 0

        for w in set2.keys():
            if w in set1 and set1[w] == 1 and set2[w] == 1:
                res += 1

        return res

