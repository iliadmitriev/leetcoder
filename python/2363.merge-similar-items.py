import itertools
from collections import defaultdict


class Solution:
    def mergeSimilarItems(
        self, items1: list[list[int]], items2: list[list[int]]
    ) -> list[list[int]]:

        items: defaultdict[int, int] = defaultdict(int)
        for k, v, *_ in itertools.chain(items1, items2):
            items[k] += v

        return sorted(map(list, items.items()))

