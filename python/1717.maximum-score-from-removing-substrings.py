class Solution:
    @staticmethod
    def getMax(s: str, a: str, b: str, x: int, y: int) -> int:
        c1, c2 = 0, 0
        res = 0

        for c in s:
            if c == a:
                c1 += 1
            elif c == b:
                if c1 > 0:
                    res += x
                    c1 -= 1
                else:
                    c2 += 1
            else:
                res += y * min(c1, c2)
                c1, c2 = 0, 0

        # Add the remaining
        res += y * min(c1, c2)

        return res

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            return self.getMax(s, "a", "b", x, y)
        else:
            return self.getMax(s, "b", "a", y, x)

