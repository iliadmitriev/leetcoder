import math


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                v = i * i + j * j
                r = int(math.sqrt(v))

                if r > n:
                    break

                if r * r == v:
                    count += 2

        return count

