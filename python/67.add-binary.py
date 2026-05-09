class Solution:
    def addBinary(self, a: str, b: str) -> str:
        atoi = lambda s: reduce(lambda i, d: (i << 1) + ord(d) - 48, s, 0)

        def itoa(i: int) -> str:
            s = []
            while i:
                i, d = divmod(i, 2)
                s.append(chr(48 + d))
            return ''.join(reversed(s)) if s else '0'

        x = atoi(a)
        y = atoi(b)

        while y:
            x, y = y ^ x, (x & y) << 1

        return itoa(x)