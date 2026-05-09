class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        base = ord("a") - 1

        for ch in s:
            if ch == "#":
                a, b = res.pop(), res.pop()
                res.append(10 * b + a)
            else:
                res.append(int(ch))

        return "".join(chr(base + ch) for ch in res)

