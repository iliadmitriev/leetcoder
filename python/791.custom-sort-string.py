
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:

        c = Counter(s)
        res = []
        for o in order:
            if o not in c:
                continue
            res += [o] * c.pop(o)

        for k, v in c.items():
            res += [k] * v

        return "".join(res)

