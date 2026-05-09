

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        out = []
        f = [0] * 10
        for d in digits:
            f[d] += 1

        for d1 in range(1, 10):
            if f[d1] == 0:
                continue

            f[d1] -= 1

            for d2 in range(0, 10):
                if f[d2] == 0:
                    continue

                f[d2] -= 1

                for d3 in range(0, 10, 2):
                    if f[d3] == 0:
                        continue

                    out.append(d1 * 100 + d2 * 10 + d3)

                f[d2] += 1

            f[d1] += 1

        return out

