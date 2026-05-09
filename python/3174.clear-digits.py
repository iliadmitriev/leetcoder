class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        for ch in s:
            if ch.isalpha():
                res.append(ch)
            else:
                if res and res[-1].isalpha():
                    res.pop()
                else:
                    res.append(ch)

        return "".join(res)

