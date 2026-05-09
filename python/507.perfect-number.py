class Solution:
    @staticmethod
    def getPositiveDivisors(x: int) -> list[int]:
        """Factorize x and return the positive divisors excluding itself."""
        divs = []

        v = x

        while v % 2 == 0:
            divs.append(2)
            v //= 2

        i = 3

        while i * i <= x:
            while v % i == 0:
                divs.append(i)
                v //= i

            i += 2

        # add the last divisor but not itself (excluding prime)
        if v > 1 and v != x:
            divs.append(v)

        return divs

    def checkPerfectNumber(self, num: int) -> bool:
        divs = self.getPositiveDivisors(num)

        prefix = [1]
        mul = 1
        for v in divs:
            mul *= v
            prefix.append(mul)

        t = 0
        seen = set()

        for i in range(len(prefix)):
            for j in range(i, len(prefix)):
                v = prefix[j] // prefix[i]
                if v in seen or v == num:
                    continue

                t += v
                seen.add(v)

        return t == num


"""
Positive testcases:
6
28
496
8128
33550336
"""

