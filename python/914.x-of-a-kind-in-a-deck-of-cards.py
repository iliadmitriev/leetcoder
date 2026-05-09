from collections import Counter
from functools import reduce
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:

        freq = Counter(deck)
        return reduce(gcd, freq.values()) >= 2

