from itertools import groupby

class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        for sym, group in groupby(chars):
            n = len(list(group))
            if n == 1:
                res.append(str(sym))
            else:
                res.append(str(sym))
                res.extend(list(str(n)))

        chars[:] = res[:]

        return len(res)