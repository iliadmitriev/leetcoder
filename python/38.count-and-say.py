

class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s: str) -> str:
            if not s:
                return ""

            res = []
            i = 0

            while i < len(s):
                cur = s[i]
                cnt = 0

                while i < len(s) and s[i] == cur:
                    cnt += 1
                    i += 1

                res.append(str(cnt))
                res.append(cur)

            return "".join(res)

        cur = "1"

        for _ in range(n - 1):
            cur = rle(cur)

        return cur

