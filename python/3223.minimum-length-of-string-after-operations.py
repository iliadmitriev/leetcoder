
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)

        for k in freq.keys():
            if freq[k] >= 3:
                freq[k] = 1 + (freq[k] - 1) % 2

        return sum(v for v in freq.values())

