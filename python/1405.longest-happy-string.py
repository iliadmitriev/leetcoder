

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        res: list[str] = []

        curA, curB, curC = 0, 0, 0
        total = a + b + c

        for _ in range(total):
            # if "a" has a maximum count and
            # there is no 2 consecutive characters "a"
            # or "b" or "c" has 2 consecutive characters
            # and some of "a" characters left
            if (a >= b and a >= c and curA < 2) or (a > 0 and (curB >= 2 or curC >= 2)):
                res.append("a")
                a -= 1
                curA, curB, curC = curA + 1, 0, 0
            elif (b >= a and b >= c and curB < 2) or (
                b > 0 and (curA >= 2 or curC >= 2)
            ):
                res.append("b")
                b -= 1
                curA, curB, curC = 0, curB + 1, 0
            elif (c >= a and c >= b and curC < 2) or (
                c > 0 and (curA >= 2 or curB >= 2)
            ):
                res.append("c")
                c -= 1
                curA, curB, curC = 0, 0, curC + 1
            else:
                break

        return "".join(res)
