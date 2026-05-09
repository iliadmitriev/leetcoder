class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        prev = ""
        counter = 0

        for ch in s:
            if ch == prev:
                counter += 1
            else:
                counter = 1

            if counter < 3:
                res.append(ch)

            prev = ch

        return "".join(res)

