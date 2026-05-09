

import collections


class Solution:
    def sortString(self, s: str) -> str:
        base = ord("a")
        res = []

        N = 26
        c = [0] * N
        for ch in s:
            c[ord(ch) - base] += 1

        k = collections.deque([i for i in range(N) if c[i] > 0])

        while k:
            # find smallest
            for i in range(len(k)):
                p = k.popleft()
                c[p] -= 1
                res.append(chr(base + p))

                if c[p] > 0:
                    k.append(p)

            # find largest
            for i in range(len(k)):
                p = k.pop()
                c[p] -= 1
                res.append(chr(base + p))

                if c[p] > 0:
                    k.appendleft(p)

        return "".join(res)

