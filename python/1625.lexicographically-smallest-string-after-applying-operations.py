import collections
import math


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        k = len(s)  # lenght of chain
        rot = math.gcd(k, b)  # rotation step for chain of digits
        dig = math.gcd(10, a)  # rotation step for a single digit in chain
        v = list(map(int, s))  # initial state of chain
        res = v[:]

        def shift(t: list[int], i: int) -> list[int]:
            ch = t[i]
            inc = (10 + ch % dig - ch) % 10

            if not inc:
                return t

            for j in range(i, len(t), 2):
                t[j] = (t[j] + inc) % 10

            return t

        for i in range(0, k, rot):
            t = v[i:] + v[:i]

            t = shift(t, 1)
            if rot % 2:
                t = shift(t, 0)

            res = min(res, t)

        return "".join(map(str, res))

        start = tuple(map(int, s))
        q = collections.deque([start])

        seen = {start}
        res = start

        while q:
            cur = q.popleft()

            if cur < res:
                res = cur

            # add
            add = tuple((cur[i] + a) % 10 if i % 2 else cur[i] for i in range(k))

            if add not in seen:
                seen.add(add)
                q.append(add)

            # rotate
            rotate = cur[b:] + cur[:b]

            if rotate not in seen:
                seen.add(rotate)
                q.append(rotate)

        return "".join(map(str, res))

