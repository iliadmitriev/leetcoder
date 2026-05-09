class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)

        res = [n] * n
        pos = -n

        for i in range(n):
            if s[i] == c:
                pos = i

            res[i] = i - pos

        for i in range(n - 1, -1, -1):
            if s[i] == c:
                pos = i

            res[i] = min(res[i], abs(pos - i))

        return res

