class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:

        res = []
        j = 0
        n = len(spaces)
        for i, ch in enumerate(s):
            if j < n and spaces[j] == i:
                res.append(" ")
                j += 1
            res.append(ch)

        return "".join(res)

