import bisect


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        balanced = []

        def gen(i: int, cur: int, m: int, voc: list[int], bal: list[int]) -> None:
            if i == m:
                if all(k == v for k, v in enumerate(voc) if v):
                    bal.append(cur)
                return

            for d in range(1, m + 1):
                if voc[d] == d or voc[d] + m - i < d:
                    continue

                voc[d] += 1
                gen(i + 1, cur * 10 + d, m, voc, bal)
                voc[d] -= 1

        gen(0, 0, len(str(n)), [0] * 10, balanced)
        gen(0, 0, len(str(n)) + 1, [0] * 10, balanced)

        return balanced[bisect.bisect_right(balanced, n)]

