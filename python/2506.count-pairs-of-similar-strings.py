from collections import defaultdict


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        def kk(st: str) -> str:
            return "".join(sorted(set(st)))

        h: defaultdict[str, int] = defaultdict(int)
        for w in words:
            h[kk(w)] += 1

        return sum(v * (v - 1) // 2 for v in h.values())

