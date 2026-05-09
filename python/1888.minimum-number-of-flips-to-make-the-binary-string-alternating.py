class Solution:
    def minFlips(self, s: str) -> int:
        parity = "01"
        n = len(s)
        count = 0

        for i in range(n):
            if s[i] == parity[i % 2]:
                count += 1

        res = min(count, n - count)
        
        if n % 2 == 0:
            return res

        for i in range(n):
            if s[i] == parity[i % 2]:
                count -= 1

            if s[i] == parity[(i + 1) % 2]:
                count += 1

            res = min(res, count, n - count)

        return res